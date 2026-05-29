# Resumo Geral de Benchmarks (CIFAR-10)
**ENG4502 — Introdução à Ciência de Dados · PUC-Rio**

Este documento consolida as estatísticas oficiais de todos os experimentos práticos e de dever de casa executados em CPU utilizando a arquitetura **ResNet-18** e o subset balanceado do **CIFAR-10** (5.000 imagens de treino, 1.000 de validação).

---

## 📊 Tabela Geral Comparativa

Abaixo está o resumo comparativo de todas as abordagens de treinamento ordenadas pelo desempenho final de validação:

| Rotina | Abordagem | Parâmetros Treináveis | Acurácia de Validação (Época 5) | Tempo Total de Execução (CPU) | Observações / Comportamento |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Fine-Tuning Completo** | Transfer Learning (All) | **11.2M** (11.181.642) | **87.90%** | **26.4 min** | **Melhor acurácia geral**. Ajuste fino de todas as camadas com taxa de aprendizado baixa (`lr=0.001`). |
| **Fine-Tuning Parcial** | Transfer Learning (layer4) | **8.4M** (8.398.858) | **75.40%** | **14.7 min** | Abordagem para o dever de casa. Descongela apenas a `layer4` + `fc` com taxas discriminativas. |
| **Feature Extraction** | Transfer Learning (FC only)| **5.1K** (5.130) | **74.50%** | **13.1 min** | **Mais rápida e estável**. Ideal para restrições severas de computação e datasets pequenos. |
| **Zero (Scratch) + Augmentation**| Pesos Aleatórios | **11.2M** (11.181.642) | **44.00%** | **26.0 min** | Dever de casa. O uso de regularização por *Data Augmentation* reduziu o overfitting e subiu a acurácia em **+6.2%**. |
| **Zero (Scratch) Padrão** | Pesos Aleatórios | **11.2M** (11.181.642) | **37.80%** | **25.9 min** | Modelo do zero sem regularização. Sofreu overfitting precoce e flutuações de ruído no final (época 5). |

---

## 💡 Principais Conclusões Didáticas para Aula

1. **Feature Extraction vs. Treino do Zero**:
   * O Feature Extraction entrega uma acurácia inicial instantânea (72.4% na época 1) e termina com 74.5% em quase metade do tempo da rede do zero. Isso prova que os filtros pré-treinados no ImageNet são genéricos e robustos para o CIFAR-10.
2. **O Poder do Fine-Tuning**:
   * Descongelar as camadas convolucionais (Completo ou Parcial) permite que a rede especialize suas características geométricas para a nova tarefa, subindo o desempenho para patamares superiores (>80%), porém exige o cuidado de usar taxas de aprendizado baixas para evitar o **Esquecimento Catastrófico**.
3. **Parâmetros vs. Velocidade**:
   * Treinar apenas a `layer4` + `fc` (8.4M parâmetros) economiza cerca de 45% do esforço computacional no CPU em relação ao Fine-Tuning completo, provando que congelar as primeiras camadas convolucionais acelera significativamente o ciclo de desenvolvimento de modelos profundos.
