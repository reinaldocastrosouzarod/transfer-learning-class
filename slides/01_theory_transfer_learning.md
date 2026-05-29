# Slides – Teoria da 1ª hora (Transfer Learning)\
\
## Slide 1 – Título\
- Transfer Learning: Conceitos e Motivação\
- **Objetivo da aula:** entender o que é transfer learning e como usá‑lo em prática.\
\
## Slide 2 – Definição\
- *Transfer Learning* = reutilização de conhecimento já aprendido por um modelo pré‑treinado para resolver outra tarefa.\
- Diferenças entre **fine‑tuning** e **feature‑extraction**.\
\
## Slide 3 – Por que usar?\
- Reduz custo computacional.\
- Menos dados rotulados necessários.\
- Melhora a performance em domínios similares.\
\
## Slide 4 – Pipeline típico\
1. Escolher modelo pré‑treinado (ex.: ResNet‑18).\
2. Congelar camadas (feature‑extraction) ou treinar tudo (fine‑tuning).\
3. Substituir a camada final para o número de classes da nova tarefa.\
4. Treinar / validar.\
\
## Slide 5 – Exemplo prático (CIFAR‑10)\
- Dataset: CIFAR‑10 (10 classes, imagens 32×32).\
- Modelo: ResNet‑18 pré‑treinado em ImageNet.\
- Estratégia: **feature‑extraction** (congelar todas as camadas exceto a última).\
- Tempo estimado: < 10 min em CPU/GPU.\
\
## Slide 6 – Métricas de avaliação\
- Acurácia, **Top‑1** e **Top‑5**.\
- Matriz de confusão.\
\
## Slide 7 – Perguntas para a turma\
- Quando o fine‑tuning pode ser mais vantajoso que feature‑extraction?\
- Quais são os riscos de usar modelos pré‑treinados em domínios muito diferentes?\
\
---\
**Referências**\
- Wang, Y., & Chen, X. (2023). *Introduction to Transfer Learning: Algorithms and Practice.*\
- PyTorch Documentation – Transfer Learning tutorials.\
