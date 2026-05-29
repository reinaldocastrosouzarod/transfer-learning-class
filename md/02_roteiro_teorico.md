# Roteiro Teórico (1 h) – Estilo Textbook

## 1. Introdução (5 min)
- **Motivação**: Por que reutilizar conhecimento de um modelo treinado em um domínio A para resolver tarefa em domínio B? 
- **Exemplo cotidiano**: Reconhecimento de gatos em fotos tiradas com diferentes câmeras.
- **Pergunta ao aluno**: "Se treinássemos do zero, quanto tempo levaria?"

> *Inspirado nos conceitos introdutórios de Wang & Chen (2023, Cap. 1).* 

## 2. Definição Formal (10 min)
- **Domínio** \(\mathcal{D}=\{\mathcal{X}, P(X)\}\): conjunto de dados e sua distribuição.
- **Tarefa** \(\mathcal{T}=\{\mathcal{Y}, f(·)\}\): espaço de rótulos e função objetivo.
- **Transfer Learning**: usar \(\mathcal{D}_S,\mathcal{T}_S\) (fonte) para melhorar \(\mathcal{D}_T,\mathcal{T}_T\) (alvo).
- **Intuição antes da formalização**: mostrar um diagrama simples de duas bolhas (fonte e alvo) com setas de transferência.

> *Definição formal retirada de Wang & Chen (2023, Sec. 2.1).* 

## 3. Taxonomia Básica (12 min)
| Tipo | Característica | Exemplo |
|------|----------------|---------|
| **Homogêneo** | \(\mathcal{X}_S = \mathcal{X}_T\) (mesmo tipo de dados) | Imagens RGB → Imagens RGB |
| **Heterogêneo** | Diferentes tipos de dados | Texto → Imagens |
| **Instance‑based** | Re‑pesagem de instâncias | k‑NN com amostras de fonte |
| **Feature‑based** | Aprender representação compartilhada | CNN pré‑treinada |
| **Model‑based** | Ajustar parâmetros de modelo | Fine‑tuning de rede profunda |

**Mini‑checkpoint**: Perguntar “Qual categoria se aplica quando usamos embeddings de BERT para análise de sentimentos?”

> *Tabela inspirada em Wang & Chen (2023, Tab. 2.1).* 

## 4. Estratégias de TL (15 min)
1. **Fine‑tuning** – congelar camadas base, treinar últimas.
2. **Domain Adaptation** – alinhar distribuições \(P_S(X)\) e \(P_T(X)\).
3. **Domain Generalization** – treinar modelo que generaliza para domínios não vistos, usando múltiplas fontes.
4. **Meta‑learning** – aprender a aprender; métodos como MAML que produzem inicializações rápidas para novas tarefas.

- **Quando usar?**: Apresentar um fluxograma de decisão (ver slide 03).
- **Armadías comuns**: Sobre‑ajuste ao pequeno conjunto alvo, escolha de camadas a congelar, risco de *negative transfer*.

## 5. Negative Transfer (8 min)
- **Definição**: Quando a transferência reduz a performance em \(\mathcal{T}_T\).
- **Causas típicas**: Domínio muito distante, rótulos incompatíveis, modelo fonte pobre.
- **Exemplo simples**: Treinar modelo de reconhecimento de dígitos MNIST e aplicar a imagens de radiografias.
- **Como detectar**: Validar no conjunto alvo antes de adotar TL.

> *Conceito descrito em Wang & Chen (2023, Sec. 3.4).* 

## 6. Resumo e Perguntas (5 min)
- Recapitular definições, taxonomia e armadilhas.
- Checklist “Quando usar TL?” (ver slide 04).
- Espaço aberto para dúvidas.

---

*Todo o conteúdo foi reescrito em linguagem didática, mantendo a fidelidade ao livro de Wang & Chen (2023).*
