# 🛠️ Ferramentas e Metodologia Utilizadas

## Ferramentas de desenvolvimento

| Ferramenta | Versão / Detalhes | Para que foi usada |
|------------|-------------------|--------------------|
| **Python** | 3.11 (CPython, Windows) | Scripts de treinamento e extração de PDFs |
| **PyTorch** | Instalado via pip | Framework de deep learning para feature extraction |
| **torchvision** | Instalado via pip | Dataset CIFAR-10, transforms, modelos pré-treinados (ResNet-18) |
| **pdfplumber** | Instalado via pip --user | Extração de texto dos PDFs da professora para análise de conteúdo |
| **scikit-learn** | Via requirements.txt | Métricas de avaliação (previsto para práticas futuras) |
| **jupyter / ipykernel** | Via requirements.txt | Execução interativa dos notebooks |
| **Git** | Sistema local | Controle de versão com commits semânticos (`feat:`, `docs:`, `fix:`) |
| **HTML5 + CSS3 + JS** | Vanilla (sem frameworks) | Apresentação de slides (`transfer_learning_aula.html`) |
| **Reveal.js** (tentativa) | CDN 4.5.0 | Tentativa inicial de slides — substituído por HTML/CSS/JS próprio |
| **Google Fonts / Inter** | CDN | Tipografia dos slides |
| **JetBrains Mono** | CDN | Fonte monospace para blocos de código nos slides |

---

## Metodologia de criação dos slides

### O que NÃO funcionou (iterações anteriores)
1. **Slide 1 (tentativa):** Markdown puro — não é uma apresentação real, não tem navegação nem visual
2. **Slide 2 (tentativa):** HTML com Reveal.js — conteúdo superficial (apenas bullet points copiados do markdown), visual genérico
3. **Slide 3 (tentativa):** Mesma coisa com pequenas variações de CSS — não houve leitura real do material da professora

### O que funcionou (versão final)
1. **Ler os PDFs reais** com `pdfplumber` — identificar o contexto real da turma, o estilo da professora, os conceitos já conhecidos pelos alunos
2. **Mapear o conteúdo** aos slides existentes da disciplina (ICD-02, ICD-04)
3. **Escrever HTML/CSS/JS do zero** sem dependências externas — controle total sobre design e interatividade
4. **Incluir conteúdo denso e real**: métricas reais do ResNet-18, tabela comparativa baseada no livro, código com syntax highlighting manual, perguntas contextualizadas para Engenharia de Produção

---

## Decisões de design dos slides

| Decisão | Motivo |
|---------|--------|
| Dark mode (fundo `#0d1117`) | Leitura mais confortável em projetores; estilo moderno e premium |
| Tipografia Inter | Moderna, legível em tamanhos pequenos, usada por GitHub e Figma |
| Sem Reveal.js na versão final | Mais controle, sem dependência de CDN externo, arquivo único autocontido |
| Cards com bordas coloridas | Diferenciação visual rápida de conceitos (azul=teoria, verde=positivo, laranja=cuidado) |
| Syntax highlighting manual (HTML `<span>`) | Funciona offline, sem biblioteca JS extra, cores calibradas para o tema dark |
| Barra de progresso no topo | Feedback visual de quanto da apresentação foi coberto |
| Navegação por teclado (←→) | Padrão de apresentações; permite uso sem mouse durante a aula |

---

## Estrutura de commits Git

```
feat: finalize phase 2 artifacts     ← notebooks, src, slides, docs
docs: add session log and tools doc  ← esta sessão
```

---

## Referências bibliográficas usadas

- Wang, Y., & Chen, X. (2023). *Introduction to Transfer Learning: Algorithms and Practice*. Springer.
- He, K., Zhang, X., Ren, S., & Sun, J. (2016). *Deep Residual Learning for Image Recognition*. CVPR.
- Material da professora: ICD-00 a ICD-04, PlanoDeAula_ICD_25-2.pdf — Celecia, Veiga, Baião, Happ. PUC-Rio ENG4502.
- PyTorch Documentation: https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html
