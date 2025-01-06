
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

---

# Transformers y Modelos de Hugging Face

## ¿Qué son los Transformers?
Los transformers son una arquitectura de red neuronal que se utiliza para tareas de procesamiento de lenguaje natural (NLP) como clasificación, traducción, generación de texto, etc.

### Principales características:
- **Mecanismo de atención**: El modelo se enfoca en las partes importantes del texto según el contexto.
- **Procesamiento simultáneo**: A diferencia de modelos antiguos como las RNNs, los transformers procesan todo el texto de entrada al mismo tiempo, lo que los hace más rápidos.
- **Versatilidad**: Se pueden aplicar a tareas como análisis de sentimientos, generación de texto, resumen, entre otros.

## ¿Qué es Hugging Face?
Hugging Face es una plataforma que ofrece modelos pre-entrenados y una biblioteca en Python para usarlos fácilmente. Con Hugging Face, puedes implementar modelos como BERT, GPT, o T5 en pocas líneas de código.

### Ejemplo básico de uso:
```python
from transformers import pipeline

# Cargar un modelo de análisis de sentimientos
classifier = pipeline("sentiment-analysis")

# Analizar un texto
result = classifier("¡Me encanta Hugging Face!")
print(result)
```
---

# **Memoria requerida para un modelo**

La memoria necesaria para cargar un modelo depende directamente de su número de parámetros y del tamaño en bytes que ocupa cada parámetro (generalmente representados como flotantes de 32 bits). Esta métrica es fundamental para determinar los recursos de hardware necesarios para ejecutar el modelo, especialmente en tareas como entrenamiento o inferencia.


## **Ejemplos de tamaños de modelos comunes**
- **BERT base (bert-base-uncased):** Aproximadamente **440MB**.  
- **GPT-Neo (125M parámetros):** Aproximadamente **1.2GB**.


## **Cómo calcular la memoria requerida**

### **Fórmula general**
La memoria requerida se calcula multiplicando el número total de parámetros del modelo por el tamaño de cada parámetro (en bytes).

Memoria (bytes) = Número de parámetros × Tamaño de flotante


Donde:  
- **Número de parámetros**: Cantidad total de pesos o valores ajustables en el modelo.  
- **Tamaño de flotante**: Normalmente 4 bytes para representación en punto flotante de 32 bits (FP32).


### **Ejemplo práctico**
Un modelo con **110 millones de parámetros** (110M) representados en formato **FP32 (4 bytes por parámetro)**.

1. **Número de parámetros:** 110 millones → `110e6`.  
2. **Tamaño por parámetro:** 4 bytes.  
3. **Cálculo de memoria:**  

Memoria = 110e6 × 4 = 440 MB


Por lo tanto, el modelo ocuparía aproximadamente **440MB** en memoria.

---

# **Tamaños de Representaciones de Flotantes**

La siguiente tabla muestra los tamaños en bytes de las diferentes representaciones comunes de números flotantes utilizados en modelos de aprendizaje automático.

| **Representación** | **Nombre**                   | **Tamaño por parámetro (bytes)** | **Uso común**                                     |
|---------------------|------------------------------|----------------------------------|--------------------------------------------------|
| FP32                | Flotante de 32 bits         | 4                                | Entrenamiento e inferencia de alta precisión     |
| FP16                | Flotante de 16 bits         | 2                                | Inferencia y modelos optimizados para GPUs/TPUs |
| BF16                | Flotante de 16 bits (bfloat)| 2                                | Optimización para hardware acelerado            |
| INT8                | Entero de 8 bits            | 1                                | Cuantización para reducir memoria y velocidad    |

---
