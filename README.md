# 🤖 Agente de Transferencia Inteligente con LangChain 0.3+

Este proyecto implementa un agente inteligente que analiza mensajes entrantes y decide si puede responder automáticamente (casos simples) o si debe transferir la conversación a un humano (casos complejos). Es ideal para empresas que desean mejorar su atención al cliente, reducir carga operativa y ofrecer un primer filtro con IA confiable.

---

## 🧠 ¿Qué hace este agente?

1. **Clasifica** la intención del usuario como `SIMPLE` o `COMPLEJA`.
2. Si es `SIMPLE`, responde directamente con información basada en el negocio.
3. Si es `COMPLEJA`, simula una transferencia a un humano.
4. Usa solo información segura y predefinida, sin inventar.

---

## 📁 Estructura del proyecto
1_agente_transferencia/
├── main.py # Punto de entrada. Orquesta el flujo completo.
├── decision.py # Clasifica el mensaje (SIMPLE o COMPLEJA) usando un modelo LLM.
├── tools.py # Ejecuta la acción adecuada: responder o transferir.
├── prompts/
│ ├── clasificacion.txt # Prompt usado para determinar la intención del mensaje.
│ └── respuesta_simple.txt # Prompt que contiene el contexto empresarial para respuestas automáticas.
├── .env # Archivo con la API key de OpenAI.
└── README.md # Documentación completa del proyecto.



---

## ⚙️ Requisitos

- Python 3.10+
- Un entorno virtual (recomendado)
- Clave API de OpenAI

### Instalación de dependencias

pip install langchain-core langchain-openai python-dotenv

🔐 Configuración
Crea un archivo .env en la raíz del proyecto:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxx
Verifica que esté en el mismo directorio desde donde ejecutarás main.py.

🚀 Cómo usar el agente
Desde consola, ejecuta:
python main.py

Te pedirá que escribas un mensaje. El flujo:

Clasifica el mensaje.

Ejecuta la herramienta correspondiente.

Devuelve la respuesta por pantalla.



🧩 Cómo adaptarlo a cualquier empresa
1. Personaliza el conocimiento base
Edita el archivo:
prompts/respuesta_simple.txt

Y reemplaza el bloque de contexto con la información de tu empresa:

Qué hacéis

Qué ofrecéis

Para quién trabajáis

Tecnologías utilizadas

Política de privacidad o zonas geográficas

Canales de contacto

2. Cambia el estilo de respuesta
Puedes modificar el prompt para:

Usar tono más formal o más cercano

Dar respuestas más técnicas o más comerciales

Adaptar el idioma

3. Añadir idiomas adicionales
Puedes detectar el idioma en main.py o extender el clasificador para redirigir al agente adecuado (por idioma).


🛡 Seguridad y precisión
El modelo no puede inventar respuestas: solo responde con el contenido que tú le das.

Si una pregunta no se puede contestar con lo disponible, se deriva automáticamente.

Esto garantiza respuestas seguras y profesionalidad de marca.


📦 ¿Qué lo hace diferente?
✅ Modular y escalable

✅ Compatible con LangChain 0.3+

✅ Sin funciones obsoletas ni estructuras antiguas

✅ Preparado para integrarse en flujos empresariales

✅ Basado en prácticas reales usadas en consultoras de IA


🛠 Ideas para ampliación futura
Conexión a WhatsApp o webchat (Twilio, Flask)

Registro de logs y análisis de conversaciones

Clasificación con embudos de venta o prioridad

Conexión con un sistema RAG real (con FAISS o Chroma)

Interfaz visual con Streamlit o FastAPI

👤 Autor
Desarrollado por Veronika Ivanova, IA Architect & Prompt Engineer especializada en soluciones inteligentes para empresas.