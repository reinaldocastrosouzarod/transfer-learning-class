import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models

# -------------------
# Configurações básicas
# -------------------
transform = transforms.Compose([
    transforms.Resize(224),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

train_dataset = datasets.CIFAR10(root='data', train=True, download=True, transform=transform)
val_dataset   = datasets.CIFAR10(root='data', train=False, download=True, transform=transform)

train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=128, shuffle=True, num_workers=2)
val_loader   = torch.utils.data.DataLoader(val_dataset, batch_size=128, shuffle=False, num_workers=2)

# -------------------
# Modelo pré‑treinado (ResNet‑18) – Feature Extraction
# -------------------
model = models.resnet18(pretrained=True)
# Congelar todas as camadas convolucionais
for param in model.parameters():
    param.requires_grad = False
# Substituir a camada final para 10 classes (CIFAR‑10)
num_ftrs = model.fc.in_features
model.fc = nn.Linear(num_ftrs, 10)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.fc.parameters(), lr=0.01, momentum=0.9)

# -------------------
# Funções de treinamento e avaliação
# -------------------
def train_one_epoch(model, loader, criterion, optimizer, device):
    model.train()
    running_loss = 0.0
    for inputs, labels in loader:
        inputs, labels = inputs.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        running_loss += loss.item() * inputs.size(0)
    return running_loss / len(loader.dataset)

def evaluate(model, loader, device):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, labels in loader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            _, preds = torch.max(outputs, 1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)
    return correct / total

# -------------------
# Treinamento
# -------------------
def main():
    num_epochs = 5
    for epoch in range(num_epochs):
        loss = train_one_epoch(model, train_loader, criterion, optimizer, device)
        acc  = evaluate(model, val_loader, device)
        print(f'Epoch {epoch+1}/{num_epochs} – Loss: {loss:.4f} – Val Acc: {acc:.4f}')

    # --------------------------------
    # Dicas para o estudante (tempo < 10 min)
    # --------------------------------
    print('\nTreinamento concluído. Use a função `evaluate` para testar em novos dados.')

if __name__ == "__main__":
    main()
