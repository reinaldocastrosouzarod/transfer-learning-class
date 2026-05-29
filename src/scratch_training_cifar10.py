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
# (idênticas ao feature_extraction_cifar10.py — comparação justa)
# -------------------
def train_one_epoch(model, loader, criterion, optimizer, device, epoch, num_epochs):
    """Treina o modelo por uma época com barra de progresso tqdm."""
    model.train()
    running_loss = 0.0
    pbar = tqdm(loader, desc=f'Época {epoch}/{num_epochs} [treino]',
                unit='batch', ncols=90, colour='red')
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
                unit='batch', ncols=90, colour='yellow')
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
    # IDÊNTICO ao feature_extraction_cifar10.py — comparação controlada.
    N_TRAIN = 5_000   # mesmos 5.000 exemplos de treino
    N_VAL   = 1_000   # mesmos 1.000 exemplos de validação

    # ── Transformações ──────────────────────────────────────────────────────
    # IDÊNTICAS ao feature_extraction_cifar10.py
    transform = transforms.Compose([
        transforms.Resize(224),          # ResNet-18 espera 224×224
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
    ])

    train_full = datasets.CIFAR10(root='data', train=True,  download=True, transform=transform)
    val_full   = datasets.CIFAR10(root='data', train=False, download=True, transform=transform)

    # Subset balanceado: 500 amostras por classe (10 classes × 500 = 5.000)
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

    # ── Modelo SEM pesos pré-treinados — Treinamento do Zero ───────────────
    # DIFERENÇA 1: weights=None  → pesos inicializados aleatoriamente
    model = models.resnet18(weights=None)
    # DIFERENÇA 2: NÃO congelamos nada → todos os 11M parâmetros são treináveis
    # (nenhum `param.requires_grad = False`)
    model.fc = nn.Linear(model.fc.in_features, 10)   # 10 classes CIFAR-10

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model  = model.to(device)

    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    n_train_eff = len(train_dataset)
    n_val_eff   = len(val_dataset)

    print(f'\nDispositivo          : {device}')
    print(f'Parâmetros treináveis: {trainable:,} (TODOS — sem congelamento)')
    print(f'Amostras de treino   : {n_train_eff:,} (subset balanceado, {n_train_eff//10}/classe)')
    print(f'Amostras de validação: {n_val_eff:,}')
    print()
    print('=' * 60)
    print(' Treinamento do ZERO — CIFAR-10 com ResNet-18 (5 épocas)')
    print(' ⚠  Pesos aleatórios, sem Transfer Learning')
    print('=' * 60)

    criterion = nn.CrossEntropyLoss()
    # Mesmo otimizador, mesmos hiperparâmetros — comparação justa
    optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

    # ── Loop de treinamento ─────────────────────────────────────────────────
    num_epochs = 5
    t_start = time.time()

    for epoch in range(1, num_epochs + 1):
        t0   = time.time()
        loss = train_one_epoch(model, train_loader, criterion, optimizer, device, epoch, num_epochs)
        acc  = evaluate(model, val_loader, device, epoch, num_epochs)
        elapsed = time.time() - t0
        print(f'  ✗ Época {epoch}/{num_epochs}  |  Loss: {loss:.4f}  |  Val Acc: {acc:.4f}  |  {elapsed:.1f}s\n')

    total = time.time() - t_start
    print('=' * 60)
    print(f' Treinamento concluído em {total/60:.1f} min.')
    print(f' Acurácia final de validação: {acc:.4f} ({acc*100:.1f}%)')
    print('=' * 60)
    print()
    print('COMPARAÇÃO ESPERADA:')
    print('  Feature Extraction (Transfer Learning) → ~74.5%')
    print(f'  Treinamento do zero (este script)      → {acc*100:.1f}%')
    print()
    print('NOTA: Mesmos dados, mesmas épocas, mesmo otimizador.')
    print('      A única diferença é a ausência de pesos pré-treinados.')
