import os
import matplotlib.pyplot as plt

# Criar pasta outputs se não existir
os.makedirs("outputs", exist_ok=True)

# ── Dados dos Experimentos ─────────────────────────────────────────────────
epochs = [1, 2, 3, 4, 5]

# 1. Feature Extraction (ResNet-18 Congelada) - Val Acc final: 74.5%
fe_loss = [1.1282, 0.6661, 0.6282, 0.5734, 0.5492]
fe_acc  = [0.7240, 0.7360, 0.7560, 0.7340, 0.7450]

# 2. Treinamento do Zero (ResNet-18 Aleatória) - Val Acc final: 37.8%
scratch_loss = [2.0210, 1.6629, 1.5229, 1.3871, 1.1587]
scratch_acc  = [0.3080, 0.3190, 0.3490, 0.4270, 0.3780]

# 3. Fine-Tuning (ResNet-18 Parâmetros Livres) - Val Acc final: 87.9%
ft_loss = [1.4790, 0.5737, 0.3451, 0.2232, 0.1509]
ft_acc  = [0.7480, 0.8410, 0.8640, 0.8720, 0.8790]

# ── Configurações de Estilo (Dark Mode Elegante - Padrão PUC) ──────────────
plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
fig.patch.set_facecolor('#0d1117')

for ax in (ax1, ax2):
    ax.set_facecolor('#161b22')
    ax.tick_params(colors='#8b949e')
    ax.spines['bottom'].set_color('#30363d')
    ax.spines['top'].set_color('#30363d')
    ax.spines['left'].set_color('#30363d')
    ax.spines['right'].set_color('#30363d')
    ax.grid(True, alpha=0.15, color='#30363d')

# ── Plot de Loss ───────────────────────────────────────────────────────────
ax1.plot(epochs, fe_loss, 'o-', color='#58a6ff', linewidth=2.5, markersize=8, label='Feature Extraction (ResNet-18)')
ax1.plot(epochs, scratch_loss, 's-', color='#f78166', linewidth=2.5, markersize=8, label='Treinamento do Zero (ResNet-18)')
ax1.plot(epochs, ft_loss, '^-', color='#bc8cff', linewidth=2.5, markersize=8, label='Fine-Tuning Completo (ResNet-18)')
ax1.set_title('Curva de Loss por Época', fontsize=14, fontweight='bold', color='#e6edf3', pad=15)
ax1.set_xlabel('Época', fontsize=12, color='#8b949e')
ax1.set_ylabel('Loss', fontsize=12, color='#8b949e')
ax1.legend(facecolor='#21262d', edgecolor='#30363d', labelcolor='#e6edf3')

# ── Plot de Acurácia ───────────────────────────────────────────────────────
ax2.plot(epochs, [x * 100 for x in fe_acc], 'o-', color='#58a6ff', linewidth=2.5, markersize=8, label='Feature Extraction (ResNet-18)')
ax2.plot(epochs, [x * 100 for x in scratch_acc], 's-', color='#f78166', linewidth=2.5, markersize=8, label='Treinamento do Zero (ResNet-18)')
ax2.plot(epochs, [x * 100 for x in ft_acc], '^-', color='#bc8cff', linewidth=2.5, markersize=8, label='Fine-Tuning Completo (ResNet-18)')
ax2.set_title('Acurácia de Validação por Época', fontsize=14, fontweight='bold', color='#e6edf3', pad=15)
ax2.set_xlabel('Época', fontsize=12, color='#8b949e')
ax2.set_ylabel('Acurácia (%)', fontsize=12, color='#8b949e')
ax2.set_ylim(0, 100)
ax2.legend(facecolor='#21262d', edgecolor='#30363d', labelcolor='#e6edf3')

plt.tight_layout()

# Salvar gráfico comparativo
output_path = "outputs/comparativo_cifar10.png"
plt.savefig(output_path, dpi=150, facecolor='#0d1117')
print(f"Grafico salvo com sucesso em: {output_path}")
