base_conhecimento = {
    "hello": {
        "resposta": "Hello! How can I help you today?",
        "sub": {}
    },
    "hi": {
        "resposta": "Hi there! What do you need help with?",
        "sub": {}
    },
    "historia": {
        "resposta": "Historia é a ciência humana sobre os acontecimentos passados.",
        "sub": {}
    },
    "ciencia": {
        "resposta": "A maior de todas as ciências é a filosofia, um conhecimento certo e demonstrativo das coisas por suas causas primeiras.",
        "sub": {}
    },
    "filosofia": {
        "resposta": "A maior de todas as ciências é a filosofia...",
        "sub": {}
    },
    "teologia": {
        "resposta": "É uma ciência sagrada que deriva da revelação divina e tem Deus como seu objeto principal.",
        "sub": {}
    },
    "etica": {
        "resposta": "A Ética aristotélica busca a eudaimonia através da prática das virtudes.",
        "sub": {}
    },
    "matematica": {
        "resposta": "A Matemática é a ciência das relações quantitativas e espaciais.",
        "sub": {}
    },
    "logica": {
        "resposta": "A Lógica é o estudo do raciocínio e da argumentação válida.",
        "sub": {}
    },
    "portugues": {
        "resposta": "A Língua Portuguesa é o idioma oficial do Brasil, um sistema complexo de comunicação.",
        "sub": {}
    },
    "cursos": {
        "resposta": "Temos diversos cursos técnicos e profissionalizantes disponíveis.",
        "sub": {}
    },
    "ajuda": {
        "resposta": "Eu posso te ajudar com dúvidas sobre diversas áreas do conhecimento!",
        "sub": {}
    }
}

def limpar_e_processar(frase):
    pontuacoes = [",", ".", "!", "?", "..."]
    for p in pontuacoes:
        frase = frase.replace(p, " ")
        
    frase = frase.lower()
    
    # Remove acentos básicos da entrada do usuário
    mapa_acentos = {
        "á": "a", "à": "a", "ã": "a", "â": "a",
        "é": "e", "ê": "e",
        "í": "i",
        "ó": "o", "õ": "o", "ô": "o",
        "ú": "u",
        "ç": "c"
    }
    for com_acento, sem_acento in mapa_acentos.items():
        frase = frase.replace(com_acento, sem_acento)
        
    tokens = frase.split()
    return tokens

def buscar_resposta(tokens, contexto_atual):
    if contexto_atual and contexto_atual in base_conhecimento:
        sub_dicionario = base_conhecimento[contexto_atual]["sub"]
        for sub_chave, sub_resposta in sub_dicionario.items():
            if sub_chave in tokens:
                return sub_resposta, None

    for chave, dados in base_conhecimento.items():
        if chave in tokens:
            return dados["resposta"], chave

    return None, contexto_atual

def iniciar_chatbot():
    print("Assistente virtual iniciado.")
    print("Digite 'sair' a qualquer momento para encerrar.\n")

    contexto_atual = None

    while True:
        entrada_usuario = input("Você: ")

        if "sair" in entrada_usuario.lower():
            print("Bot: Até logo!")
            break

        tokens_usuario = limpar_e_processar(entrada_usuario)
        resposta_bot, novo_contexto = buscar_resposta(tokens_usuario, contexto_atual)

        contexto_atual = novo_contexto

        if resposta_bot:
            print(f"Bot: {resposta_bot}\n")
        else:
            e_do_contexto = "n"
            
            if contexto_atual:
                print(f"Bot: Não entendi. Sua dúvida é sobre '{contexto_atual}'? (s/n)")
                e_do_contexto = input("Sua resposta: ").lower().strip()

            if e_do_contexto == "s":
                nova_sub_chave = input(f"Qual a palavra-chave específica dentro de '{contexto_atual}'?: ").lower().strip()
                nova_sub_resposta = input(f"Digite a resposta esperada para '{nova_sub_chave}': ")

                base_conhecimento[contexto_atual]["sub"][nova_sub_chave] = nova_sub_resposta
                print(f"Bot: Aprendido! Agora já sei responder sobre '{nova_sub_chave}' dentro do assunto '{contexto_atual}'.\n")

            else:
                contexto_atual = None

                print("Bot: Não entendi. Por favor, resuma seu NOVO assunto em apenas uma palavra:")
                nova_chave = input("Sua palavra-chave: ").lower().strip()
                
                # Garante que a nova palavra também será salva sem acentos
                tokens_nova_chave = limpar_e_processar(nova_chave)
                if tokens_nova_chave:
                    nova_chave = tokens_nova_chave[0]
                
                nova_resposta = input(f"Agora, digite a resposta que você esperava para '{nova_chave}': ")

                base_conhecimento[nova_chave] = {
                    "resposta": nova_resposta,
                    "sub": {}
                }
                print("Bot: Aprendido! Agora já sei responder sobre esse novo assunto.\n")

iniciar_chatbot()
