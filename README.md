
# Models Execution

Este repositorio contiene 3 proyectos sobre implementación de modelos de IA, son los siguientes:

- Implementación de un modelo QA | #roberta-base-squad2
- Implementacion de dos modelos en una misma clase, traductor y resumen | t5-base
- Ejecución local de un modelo Object Detection | yolov5

---

# Configuración

1. Clona el respositorio
 ```bash
   git clone https://github.com/JuanManuelGilQuiroga/modelsExecution-HuggingFace
   ```
2. Instalacion de dependencias
 ```bash
   pip install -r requirements.txt
   ```

---

## Primer proyecto

Se implementa un modelo QA (Question Answering) el cual se emplea por medio de un frontend en streamlit.

Las librerias usadas fueron: 
- transformers
- streamlit
- torch

### Ejecucion
1. Accede a la carpeta con el proyecto
```bash 
    cd project1
```
2. Ejecuta el archivo con el siguiente comando
```bash 
    python -m streamlit run model.py
```

![alt text](image-1.png)

---

## Segundo proyecto

Se implementan dos modelos (traductor y resumen) en una misma clase, esta clase se importa en el archivo que configura el frontend en streamlit. El traductor funciona de ingles a frances.

Las librerias usadas fueron: 
- transformers
- streamlit
- sentencepiece
- torch

### Ejecucion
1. Accede a la carpeta con el proyecto
```bash 
    cd project2
```
2. Ejecuta el archivo con el siguiente comando
```bash 
    python -m streamlit run view.py
```

![alt text](image-2.png)

---

## Tercer proyecto

Se ejecuta un modelo de object detection localmente y se crea un archivo que le permite al codigo analizar un archivo de imagen en la carpeta images del mismo directorio.

Las librerias usadas fueron: 
- transformers
- streamlit

### Ejecucion
1. Accede a la carpeta con el proyecto
```bash 
    cd project3
```
2. Ejecuta el archivo con el siguiente comando
```bash 
    python main.py
```
 El resultado tiene que verse asi:

![alt text](image.png)