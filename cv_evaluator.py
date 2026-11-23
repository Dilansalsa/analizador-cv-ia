from langchain_openai import ChatOpenAI
from prompts.cv_prompts import crear_sistema_prompts
from models.cv_model import AnalisisCV

def crear_evaluador_cv():
    chat_model = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2
    )

    chat_prompt = crear_sistema_prompts()
    modelo_estructurada = chat_model.with_structured_output(AnalisisCV)
    cadena_evaluadora = chat_prompt | modelo_estructurada
    
    return cadena_evaluadora

def evaluar_candidato(texto_cv: str, descripcion_puesto: str) -> AnalisisCV:
    try:
        cadena_evaluadora  = crear_evaluador_cv()

        respuesta = cadena_evaluadora.invoke({
            "texto_cv": texto_cv,
            "descripcion_puesto": descripcion_puesto
        })

        return respuesta
    except Exception as e:
        error_real = str(e)
        return AnalisisCV(
            nombre_candidato = "Error del procesamiento",
            experiencia_años = 0,
            habilidades_clave = ["Error al procesar el CV"],
            education = "No se puede determinar",
            experiencia_relevante = f"Error durante el analisis error real: {error_real}",
            fortalezas = ["Error al procesar el CV"],
            areas_mejora = ["Error al procesar el CV"],
            porcentaje_ajuste = 0
        )
