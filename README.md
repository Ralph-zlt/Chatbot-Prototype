# Chatbot-Prototype
This repository contains a strictly Rule-Based Chatbot prototype. The goal of this project is not to build an advanced language model, but to demonstrate in a simplified and didactic way how artificial intelligences process inputs, retrieve information (reasoning), and store new knowledge (learning).
How the Code Works Core Functions

 Basic Natural Language Processing (NLP): The limpar_e_processar function mimics what modern AIs do. Here, punctuation is removed, and the text is split into whole words. In modern Large Language Models (LLMs), this is handled by Tokenization, where words are broken down into sub-units (morphemes) so the AI can understand roots and prefixes (e.g., understanding that "illiterate" is "il-" meaning lack of + "literate").
    Reasoning and Search: The responder_senai function acts as our search algorithm. It checks if the user's input matches the keys in our database (Dictionary). In neural networks, this would be equivalent to vector mathematics and parallelism calculating context weights.
    Learning (State Mutation): When the machine lacks an answer, it enters a learning flow. It prompts for data, categorizes the information (new topic or sub-topic), and saves it to the dictionary at runtime.


Scalability and Layers
Currently, this model uses two layers of depth (Main Topic -> Sub-topic). However, this nested dictionary data structure could easily be expanded to infinite layers, serving as a rudimentary simulation of the "Hidden Layers" found in complex neural networks.
