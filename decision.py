from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableMap
from langchain_core.output_parsers import StrOutputParser
import os 

modelo = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)

def cargar_prompt(path: str) -> str:
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
    
prompt_path = os.path.join("prompts", "clasificacion.txt")
prompt_template = ChatPromptTemplate.from_template(cargar_prompt(prompt_path))

cadena_clasificacion = (
    prompt_template
    | modelo
    | StrOutputParser()
)
    
def clasificar_mensaje(mensaje: str) -> str:
    flujo = RunnableMap({
        "mensaje": lambda _: mensaje
    })
    resultado = cadena_clasificacion.invoke(flujo.invoke({}))
    return resultado.strip().upper()




