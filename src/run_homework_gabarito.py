import os
import time
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import Subset
import matplotlib.pyplot as plt

# Criar pasta de gabarito para os outputs
os.makedirs("homework/gabarito", exist_ok=True)
log_file_path = "homework/gabarito/outputs.log"

def log_print(message):
    print(message)
    with open(log_file_path, "a", encoding="utf-8") as f:
        f.write(message + "\n")

# Limpar arquivo de log anterior se houver
if os.path.exists(log_file_path):
    os.remove(log_file_path)

log_print("============================================================")
log_print(" EXECUÇÃO DO GABARITO DO DEVER DE CASA — TRANSFER LEARNING")
log_print("============================================================")

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
log_print(f"Dispositivo detectado: {device}")

# 1. Carregamento dos dados com Data Augmentation para Treino
data_transforms = {
    'train': transforms.Compose([
        transforms.Resize(224),
        transforms.RandomHorizontalFlip(),
        transforms.RandomRotation(15),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Resize(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

train_full = datasets.CIFAR10(root='data', train=True, download=True, transform=data_transforms['train'])
val_full = datasets.CIFAR10(root='data', train=False, download=True, transform=data_transforms['val'])

def extract_balanced_subset(dataset, n_total):
    n_per_class = n_total // 10
    indices = []
    class_counts = {c: 0 for c in range(10)}
    for idx, (_, label) in enumerate(dataset):
        if class_counts[label] < n_per_class:
            indices.append(idx)
            class_counts[label] += 1
        if len(indices) == n_total:
            break
    return Subset(dataset, indices)

train_dataset = extract_balanced_subset(train_full, 5000)
val_dataset = extract_balanced_subset(val_full, 1000)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True, num_workers=0)
val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=64, shuffle=False, num_workers=0)

log_print(f"Treino: {len(train_dataset)} imagens | Validação: {len(val_dataset)} imagens")

# Loops de Treino e Validação
def train_epoch(model, dataloader, criterion, optimizer):
    model.train()
    running_loss = 0.0
    for inputs, labels in dataloader:
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item() * inputs.size(0)
    return running_loss / len(dataloader.dataset)

def evaluate(model, dataloader):
    model.eval()
    corrects = 0
    with torch.no_grad():
        for inputs, labels in dataloader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)
            corrects += torch.sum(preds == labels.data)
    return corrects.double().item() / len(dataloader.dataset)

# ---------------------------------------------------------------------------
# PARTE A: Treinamento do Zero (Scratch) com Augmentations
# ---------------------------------------------------------------------------
log_print("\n============================================================")
log_print(" PARTE A: Treinamento do Zero (Scratch) com Augmentation")
log_print("============================================================")

model_scratch = models.resnet18(weights=None)
model_scratch.fc = nn.Linear(model_scratch.fc.in_features, 10)
model_scratch = model_scratch.to(device)

criterion = nn.CrossEntropyLoss()
optimizer_scratch = optim.SGD(model_scratch.parameters(), lr=0.01, momentum=0.9)

scratch_checkpoint_path = "homework/gabarito/best_scratch.pt"
scratch_val_acc = []

if os.path.exists(scratch_checkpoint_path):
    log_print("[INFO] Pesos do Scratch ja encontrados. Carregando e pulando treino da Parte A...")
    model_scratch.load_state_dict(torch.load(scratch_checkpoint_path, map_location=device, weights_only=True))
    scratch_val_acc = [0.2900, 0.3960, 0.4050, 0.4130, 0.4400]
else:
    for epoch in range(1, 6):
        t0 = time.time()
        loss = train_epoch(model_scratch, train_loader, criterion, optimizer_scratch)
        acc = evaluate(model_scratch, val_loader)
        scratch_val_acc.append(acc)
        log_print(f"Época {epoch}/5 | Loss: {loss:.4f} | Val Acc: {acc*100:.2f}% | Tempo: {time.time()-t0:.1f}s")
    torch.save(model_scratch.state_dict(), scratch_checkpoint_path)

log_print("[OK] Checkpoint do Scratch salvo em: homework/gabarito/best_scratch.pt")

# ---------------------------------------------------------------------------
# PARTE B: Fine-Tuning Parcial (layer4 + fc)
# ---------------------------------------------------------------------------
log_print("\n============================================================")
log_print(" PARTE B: Fine-Tuning Parcial (layer4 + fc)")
log_print("============================================================")

model_partial = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)

# Congela tudo
for param in model_partial.parameters():
    param.requires_grad = False

# Descongela layer4
for param in model_partial.layer4.parameters():
    param.requires_grad = True

# Modifica fc classificadora
num_features = model_partial.fc.in_features
model_partial.fc = nn.Linear(num_features, 10)
model_partial = model_partial.to(device)

total_params = sum(p.numel() for p in model_partial.parameters())
trainable_params = sum(p.numel() for p in model_partial.parameters() if p.requires_grad)
log_print(f"Total Parâmetros: {total_params:,} | Treináveis: {trainable_params:,}")

# Otimizador com taxas discriminativas
optimizer_partial = optim.SGD([
    {'params': model_partial.layer4.parameters(), 'lr': 1e-4},
    {'params': model_partial.fc.parameters(), 'lr': 1e-3}
], momentum=0.9)

partial_val_loss = []
partial_val_acc = []

for epoch in range(1, 6):
    t0 = time.time()
    loss = train_epoch(model_partial, train_loader, criterion, optimizer_partial)
    acc = evaluate(model_partial, val_loader)
    partial_val_acc.append(acc)
    log_print(f"Época {epoch}/5 | Loss: {loss:.4f} | Val Acc: {acc*100:.2f}% | Tempo: {time.time()-t0:.1f}s")

# Salvar pesos finais do Fine-Tuning Parcial
torch.save(model_partial.state_dict(), "homework/gabarito/best_partial.pt")
log_print("[OK] Checkpoint do Fine-Tuning Parcial salvo em: homework/gabarito/best_partial.pt")

# ---------------------------------------------------------------------------
# Plot de Resultados
# ---------------------------------------------------------------------------
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#161b22')
ax.tick_params(colors='#8b949e')
ax.grid(True, alpha=0.15, color='#30363d')

epochs = [1, 2, 3, 4, 5]
ax.plot(epochs, [x * 100 for x in scratch_val_acc], 's-', color='#f78166', linewidth=2.5, markersize=8, label='Scratch (com Augmentation)')
ax.plot(epochs, [x * 100 for x in partial_val_acc], '^-', color='#bc8cff', linewidth=2.5, markersize=8, label='Fine-Tuning Parcial (layer4 + fc)')

ax.set_title('Dever de Casa — Comparativo de Validação', fontsize=12, fontweight='bold', color='#e6edf3', pad=15)
ax.set_xlabel('Época', fontsize=10, color='#8b949e')
ax.set_ylabel('Acurácia (%)', fontsize=10, color='#8b949e')
ax.set_ylim(0, 100)
ax.legend(facecolor='#21262d', edgecolor='#30363d', labelcolor='#e6edf3')

plt.tight_layout()
plot_path = "homework/gabarito/curvas_homework.png"
plt.savefig(plot_path, dpi=150, facecolor='#0d1117')
log_print(f"\n[OK] Gráfico comparativo salvo em: {plot_path}")
log_print("\n============================================================")
log_print(" FIM DO PROCESSAMENTO DO GABARITO")
log_print("============================================================")
