# Nome do Projeto: Gerenciador de Tarefas
Chatbot Baseado em Regras (Rule-Based System)

Este repositório contém um protótipo de **Chatbot Baseado em Regras (Rule-Based System)**. O objetivo deste projeto não é criar um modelo de linguagem avançado, mas sim demonstrar, de forma simplificada e didática, como as inteligências artificiais processam entradas, buscam informações (raciocínio) e armazenam novos conhecimentos (aprendizado).

---

 Como o código funciona (Funções Principais)

 🧠 Processamento de Linguagem Natural (NLP) Básico

A função `limpar_e_processar` simula, de forma simplificada, o processamento inicial realizado por sistemas de IA.

Ela executa tarefas como:
- Remoção de pontuações;
- Normalização do texto;
- Separação da frase em palavras.

Nos **Large Language Models (LLMs)** modernos, esse processo é realizado por meio da **Tokenização**, em que palavras são divididas em subunidades (*tokens*), permitindo que o modelo compreenda raízes, prefixos e sufixos.

**Exemplo:**


analfabeto
↓
an + alfabeto


Onde:
 an- → indica ausência ou negação;
alfabeto → conjunto de letras.

Esse método permite que modelos entendam palavras desconhecidas analisando sua estrutura.

---

### 🔎 Raciocínio e Busca

A função responder_senai representa o mecanismo de busca do chatbot.

Seu funcionamento consiste em:

1. Receber a entrada do usuário;
2. Comparar as palavras com as chaves do banco de dados (um **Dicionário** do Python);
3. Retornar a resposta correspondente quando houver uma correspondência.

Em modelos baseados em redes neurais, esse comportamento seria equivalente aos cálculos realizados sobre **vetores de contexto**, utilizando **pesos** e operações paralelas para estimar a resposta mais provável.

---

### 📚 Aprendizado (State Mutation)

Quando o chatbot não encontra uma resposta para determinada pergunta, ele inicia um processo simples de aprendizado.

Esse fluxo consiste em:

1. Solicitar a resposta ao usuário;
2. Identificar se a informação corresponde a:
   - um novo assunto;
   - ou uma nova resposta para um assunto existente;
3. Armazenar essa informação no dicionário durante a execução do programa.

Esse processo representa uma **mutação de estado (State Mutation)**, pois o estado interno do chatbot é modificado dinamicamente conforme novos conhecimentos são adicionados.

> **Observação:** Neste projeto, o aprendizado ocorre apenas em tempo de execução. As informações não são persistidas em banco de dados ou arquivo permanente, sendo perdidas quando o programa é encerrado.

---

## Objetivo do Projeto

Este projeto possui caráter **educacional** e tem como finalidade demonstrar conceitos fundamentais utilizados em sistemas de inteligência artificial, como:

- Processamento de linguagem natural (NLP);
- Busca baseada em regras;
- Estruturas de dados para armazenamento de conhecimento;
- Aprendizado por atualização de estado (*State Mutation*);
- Diferenças entre sistemas baseados em regras e modelos modernos de IA (LLMs).

Embora simplificado, o projeto ajuda a compreender os princípios básicos que inspiram sistemas de IA mais avançados.
