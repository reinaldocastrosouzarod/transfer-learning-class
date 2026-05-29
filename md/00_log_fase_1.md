# Log da Fase 1 – Scaffolding

## Descrição detalhada das atividades
1. **Criação da estrutura de diretórios** conforme especificado:
   - `.vscode/`, `data/`, `notebooks/`, `src/`, `slides/`, `md/`, `outputs/`, `prompts/`.
2. **Geração dos arquivos base**:
   - `README.md` – objetivo, contexto, estrutura, restrições, workflow.
   - `requirements.txt` – bibliotecas essenciais (numpy, pandas, matplotlib, scikit-learn, jupyter, ipykernel, torch, torchvision).
   - `.gitignore` – regras para ignorar ambientes virtuais, caches, outputs e dados.
3. **Produção dos prompts de contexto e master** (`00_system_context.md`, `01_master_prompt.md`, `02_acceptance_criteria.md`).
4. **Registro dos prompts da fase**:
   - `03_prompt_fase_1_scaffolding.md` – prompt original usado para criar a fundação.
   - `04_prompt_fase_2_teoria_slides.md` – prompt preparado para a próxima fase (não executado).
5. **Documentação de estado**:
   - `md/00_status_projeto_ate_agora.md` – resumo executivo, arquivos existentes, pendências e roadmap.
6. **Versãoção Git**:
   - Inicializado repositório (`git init`).
   - Adicionados todos os arquivos acima ao índice.
   - Commit realizado com a mensagem `chore: salvar fundação do projeto e documentação da fase 1`.

## Decisões tomadas
- **Simplicidade**: optamos por um conjunto enxuto de dependências e por arquivos de configuração básicos.
- **Portabilidade**: a estrutura foi pensada para rodar em VS Code em máquinas típicas de laboratório (CPU, 8 GB RAM).
- **Documentação**: todos os prompts e status foram salvos em Markdown para fácil leitura e versionamento.

## Restrições assumidas
- Código a ser desenvolvido nas fases seguintes deve permanecer simples, executável em < 10 min.
- Datasets devem ser pequenos e de domínio público.
- Todo material final será entregue em arquivos Markdown.

## Observações importantes para continuidade
- Os diretórios `data/`, `outputs/` e `.venv/` estão listados no `.gitignore` e **não** foram adicionados ao commit.
- As pastas `md/` e `prompts/` contêm a documentação que será referenciada nas próximas fases.
- Não há nenhum remote configurado ainda; será necessário acrescentar um origin antes de fazer push.

## Riscos conhecidos nesta etapa
- **Ambiente de desenvolvimento**: se o usuário não possuir VS Code ou Python 3.10+, será necessário instalar manualmente.
- **Remote Git**: a falta de um remote impede o push automático; será necessário configurá‑lo antes da sincronização.
- **Dependências futuras**: bibliotecas adicionais podem ser necessárias nas fases de prática; será preciso atualizar `requirements.txt` posteriormente.
