# Aprendizado por Transferência (Transfer Learning) — ENG4502
**Introdução à Ciência de Dados · Engenharia de Produção · PUC-Rio**

Este repositório contém todo o material pedagógico, prático e teórico desenvolvido para a aula de **Transfer Learning** (com duração de 2 horas) da disciplina de Introdução à Ciência de Dados. O conteúdo é estruturado com base na literatura clássica e no livro-base de **Wang & Chen (2023)**, *Introduction to Transfer Learning: Algorithms and Practice*.

---

## 🚀 Destaques do Repositório

### 1. Apresentação & Teoria
*   **Slides da Aula ([slides/transfer_learning_aula.html](file:///C:/Users/rodri/gemini-sandbox/transfer-learning-class/slides/transfer_learning_aula.html))**: Slides interativos em HTML modernos com animações suaves, blocos de código formatados com destaque de sintaxe e o benchmark real plotado dinamicamente com Chart.js.
*   **Guia de Estudos ([md/guia_estudante.md](file:///C:/Users/rodri/gemini-sandbox/transfer-learning-class/md/guia_estudante.md))**: Material conceitual detalhando a taxonomia do Transfer Learning, a formulação matemática de domínios e tarefas, e o perigo do *Negative Transfer*. Inclui também um **Guia de Sobrevivência PyTorch** com soluções para bugs comuns (multiprocessing no Windows, OOM, `model.eval()`, etc.).

### 2. Laboratórios Práticos (`notebooks/`)
Divididos em versões para o aluno (com marcações para preencher) e gabaritos completos para o professor:
*   **Lab 1 — Feature Extraction ([Aluno](file:///C:/Users/rodri/gemini-sandbox/transfer-learning-class/notebooks/01_feature_extraction_cifar10_aluno.ipynb) | [Professor](file:///C:/Users/rodri/gemini-sandbox/transfer-learning-class/notebooks/01_feature_extraction_cifar10_professor.ipynb))**: Redimensionamento do CIFAR-10, congelamento do backbone convolucional da ResNet-18 e treinamento exclusivo da camada linear classificadora (`model.fc`).
*   **Lab 2 — Fine-Tuning ([Aluno](file:///C:/Users/rodri/gemini-sandbox/transfer-learning-class/notebooks/02_fine_tuning_cifar10_aluno.ipynb) | [Professor](file:///C:/Users/rodri/gemini-sandbox/transfer-learning-class/notebooks/02_fine_tuning_cifar10_professor.ipynb))**: Ajuste fino de todas as camadas utilizando taxas de aprendizado reduzidas para evitar o *Esquecimento Catastrófico*.

### 3. Simulador Web Interativo ([slides/simulator.html](file:///C:/Users/rodri/gemini-sandbox/transfer-learning-class/slides/simulator.html))
Um simulador interativo em HTML/JS com Chart.js onde os alunos podem experimentar live os efeitos de alterar:
*   A estratégia (Treinamento do zero, Feature Extraction, Fine-Tuning).
*   A taxa de aprendizado (Alta, Média ou Baixa).
*   O tamanho do dataset de destino.
*   O simulador gera curvas de treinamento época por época e explica didaticamente as causas de eventuais problemas de convergência.

### 4. Dever de Casa Prático (`homework/`)
Uma atividade de consolidação para os alunos entregarem de forma individual:
*   **Notebook Aluno ([03_homework_student](file:///C:/Users/rodri/gemini-sandbox/transfer-learning-class/homework/student/03_homework_transfer_learning_student.ipynb))**: Exercícios para implementar *Data Augmentation* no treino básico e codificar um *Fine-Tuning Parcial* (descongelando e treinando apenas as camadas da `layer4` + `fc` da ResNet-18 usando taxas discriminativas).
*   **Notebook Professor ([03_homework_professor](file:///C:/Users/rodri/gemini-sandbox/transfer-learning-class/homework/professor/03_homework_transfer_learning_professor.ipynb))**: Gabarito conceitual não-executado.
*   **Outputs do Gabarito ([homework/gabarito/](file:///C:/Users/rodri/gemini-sandbox/transfer-learning-class/homework/gabarito))**: Pasta contendo os pesos treinados (`.pt`), o log de treinamento oficial (`outputs.log`) e as curvas comparativas (`curvas_homework.png`).

---

## 📈 Resultados Comparativos dos Benchmarks

Todos os experimentos foram executados localmente no CPU utilizando a arquitetura **ResNet-18** e o subset balanceado do **CIFAR-10** (5.000 treino, 1.000 validação). 

Para mais detalhes teóricos e práticos, consulte o arquivo [md/benchmark_completo.md](file:///C:/Users/rodri/gemini-sandbox/transfer-learning-class/md/benchmark_completo.md).

| Rotina | Parâmetros Treináveis | Acurácia de Validação (Época 5) | Tempo Total (CPU) | Características principais |
| :--- | :---: | :---: | :---: | :--- |
| **Fine-Tuning Completo** | 11.2M | **87.90%** | **26.4 min** | Maior acurácia, taxa de aprendizado muito baixa (`lr=0.001`). |
| **Fine-Tuning Parcial** | 8.4M | **75.40%** | **14.7 min** | Descongela apenas `layer4`+`fc`. Excelente compromisso tempo-acurácia. |
| **Feature Extraction** | 5.1K | **74.50%** | **13.1 min** | Execução rápida, livre de overfitting grave. |
| **Zero + Augmentation** | 11.2M | **44.00%** | **26.0 min** | Treinado do zero. *Data Augmentation* mitigou overfitting (+6.2% de ganho). |
| **Zero Padrão (Scratch)** | 11.2M | **37.80%** | **25.9 min** | Instável. Sofreu overfitting severo pelo tamanho reduzido do dataset. |

---

## 🔧 Configuração e Execução do Ambiente

### 1. Pré-requisitos
Certifique-se de ter o Python 3.10 ou superior instalado. Instale as dependências listadas no [requirements.txt](file:///C:/Users/rodri/gemini-sandbox/transfer-learning-class/requirements.txt):
```bash
pip install -r requirements.txt
```

### 2. Executando os Slides e o Simulador
Não é necessária a execução de servidores complexos. Para abrir a apresentação ou o simulador, basta abrir os seguintes arquivos em qualquer navegador:
*   [slides/transfer_learning_aula.html](file:///C:/Users/rodri/gemini-sandbox/transfer-learning-class/slides/transfer_learning_aula.html) (Apresentação principal)
*   [slides/simulator.html](file:///C:/Users/rodri/gemini-sandbox/transfer-learning-class/slides/simulator.html) (Painel de simulação interativo)

Caso queira servir a pasta localmente via HTTP:
```bash
python -m http.server 8000
```
E acesse `http://localhost:8000/slides/transfer_learning_aula.html`.
