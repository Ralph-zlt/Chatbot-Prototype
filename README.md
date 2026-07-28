*🇧🇷 [Leia este documento em Português](README.pt-br.md)*

# Chatbot-Prototype Understanding AI Fundamentals

This repository contains a strictly Rule-Based Chatbot prototype. The goal of this project is not to build an advanced language model, but to demonstrate in a simplified and didactic way how artificial intelligences process inputs, retrieve information (reasoning), and store new knowledge (learning).

### How the Code Works: Core Functions
* **The function of base_conhecimento is to act as a Python dictionary, equivalent to the database of modern AIs. In it, the AI retrieves the information it needs to search, read, and determine how to respond.
* **Basic Natural Language Processing (NLP):** The `limpar_e_processar` function mimics what modern AIs do. Here, punctuation is removed, **accents are stripped to standardize inputs (allowing the bot to recognize words regardless of whether the user types them with or without accent marks)**, and the text is split into whole words. In modern Large Language Models (LLMs), this is handled by Tokenization, where words are broken down into sub-units (morphemes) so the AI can understand roots and prefixes (e.g., understanding that "illiterate" is "il-" meaning lack of + "literate").
* **Reasoning and Search:** The `buscar_resposta` function acts as our search algorithm. It checks if the user's input matches the keys in our database (Dictionary). In neural networks, this would be equivalent to vector mathematics and parallelism calculating context weights.
* **Learning (State Mutation):** When the machine lacks an answer, it enters a learning flow. It prompts for data, categorizes the information (new topic or sub-topic), and saves it to the dictionary at runtime.

### Scalability and Layers

Currently, this model uses two layers of depth (Main Topic -> Sub-topic). However, this nested dictionary data structure could easily be expanded to infinite layers, serving as a rudimentary simulation of the "Hidden Layers" found in complex neural networks.
