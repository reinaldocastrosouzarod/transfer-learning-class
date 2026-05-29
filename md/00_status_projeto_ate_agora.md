# Status do Projeto até Agora

## Resumo Executivo
- **Objetivo da aula**: Introduzir o conceito e prática de Transfer Learning em 2 horas para graduandos de Ciência de Dados da Engenharia de Produção (PUC‑Rio).
- **Livro‑base**: *Introduction to Transfer Learning: Algorithms and Practice* (Wang & Chen, 2023).
- **Fase Atual**: Fase 3 - Desenvolvimento Prático (Benchmarks e Otimizações).

## Resultados dos Benchmarks (CIFAR-10)
Treinamento de uma arquitetura **ResNet-18** em um subset balanceado de **5.000 imagens** (10% do CIFAR-10):

| Experimento | Tipo | Épocas | Acurácia de Validação | Tempo de Execução | Observações |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Feature Extraction** | Transfer Learning | 5 | **74.5%** | **13.1 min** | Acurácia inicial estável em 72.4% na Época 1. |
| **Treinamento do Zero** | Pesos Aleatórios | 5 | **37.8%** | **25.9 min** | Começou em 30.8%. Demonstrou instabilidade na época 5 (overfitting/ruído). |
| **Fine-Tuning** | Ajuste Fino Geral | 5 | *Em andamento* | *Executando* | Rodando com taxa de aprendizado menor (lr=0.001). |

## Arquivos Existentes no Projeto

### Pasta `md/` (Documentação e Roteiros)
- `00_visao_geral.md` (resumo de conceitos).
- `01_plano_da_aula.md` (cronograma de 2 horas).
- `02_roteiro_teorico.md` (capítulo texto sobre Transfer Learning).
- `03_slides_aula.md` (roteiro de slides em markdown).
- `03_praticas.md` (descrição das práticas laboratoriais).
- `00_status_projeto_ate_agora.md` (este documento).

### Pasta `src/` (Scripts executáveis)
- `feature_extraction_cifar10.py` (treino congelado).
- `scratch_training_cifar10.py` (treino do zero).
- `fine_tuning_cifar10.py` (treino completo com lr baixo).

### Pasta `notebooks/` (Laboratórios interativos)
- `01_feature_extraction_cifar10.ipynb`
- `02_fine_tuning_cifar10.ipynb`

### Pasta `torch-example/` (Tutorial PyTorch - Formigas e Abelhas)
- `transfer_learning_tutorial.py` (ajustado para 5 épocas e num_workers=0 no Windows).
- Dataset `data/hymenoptera_data` copiado para a raiz para facilitar execução global.

## Próximos Passos
1. Concluir o benchmark de **Fine-Tuning** e catalogar seus resultados.
2. Gerar gráficos comparativos automatizados em `outputs/comparativo_cifar10.png`.
3. Criar os notebooks Jupyter interativos (versões aluno e professor).
4. Produzir a apresentação de slides HTML moderna e responsiva.
5. Criar o **Guia de Estudos Acadêmico** para os alunos.
6. Commit e Push final consolidando tudo.
