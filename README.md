# Analizador de CVs con IA

Aplicación que evalúa un CV en PDF frente a la descripción de un puesto de trabajo y devuelve un análisis estructurado del candidato.

## ¿Cómo funciona?

1. El usuario sube un CV en PDF y pega la descripción del puesto.
2. Se extrae el texto del PDF (PyPDF2).
3. GPT-4o-mini analiza el CV con un prompt de reclutamiento y devuelve **salida estructurada** validada con Pydantic:
   - Nombre del candidato y años de experiencia
   - Habilidades clave para el puesto
   - Formación académica y experiencia relevante
   - Fortalezas y áreas de mejora
   - **Porcentaje de ajuste al puesto (0–100)**
4. Si el PDF está vacío o es escaneado, la app lo detecta y muestra un diagnóstico en lugar de fallar.

## Estructura

```
cv_analyzer/
├── app.py                  # punto de entrada
├── models/cv_model.py      # esquema Pydantic del análisis
├── prompts/cv_prompts.py   # prompts del evaluador
├── services/
│   ├── pdf_processor.py    # extracción de texto del PDF
│   └── cv_evaluator.py     # cadena LangChain + salida estructurada
└── ui/streamlit_ui.py      # interfaz
```

## Tecnologías

Python · LangChain · OpenAI API (GPT-4o-mini) · Pydantic · PyPDF2 · Streamlit

## Instalación

```bash
pip install streamlit langchain-openai pydantic PyPDF2
```

Configura tu API key de OpenAI como variable de entorno:

```bash
# PowerShell
$env:OPENAI_API_KEY="tu-api-key"
# Linux / Mac
export OPENAI_API_KEY="tu-api-key"
```

## Uso

```bash
streamlit run app.py
```
