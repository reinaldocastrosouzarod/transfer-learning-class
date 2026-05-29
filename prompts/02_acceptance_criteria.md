# Critérios de Aceite

## Arquivos Obrigatórios
- `README.md` com objetivo, contexto, estrutura e workflow.
- Diretório `prompts/` contendo os três arquivos:
  - `00_system_context.md`
  - `01_master_prompt.md`
  - `02_acceptance_criteria.md`
- `requirements.txt` com dependências mínimas.
- `.gitignore` configurado.
- Estrutura de pastas completa conforme especificado.

## Qualidade Pedagógica
- Texto em português claro e objetivo.
- Conceitos explicados de forma didática, seguindo a perspectiva do estudante do livro.
- Exemplos ilustrativos e diagramas (se houver) adequados ao nível de graduação.

## Clareza do Código
- Código Python legível, comentado linha a linha.
- Nomeação de variáveis e funções em snake_case.
- Comentários explicando lógica de fine‑tuning e escolhas de hiper‑parâmetros.

## Datasets Abertos
- Utilizar apenas datasets públicos (ex.: CIFAR‑10, AG News) que podem ser baixados via `torchvision` ou `torchtext`.
- Tamanho < 100 MB para garantir download rápido.

## Tempo de Execução
- Cada prática (notebook ou script) deve concluir em **≤ 10 min** em máquina padrão de laboratório (CPU, 8 GB RAM).
- Preferencialmente **≤ 5 min**.

## Coerência Teoria ↔ Prática
- Cada exercício prático deve refletir diretamente um tópico abordado na parte teórica.
- O roteiro teórico deve mencionar explicitamente as práticas que serão realizadas.

## Explicações do Código
- Cada bloco de código tem uma célula ou seção de explicação em Markdown.
- As explicações descrevem entrada, processo, saída e motivos das escolhas.

## Plano B (Contingência)
- Caso o tempo de execução ultrapasse o limite, o agente deve providenciar alternativa:
  - Modelo mais leve (ex.: `MobileNetV2` ao invés de `ResNet18`).
  - Subconjunto ainda menor do dataset.
  - Redução de número de epochs.

## Checklist de Execução em Sala
- [ ] Ambiente virtual criado (`python -m venv .venv`).
- [ ] Dependências instaladas (`pip install -r requirements.txt`).
- [ ] Datasets baixados sem erros.
- [ ] Notebook ou script executado sem falhas.
- [ ] Slides renderizados corretamente.
- [ ] Tempo de prática medido e dentro do limite.
- [ ] Plano B testado.

## Avaliação Final
- Se todos os itens acima forem atendidos, o projeto é considerado **pronto para uso** na aula.
