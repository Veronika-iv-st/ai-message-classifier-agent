import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Configura el modelo para respuestas simples
modelo_simple = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.3,
)

# Función para cargar el prompt desde archivo
def cargar_prompt(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

# Cargar prompt desde prompts/respuesta_simple.txt
prompt_path = os.path.join("prompts", "respuesta_simple.txt")
prompt_respuesta_simple = ChatPromptTemplate.from_template(cargar_prompt(prompt_path))

# Cadena de ejecución de respuesta
cadena_respuesta = (
    prompt_respuesta_simple
    | modelo_simple
    | StrOutputParser()
)

# Acción 1: responder automáticamente usando el conocimiento base
def responder_automaticamente(mensaje: str) -> str:
    return cadena_respuesta.invoke({"mensaje": mensaje}).strip()

# Acción 2: transferir a humano
def transferir_a_humano(mensaje: str) -> str:
    return "Voy a derivarte con uno de nuestros consultores. Un momento, por favor..."
