from dotenv import load_dotenv
from decision import clasificar_mensaje
from tools import responder_automaticamente, transferir_a_humano

def ejecutar_agente():
    load_dotenv()
    mensaje = input("Escribe tu mensaje:")
    clasificacion = clasificar_mensaje(mensaje)
    print (f"ªn Clasificacion : {clasificacion}")

    if clasificacion == "SIMPLE":
        respuesta = responder_automaticamente(mensaje)
    elif clasificacion == "COMPLEJA":
        respuesta = transferir_a_humano(mensaje)
    else:
        respuesta = "No se pudo clasificar el mensaje"

    print(f"\n Respuesta del agente {respuesta}")

if __name__ == "__main__":
    ejecutar_agente()
