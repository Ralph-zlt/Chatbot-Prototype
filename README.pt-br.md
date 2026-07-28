*🇺🇸 [Read this document in English](README.md)*

# Chatbot-Prototype: Entendendo os Fundamentos da IA

Este repositório contém um protótipo de Chatbot estritamente Baseado em Regras. O objetivo deste projeto não é construir um modelo de linguagem avançado, mas demonstrar de forma simplificada e didática como as inteligências artificiais processam entradas, recuperam informações (raciocínio) e armazenam novos conhecimentos (aprendizado).

### Como o Código Funciona: Funções Principais

 * **   A função da base_conhecimento é atuar como um dicionário em Python, equivalente à base de dados das IAs modernas. Nela, a IA consulta as informações que precisa buscar, ler e definir como responder.
* **Processamento Básico de Linguagem Natural (NLP):** A função `limpar_e_processar` imita o que as IAs modernas fazem. Aqui, a pontuação é removida, **os acentos são retirados para padronizar as entradas (permitindo que o bot reconheça as palavras independentemente de o usuário digitá-las com ou sem acentuação)**, e o texto é dividido em palavras inteiras. Nos Grandes Modelos de Linguagem (LLMs) modernos, isso é tratado pela Tokenização, onde as palavras são divididas em subunidades (morfemas) para que a IA possa entender raízes e prefixos (ex: entender que "iletrado" é "i-" indicando negação/falta de + "letrado").
* **Raciocínio e Busca:** A função buscar_resposta atua como nosso algoritmo de busca. Ela verifica se a entrada do usuário corresponde às chaves em nosso banco de dados (Dicionário). Em redes neurais, isso seria equivalente à matemática vetorial e ao paralelismo calculando os pesos de contexto.
* **Aprendizado (Mutação de Estado):** Quando a máquina não possui uma resposta, ela entra em um fluxo de aprendizado. Ela solicita dados, categoriza a informação (novo tópico ou subtópico) e a salva no dicionário em tempo de execução (runtime).

### Escalabilidade e Camadas

Atualmente, este modelo usa duas camadas de profundidade (Tópico Principal -> Subtópico). No entanto, essa estrutura de dados em dicionários aninhados poderia facilmente ser expandida para camadas infinitas, servindo como uma simulação rudimentar das "Camadas Ocultas" (Hidden Layers) encontradas em redes neurais complexas.
