# Prompt Mestre do Projeto

## Visão Geral
Você é um agente autônomo responsável por gerar todo o material de uma aula de 2 horas sobre **Transfer Learning** para alunos de graduação em Ciência de Dados da Engenharia de Produção da PUC‑Rio. O projeto deve seguir a abordagem "student’s perspective" do livro *Introduction to Transfer Learning: Algorithms and Practice* (Wang & Chen, 2023).

## Entregáveis a Produzir
1. **Plano da aula** – cronograma detalhado, divisão entre teoria e prática, tempo estimado para cada tópico.
2. **Roteiro teórico** – texto em estilo textbook (definições, motivação, algoritmos principais, diagramas) em Markdown.
3. **Slides** – arquivos Markdown (ou PDF) contendo os mesmos conceitos do roteiro, com visual agradável para projeção.
4. **Práticas de Transfer Learning** – 1 ou 2 notebooks ou scripts Python simples que:
   - Utilizem um modelo pré‑treinado (ex.: ResNet‑18, BERT) disponível em `torchvision` ou `transformers`.
   - Apliquem fine‑tuning em um dataset aberto pequeno (ex.: CIFAR‑10, AG News).
   - Possuam tempo de execução ≤ 10 min em CPU.
5. **Código pronto para VS Code** – estrutura em `src/` com instruções de execução (ex.: `python -m src.train`), comentários linha a linha e `requirements.txt`.
6. **Explicação do código** – documentação em Markdown dentro de `md/` descrevendo cada bloco, decisões de design e como rodar.
7. **Notas do professor** – dicas de condução da aula, perguntas a fazer, pontos de atenção.
8. **Checklist operacional** – lista de verificação para garantir que tudo funciona em sala (instalações, dados, runtime). 
9. **Referências** – citações completas do livro base e links para datasets e bibliotecas.
10. **Arquivos finais em Markdown** – todo o conteúdo produzido deve ser salvo como `.md` (exceto códigos Python que ficam em `src/`).

## Regras de Operação
- **Fases sequenciais**: Cada entregável só deve ser gerado após a validação da fase anterior.
- **Simplicidade**: Priorizar códigos curtos, bem comentados e que não exijam GPU.
- **Clareza Pedagógica**: Linguagem em português, termos técnicos em inglês quando indispensáveis; incluir exemplos ilustrativos.
- **Robustez**: Incluir tratamento de erros simples (ex.: download de datasets) e mensagens de progresso.
- **Consistência**: As práticas devem estar alinhadas ao roteiro teórico e ao plano da aula.
- **Tempo de Execução**: Garantir que cada notebook/script execute em ≤ 10 min em máquina padrão de laboratório.
- **Documentação**: Cada notebook deve conter célula de introdução, célula de código, célula de explicação; arquivos Markdown devem ter títulos claros (`#`, `##`).
- **Exportação**: Slides devem ser exportáveis para PDF via extensão VS Code ou `pandoc`.
- **Iteratividade**: O agente deve validar cada arquivo (ex.: existência, tamanho, sintaxe) antes de prosseguir.
- **Autonomia**: O agente pode chamar sub‑agentes ou ferramentas de busca para obter exemplos de código, mas deve citar a fonte.

## Orientações Específicas
- Use datasets públicos como `CIFAR‑10` (via `torchvision.datasets`) ou `AG News` (via `torchtext`).
- Utilize modelos pré‑treinados da biblioteca `torchvision` (ex.: `resnet18(pretrained=True)`) ou `transformers` (ex.: `distilbert-base-uncased`).
- Forneça instruções de instalação no README e no `md/installation.md`.
- Cada prática deve conter **Objetivo**, **Passos**, **Código**, **Resultado esperado** e **Tempo estimado**.
- Incluir comentários que expliquem a lógica do fine‑tuning e a escolha dos hiper‑parâmetros.
- Produzir um **Plano B** (ex.: usar dataset ainda menor ou um modelo mais leve) caso o tempo exceda.

> **Objetivo final**: entregar um repositório completo, pronto para ser clonado e usado em sala de aula, com material coerente, pedagogicamente sólido e tecnicamente executável.

### MATERIAL DE REFERÊNCIA DA PROFESSORA (OBRIGATÓRIO)

Localização dos arquivos:
  reference-slides-professora/

Arquivos disponíveis:
arquivos de slides que estiverem nesta pasta

Objetivo deste material:
Os slides da professora servem apenas como MOLDE VISUAL e PEDAGÓGICO para a sua apresentação.
Eles NÃO são a fonte principal de conceitos.

O que você DEVE fazer com este material:

1. Ler e analisar os slides da professora para extrair:
   - estilo visual (cores, fontes, layout, densidade de texto, uso de diagramas/imagens);
   - nível de formalismo e profundidade esperada;
   - padrão de organização dos tópicos (abertura, agenda, desenvolvimento, exemplos, fechamento);
   - convenções locais da disciplina (ex: como ela introduz conceitos, como fecha aulas).

2. Usar esse estilo como GUIA para criar seus próprios slides sobre Transfer Learning:
   - Recrie o conteúdo teórico COM BASE NO LIVRO de Wang & Chen (2023).
   - Adapte o ESTILO VISUAL e a ESTRUTURA DIDÁTICA ao padrão da professora.
   - Mantenha a mesma densidade de texto por slide, mesmo padrão de títulos/subtítulos,
     mesmo uso de boxes, diagramas e exemplos típicos.

3. Produzir o arquivo md/03_slides_aula.md com:
   - conteúdo completo de cada slide (título, subtítulo, bullets, notas do apresentador);
   - pelo menos 1 slide comparando: TL vs treinamento do zero vs fine-tuning vs domain adaptation;
   - pelo menos 1 slide sobre negative transfer;
   - pelo menos 1 slide com workflow visual "quando usar TL";
   - transições conceituais claras entre os tópicos.

O que você NÃO deve fazer:

- NÃO usar os slides da professora como fonte principal de conceitos.
- NÃO copiar trechos longos literalmente dos slides da professora.
- NÃO reutilizar exemplos específicos da professora sem adaptá-los ao contexto de Transfer Learning e ao nível da turma.
- NÃO gerar os slides finais em PPTX agora; apenas o conteúdo teórico em md/03_slides_aula.md.
- NÃO alterar o estilo visual para algo muito diferente do padrão da professora.

Regra de ouro (PRIORIDADE):

- Se houver conflito entre o livro de Wang & Chen e os slides da professora:
  • CONCEITOS, DEFINIÇÕES e FUNDAMENTAÇÃO teórica → seguem o livro de Wang & Chen (2023).
  • ESTILO VISUAL, ESTRUTURA DOS SLIDES e NÍVEL DE PROFUNDIDADE → seguem o padrão da professora.

Fluxo obrigatório:

1. Leia primeiro: README.md → prompts/00_system_context.md → prompts/02_acceptance_criteria.md.
2. Em seguida, analise os slides na pasta reference-slides-professora/.
3. Use os slides apenas para extrair o estilo visual e pedagógico.
4. Gere o conteúdo teórico com base no livro.
5. Produza md/03_slides_aula.md no estilo da professora, mas com conteúdo de Wang & Chen.