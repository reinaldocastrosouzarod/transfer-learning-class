# Transfer Learning Class

## Objetivo do Projeto
Desenvolver material didático para uma aula de 2 horas sobre **Transfer Learning** destinada a alunos de graduação em Ciência de Dados da Engenharia de Produção da PUC‑Rio.

## Contexto da Disciplina
A aula faz parte da disciplina *Aprendizado de Máquina* e tem como base o livro **"Introduction to Transfer Learning: Algorithms and Practice"** (Wang & Chen, 2023). O enfoque será a perspectiva do estudante, combinando teoria em estilo textbook e práticas simples que podem ser executadas no VS Code.

## Estrutura de Pastas
```
transfer-learning-class/
├── .vscode/                # Configurações do VS Code
├── data/                   # Datasets abertos
├── notebooks/              # Notebooks exploratórios
├── src/                    # Código‑fonte Python
├── slides/                 # Slides em markdown ou PDF
├── md/                     # Material em markdown (teoria, notas)
├── outputs/                # Saídas de experimentos
├── prompts/                # Prompts para o agente autônomo
│   ├── 00_system_context.md
│   ├── 01_master_prompt.md
│   └── 02_acceptance_criteria.md
├── requirements.txt        # Dependências do projeto
├── README.md               # Este arquivo
└── .gitignore              # Arquivos a serem ignorados
```

## Restrições Principais
- Código simples e legível para graduação.
- Datasets abertos e facilmente baixáveis.
- Tempo de execução das práticas ≤ 10 min (ideal ≤ 5 min).
- Todo material entregue em arquivos **Markdown**.
- Projeto deve ser executável e editável no **VS Code**.
- Preparado para ser usado por um agente autônomo em fases sequenciais.

## Visão Geral do Workflow do Agente
1. **Planejar a aula** – gerar plano detalhado, divisão teoria/prática.
2. **Criar roteiro teórico** – texto estilo textbook, baseado no livro.
3. **Gerar slides** – em markdown, exportáveis para PDF.
4. **Desenvolver práticas** – notebooks ou scripts Python com transfer learning simples.
5. **Produzir código** – pronto para rodar no VS Code, com instruções de execução.
6. **Escrever notas do professor** – dicas de condução e checkpoints.
7. **Compilar checklist operacional** – itens para garantir que tudo funciona em sala.
8. **Adicionar referências** – citações completas do livro e de datasets.

> **O agente deve seguir uma abordagem iterativa, validando cada entrega antes de avançar para a próxima fase.**

## Estado atual do projeto

- A fundação do projeto foi criada e versionada.
- Fase 1 foi concluída com sucesso.
- Arquivos‑base existentes: README.md, requirements.txt, .gitignore, prompts (00‑02 + 03‑04), md/00_status_projeto_ate_agora.md, md/00_log_fase_1.md, md/00_checkpoint_proxima_fase.md.
- Próxima fase esperada: geração da teoria e dos slides (Fase 2).
