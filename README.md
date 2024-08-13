# Proyecto Final: Desarrollo de un sistema de noticias. Análisis de noticias

By José Enrique, Hilda Posada, Daniel Alvarado, Alexa Gloss
Objetivo General

El objetivo principal de este proyecto es aplicar los fundamentos de ciencia de datos para desarrollar un sistema integral de análisis de noticias para un determinado tema. Se abordarán diferentes etapas, desde la obtención de datos mediante API hasta la implementación de modelos de aprendizaje automático y procesamiento del lenguaje natural, culminando con la creación de una interfaz interactiva utilizando Streamlit y una presentación final frente a los stakeholders objetivo.

Tema elegido por el equipo:

Vamos a indagar sobre las noticias respecto a tecnología con el fin de entender cuáles son los diarios más activos de noticias tecnológicas para el ministerio de Tecnologías de Colombia.

Enlaces Importantes:
[Google Colab Project](https://colab.research.google.com/drive/10WOh4ydRyKezrosZAkAmIg3kn-xRNeSb#scrollTo=_I1IIl8OC0DX),
[Medium Blog](https://medium.com/@hildaecogreen/9bfb0fe613b5)


# Cómo ejecutar el código
Requisitos

Asegúrate de tener instalados los siguientes paquetes en tu entorno de trabajo:

    streamlit
    pandas
    plotly
    nltk
    scikit-learn

Puedes instalar estos paquetes utilizando pip:
pip install streamlit pandas plotly nltk scikit-learn

# Paso 1: Descarga los recursos de NLTK

El código hace uso de las bibliotecas de NLTK para el procesamiento de texto. Antes de ejecutar el código, asegúrate de descargar los recursos necesarios:

    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')

# Paso 2: Ejecuta la aplicación en Streamlit

Asegúrate de tener el archivo noticias_categorizadas_20240803131627.csv en el mismo directorio que tu script de Python.

Luego, puedes ejecutar la aplicación de Streamlit utilizando el siguiente comando en tu terminal:

    streamlit run nombre_del_script.py

# Paso 3: Interactúa con la aplicación

Una vez que la aplicación esté en funcionamiento:

1. Filtrado de Fechas: Utiliza el deslizador en la barra lateral para seleccionar el rango de fechas que te interesa.
2. Categorización en Tiempo Real: Ingresa contenido de noticias en el cuadro de texto proporcionado para obtener una predicción de categoría.
3. Visualización de Datos: Explora el dataframe filtrado y las gráficas interactivas que se generan automáticamente.

# Estructura del Proyecto

noticias_categorizadas_20240803131627.csv: Archivo CSV con las noticias categorizadas.
nombre_del_script.py: Script principal para la ejecución de la aplicación Streamlit.
README.md: Este archivo, que contiene instrucciones sobre cómo ejecutar el proyecto.

# Notas Adicionales

Este proyecto fue desarrollado como parte de la colaboración con Omdena para el desarrollo de soluciones basadas en IA. La aplicación permite analizar, categorizar y visualizar noticias tecnológicas de interés para el Ministerio de Tecnologías de Colombia.