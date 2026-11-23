from pydantic import BaseModel, Field

class AnalisisCV(BaseModel):
    """Modelo de datos para el analisis del un CV"""

    nombre_candidato : str = Field(description="Nombre completo del candidato extraido del cv")
    experiencia_años : int = Field(description="Años totales de experiencia laboral relevantes")
    habilidades_clave : list[str] = Field(descrption="lista de las 5 o 7 habilidades del candidato mas relevantes para el puesto")
    education : str = Field(description="Nivel educativo mas alto y la especializacion principal del candidato")
    experiencia_relevante : str =Field(description="Resumen conciso de la experiencia mas relevanmte para el puesto especifico")
    fortalezas : list[str] = Field(description="3-5 principales fortalezas del candidato basadas en su perfil")
    areas_mejora : list[str] = Field(description="2-4 ares donde el candidato pordira desarrollarse o mejorar")
    porcentaje_ajuste : int = Field(description="Procentaje del ajuste al puesto (0-100) basado en experiencia, habilidades y en la formacion", ge=0, le=100)
