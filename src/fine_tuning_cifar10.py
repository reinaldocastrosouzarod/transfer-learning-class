import sys
import time
import warnings
import torch
# Força UTF-8 no stdout para evitar UnicodeEncodeError no Windows (cp1252)
sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import Subset
from tqdm import tqdm

warnings.filterwarnings("ignore", category=UserWarning)

# -------------------
# Funções de treinamento e avaliação
# -------------------
def train_one_epoch(model, loader, criterion, optimizer, device, epoch, num_epochs):
    """Treina o modelo por uma época com barra de progresso tqdm."""
    model.train()
    running_loss = 0.0
    pbar = tqdm(loader, desc=f'Época {epoch}/{num_epochs} [treino]',
                unit='batch', ncols=90, colour='green')
    for inputs, labels in pbar:
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item() * inputs.size(0)
        pbar.set_postfix({'loss': f'{running_loss / ((pbar.n + 1) * loader.batch_size):.4f}'})
    return running_loss / len(loader.dataset)


def evaluate(model, loader, device, epoch, num_epochs):
    """Avalia acurácia com barra de progresso tqdm."""
    model.eval()
    correct = 0
    total = 0
    pbar = tqdm(loader, desc=f'Época {epoch}/{num_epochs} [val]  ',
                unit='batch', ncols=90, colour='blue')
    with torch.no_grad():
        for inputs, labels in pbar:
            inputs, labels = inputs.to(device), labels.to(device)
            _, preds = torch.max(model(inputs), 1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)
            pbar.set_postfix({'acc': f'{correct / total:.4f}'})
    return correct / total


if __name__ == "__main__":

    # ── Configuração do subset ─────────────────────────────────────────────
    # IDÊNTICO aos anteriores para comparação justa.
    N_TRAIN = 5_000
    N_VAL   = 1_000

    # ── Transformações ──────────────────────────────────────────────────────
    transform = transforms.Compose([
        transforms.Resize(224),          # ResNet-18 espera 224×224
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    train_full = datasets.CIFAR10(root='data', train=True,  download=True, transform=transform)
    val_full   = datasets.CIFAR10(root='data', train=False, download=True, transform=transform)

    # Subset balanceado: 500 amostras por classe
    def balanced_subset(dataset, n_total):
        if n_total is None:
            return dataset
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

    train_dataset = balanced_subset(train_full, N_TRAIN)
    val_dataset   = balanced_subset(val_full,   N_VAL)

    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=64, shuffle=True,  num_workers=0)
    val_loader   = torch.utils.data.DataLoader(val_dataset,   batch_size=64, shuffle=False, num_workers=0)

    # ── Modelo com Fine-Tuning ──────────────────────────────────────────────
    # DIFERENÇA 1: Iniciamos com os pesos pré-treinados do ImageNet
    model = models.resnet18(weights=models.ResNet18_Weights.IMAGENET1K_V1)
    
    # DIFERENÇA 2: NÃO congelamos os parâmetros. Deixamos requires_grad = True (padrão)
    # permitindo que toda a rede se adapte aos novos dados de CIFAR-10.
    model.fc = nn.Linear(model.fc.in_features, 10)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model  = model.to(device)

    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    n_train_eff = len(train_dataset)
    n_val_eff   = len(val_dataset)

    print(f'\nDispositivo          : {device}')
    print(f'Parâmetros treináveis: {trainable:,} (TODOS - Fine-tuning)')
    print(f'Amostras de treino   : {n_train_eff:,} (subset balanceado, {n_train_eff//10}/classe)')
    print(f'Amostras de validação: {n_val_eff:,}')
    print()
    print('=' * 60)
    print(' Fine-Tuning — CIFAR-10 com ResNet-18 (5 épocas)')
    print(' 🚀 Pesos pré-treinados, ajuste fino de TODAS as camadas')
    print('=' * 60)

    criterion = nn.CrossEntropyLoss()
    
    # DIFERENÇA 3: Usamos uma taxa de aprendizado menor (lr=0.001) para não destruir
    # os pesos pré-treinados úteis já aprendidos no ImageNet.
    optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

    # ── Loop de treinamento ─────────────────────────────────────────────────
    num_epochs = 5
    t_start = time.time()

    for epoch in range(1, num_epochs + 1):
        t0   = time.time()
        loss = train_one_epoch(model, train_loader, criterion, optimizer, device, epoch, num_epochs)
        acc  = evaluate(model, val_loader, device, epoch, num_epochs)
        elapsed = time.time() - t0
        print(f'  ✔ Época {epoch}/{num_epochs}  |  Loss: {loss:.4f}  |  Val Acc: {acc:.4f}  |  {elapsed:.1f}s\n')

    total = time.time() - t_start
    print('=' * 60)
    print(f' Treinamento concluído em {total/60:.1f} min.')
    print(f' Acurácia final de validação: {acc:.4f} ({acc*100:.1f}%)')
    print('=' * 60)
    print()
    print('COMPARAÇÃO ESPERADA:')
    print('  Feature Extraction (Transfer Learning) → ~74.5%')
    print('  Treinamento do zero                    → ~30-40%')
    print(f'  Fine-Tuning (este script)              → {acc*100:.1f}%')
    print()
