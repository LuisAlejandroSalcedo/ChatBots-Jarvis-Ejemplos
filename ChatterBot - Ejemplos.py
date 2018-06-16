
# coding: utf-8

# In[1]:


from chatterbot import ChatBot # Importamos la clase ChatBot

# Creamos una instancia de ChatBot para la creación de un Bot.
# Le pasamos como arcumneto el nombre que le daremos al Bot: "PythonBot"
# Y los datos que se utilizaran para entrenar al Bot
chatbot = ChatBot(
    'PythonBot',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Entrenamos al Bot
chatbot.train("chatterbot.corpus.english")

# Respuesta para "Hello, how are you?"
chatbot.get_response("Hello, how are you?")


# In[2]:


chatbot.get_response("Dollar")


# In[3]:


from chatterbot import ChatBot

# Creamos a jarvis y definimos sus caracteristicas
bot = ChatBot(
    "jarvis",
    logic_adapters=[ # Importamos los adaptadores
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter"
    ],
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter"
)

# Le preguntamos a Jarvis cuanto es 30 * 4
response = bot.get_response("What is 30 * 4?")
print(response) # mostramos la respuesta de Jarvis

# Le preguntamos a jarvis ¿que hora es?
response = bot.get_response("What time is it?")
print(response) # Mostramos la respuesta de jarvis


# In[4]:


from chatterbot import ChatBot

# Creamos una instancia de jarvis
bot = ChatBot(
    'jarvis',
    storage_adapter='chatterbot.storage.SQLStorageAdapter', # Importamos el adaptador de almacenamiento
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch' # importaos el adaptador para las respuestas
        },
        {
            'import_path': 'chatterbot.logic.SpecificResponseAdapter', # Adaptador para respuestas especificas
            'input_text': 'Quien eres?', # Entrada del usuario
            'output_text': 'Mi nombre es Jarvis, estoy para servirle' # Respuesta de jarvis
        }
    ],
    trainer='chatterbot.trainers.ListTrainer' # Entrenamos al bot
)

# Preguntamos al Bot ¿Quien eres?
response = bot.get_response('Quien eres?')
print(response) # Mostramos la respuesta

