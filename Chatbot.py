base_conhecimento = {
    # --- SAUDAÇÕES / GREETINGS ---
    "oi": {
        "resposta": "Olá! Como posso te ajudar hoje?",
        "sub": {
            "tudo": "Tudo ótimo! Estou pronto para responder suas dúvidas."
        }
    },
    "hello": {
        "resposta": "Hello! How can I help you today?",
        "sub": {
            "how": "I'm doing great, ready to learn and answer your questions!"
        }
    },
    "hi": {
        "resposta": "Hi there! What do you need help with?",
        "sub": {
            "how": "I'm doing great, ready to learn and answer your questions!"
        }
    },
    
    # --- HISTÓRIA / HISTORY ---
    "historia": {
        "resposta": "História é a ciência humana sobre os acontecimentos passados.",
        "sub": {
            "brasil": "Conhecida inicialmente como Terra de Santa Cruz (uma terra abençoada), teve sua primeira missa celebrada no ano de 1500."
        }
    },
    "history": {
        "resposta": "History is the human science about past events.",
        "sub": {
            "brazil": "Initially known as the Land of Holy Cross (a blessed land), it had its first mass celebrated in the year 1500."
        }
    },

    # --- CIÊNCIA / SCIENCE ---
    "ciencia": {
        "resposta": "A maior de todas as ciências é a filosofia, um conhecimento certo e demonstrativo das coisas por suas causas primeiras.",
        "sub": {
            "metodo": "O método científico é baseado na observação, formulação de hipóteses, experimentação e conclusão."
        }
    },
    "science": {
        "resposta": "The greatest of all sciences is philosophy, a certain and demonstrative knowledge of things by their first causes.",
        "sub": {
            "method": "The scientific method is based on observation, hypothesis formulation, experimentation, and conclusion."
        }
    },

    # --- FILOSOFIA / PHILOSOPHY ---
    "filosofia": {
        "resposta": "A maior de todas as ciências é a filosofia, a busca pela sabedoria e pelas causas primeiras.",
        "sub": {
            "socrates": "Sócrates foi um dos maiores filósofos gregos, famoso pela máxima: 'Só sei que nada sei'."
        }
    },
    "philosophy": {
        "resposta": "The greatest of all sciences is philosophy, the search for wisdom and first causes.",
        "sub": {
            "socrates": "Socrates was one of the greatest Greek philosophers, famous for the maxim: 'I know that I know nothing'."
        }
    },

    # --- TEOLOGIA / THEOLOGY ---
    "teologia": {
        "resposta": "É uma ciência sagrada, a maior de todas as ciências pois deriva da revelação divina e tem Deus como seu objeto principal.",
        "sub": {
            "tomas": "São Tomás de Aquino foi um de seus maiores expoentes, responsável por unir a fé cristã à razão aristotélica."
        }
    },
    "theology": {
        "resposta": "It is a sacred science, the greatest of all sciences because it derives from divine revelation and has God as its main object.",
        "sub": {
            "thomas": "Saint Thomas Aquinas was one of its greatest exponents, responsible for uniting Christian faith with Aristotelian reason."
        }
    },

    # --- ÉTICA / ETHICS ---
    "etica": {
        "resposta": "A Ética aristotélica busca a eudaimonia (felicidade) através da prática das virtudes.",
        "sub": {
            "virtude": "Para Aristóteles, a virtude é o justo meio (equilíbrio) entre dois extremos: um vício por falta e outro por excesso."
        }
    },
    "ethics": {
        "resposta": "Aristotelian Ethics seeks eudaimonia (happiness) through the practice of virtues.",
        "sub": {
            "virtue": "For Aristotle, virtue is the golden mean (balance) between two extremes: a vice of deficiency and a vice of excess."
        }
    },

    # --- MATEMÁTICA / MATH ---
    "matematica": {
        "resposta": "A Matemática é a ciência das relações quantitativas e espaciais.",
        "sub": {
            "geometria": "A geometria é a área que estuda as formas, tamanhos e posições no espaço, desde pontos até sólidos em 3D."
        }
    },
    "math": {
        "resposta": "Mathematics is the science of quantitative and spatial relations.",
        "sub": {
            "geometry": "Geometry is the branch that studies shapes, sizes, and positions in space, from points to 3D solids."
        }
    },

    # --- LÓGICA / LOGIC ---
    "logica": {
        "resposta": "A Lógica é o estudo do raciocínio e da argumentação válida.",
        "sub": {
            "silogismo": "O silogismo é uma estrutura clássica de dedução formada por duas premissas que levam a uma conclusão lógica."
        }
    },
    "logic": {
        "resposta": "Logic is the study of reasoning and valid argumentation.",
        "sub": {
            "syllogism": "A syllogism is a classic structure of deduction formed by two premises that lead to a logical conclusion."
        }
    },

    # --- PORTUGUÊS / PORTUGUESE ---
    "portugues": {
        "resposta": "A Língua Portuguesa é o idioma oficial do Brasil, um sistema complexo de comunicação.",
        "sub": {
            "gramatica": "A gramática normativa dita as regras da língua e se divide em fonologia, morfologia e sintaxe."
        }
    },
    "portuguese": {
        "resposta": "The Portuguese language is the official language of Brazil, a complex system of communication.",
        "sub": {
            "grammar": "Normative grammar dictates the rules of the language and is divided into phonology, morphology, and syntax."
        }
    },

    # --- AJUDA / HELP ---
    "ajuda": {
        "resposta": "Eu posso te ajudar com dúvidas sobre diversas áreas do conhecimento!",
        "sub": {
            "assuntos": "Você pode me perguntar sobre história, matemática, teologia, ciência, lógica e muito mais."
        }
    },
    "help": {
        "resposta": "I can help you with questions about various areas of knowledge!",
        "sub": {
            "topics": "You can ask me about history, math, theology, science, logic, and much more."
        }
    }
}
def limpar_e_processar(frase):
    pontuacoes = [",", ".", "!", "?", "..."]
    for p in pontuacoes:
        frase = frase.replace(p, " ")
        
    frase = frase.lower()
    
    # Remove acentos da entrada do usuário
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
                
                # Garante que a nova palavra também será salva limpa/sem acentos
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
