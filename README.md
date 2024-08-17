
# Análisis de Categorías de títulos en Noticias de Colombia

Este proyecto permite obtener y analizar Categorías de títulos en Noticias de Colombia utilizando la API de News API. El objetivo es extraer, procesar y visualizar datos relevantes sobre el tema.

[Google Colab Project](https://colab.research.google.com/drive/10WOh4ydRyKezrosZAkAmIg3kn-xRNeSb#scrollTo=_I1IIl8OC0DX), 
[Medium Blog](https://medium.com/@hildaecogreen/9bfb0fe613b5).

# Project Files

- `noticias_categorizadas_20240803131627.csv`: Archivo CSV con las noticias categorizadas.
- `nombre_del_script.py`: Script principal para la ejecución de la aplicación Streamlit.
- `README.md`: Este archivo, que contiene instrucciones sobre cómo ejecutar el proyecto.
"""

## Requisitos

Antes de ejecutar el código, asegúrate de tener instaladas las siguientes librerías:

- `requests`
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `wordcloud`
- `scikit-learn`
- `nltk`
- `python-dotenv`

Puedes instalarlas usando pip:

```bash
pip install requests pandas numpy matplotlib seaborn wordcloud scikit-learn nltk python-dotenv
```

## Configuración

1. **Obtener la clave de API**: Para utilizar la API de News API, necesitas obtener una clave de API. Puedes registrarte y obtener la tuya en [News API](https://newsapi.org/).

2. **Configurar la clave de API**: La clave de API debe ser colocada en la variable `api_key` en el código. Puedes almacenar esta clave en un archivo `.env` para mayor seguridad, utilizando la librería `python-dotenv`.

## Uso

1. **Consulta de noticias**: El script realiza una consulta a la API de News API para obtener noticias relacionadas con la tecnología en Colombia. Los resultados se guardan en un DataFrame de pandas y también se exportan a un archivo CSV.

2. **Manipulación de datos**: Se eliminan columnas innecesarias y se guarda el DataFrame manipulado en otro archivo CSV.

3. **Análisis Exploratorio de Datos (EDA)**:
   - Información básica y resumen estadístico del DataFrame.
   - Visualización de la distribución de artículos por fecha, día de la semana y hora del día.
   - Análisis de la longitud de los títulos y descripciones de las noticias.

4. **Visualización Gráfica**: Se generan diferentes gráficos para visualizar las tendencias en los datos, incluyendo:
   - Distribución de artículos por fuente.
   - Análisis de las palabras más comunes en los títulos.
   - Distribución de sentimientos en las descripciones.

## Resultados

Los resultados del análisis se pueden visualizar mediante gráficos generados con `matplotlib` y `seaborn`. También se obtiene un archivo CSV con la información procesada para un análisis posterior.


############## PARTE 2 ###################

# Clasificación de Noticias de Tecnología en Colombia

Este proyecto utiliza la biblioteca NLTK (Natural Language Toolkit) junto con scikit-learn para realizar la categorización automática de noticias basadas en su contenido. El objetivo es preprocesar el texto de noticias, entrenar un modelo de clasificación y luego categorizar nuevas noticias en diferentes temas.

## Requisitos

Antes de ejecutar el código, asegúrate de tener instaladas las siguientes librerías:

- `pandas`
- `nltk`
- `scikit-learn`

Puedes instalarlas usando pip:

```bash
pip install pandas nltk scikit-learn
```

## Configuración

1. **Descargar recursos de NLTK**: El script descargará automáticamente los recursos necesarios de NLTK, como las stopwords en español y el tokenizador.

2. **Cargar el archivo CSV**: Asegúrate de tener el archivo `tecnologia_colombia_manipulada20240705225512.csv` en el mismo directorio donde se ejecutará el script. Este archivo contiene las noticias previamente manipuladas y servirá como entrada para la clasificación.

## Uso

1. **Preprocesamiento de texto**: 
   - El texto se tokeniza y se eliminan las stopwords utilizando las funciones de NLTK.
   - El contenido preprocesado se almacena en una nueva columna del DataFrame.

2. **Definición y entrenamiento del modelo**:
   - Se definen manualmente algunas noticias de ejemplo con sus respectivas categorías (Tecnología, Deportes, Política, Entretenimiento, Economía) para entrenar el modelo.
   - Se utiliza `TfidfVectorizer` para convertir el texto en vectores TF-IDF y `MultinomialNB` para entrenar un modelo Naive Bayes multinomial.

3. **Categorización automática**:
   - El modelo entrenado se utiliza para predecir la categoría de cada noticia en el DataFrame.
   - Las categorías predichas se almacenan en una nueva columna llamada `category`.

4. **Guardar el resultado**:
   - El DataFrame actualizado se guarda en un archivo CSV con un nombre basado en la fecha y hora actuales.
   - El archivo de salida contiene las noticias con su respectiva categoría predicha.

## Resultados

El archivo resultante `noticias_categorizadas_<timestamp>.csv` contendrá las noticias categorizadas según el modelo entrenado. Además, se muestra un resumen de las primeras noticias categorizadas.

#################### PARTE 3 ################

# Colombian News Categorization App

Esta aplicación permite categorizar noticias colombianas en tiempo real utilizando técnicas de procesamiento de lenguaje natural y aprendizaje automático. La interfaz está construida con Streamlit y permite a los usuarios interactuar con los datos y visualizar las categorías de las noticias de manera dinámica.

## Requisitos

Antes de ejecutar el código, asegúrate de tener instaladas las siguientes librerías:

- `streamlit`
- `pandas`
- `plotly`
- `nltk`
- `scikit-learn`

Puedes instalarlas usando pip:

```bash
pip install streamlit pandas plotly nltk scikit-learn
```

## Configuración

1. **Descargar recursos de NLTK**: El script descargará automáticamente los recursos necesarios de NLTK, como las stopwords en español y el tokenizador.

2. **Cargar el archivo CSV**: Asegúrate de tener el archivo `noticias_categorizadas_20240803131627.csv` en el mismo directorio donde se ejecutará el script. Este archivo contiene las noticias categorizadas y se utilizará para entrenar el modelo.

## Uso

1. **Preprocesamiento de texto**: 
   - El texto se tokeniza y se eliminan las stopwords utilizando funciones de NLTK.
   - El contenido preprocesado se utiliza para entrenar el modelo.

2. **Modelo de clasificación**:
   - Se utiliza `TfidfVectorizer` para convertir el texto en vectores TF-IDF y `MultinomialNB` para entrenar un modelo Naive Bayes multinomial.
   - El modelo entrenado se utiliza para predecir la categoría de las noticias en tiempo real.

3. **Interfaz de usuario con Streamlit**:
   - **Filtrado por rango de fechas**: Los usuarios pueden filtrar las noticias según la fecha de publicación utilizando un control deslizante.
   - **Categorización en tiempo real**: Los usuarios pueden ingresar contenido de noticias en tiempo real para obtener una predicción de la categoría.
   - **Visualización**:
     - **Tabla de artículos filtrados**: Muestra las noticias filtradas por categoría y fecha de publicación.
     - **Gráfico de barras**: Visualiza la distribución de categorías de noticias en los datos filtrados.
     - **Gráfico de series de tiempo**: Muestra la evolución de las categorías de noticias a lo largo del tiempo.

## Ejecución

Para ejecutar la aplicación, usa el siguiente comando en tu terminal:

```bash
streamlit run app.py
```

**Nota**: Asegúrate de estar en el directorio donde se encuentra el archivo `app.py`.

## Personalización de la Interfaz

La interfaz de la aplicación incluye estilos personalizados en CSS para mejorar la apariencia de los botones y el fondo de la aplicación.

## Resultados

La aplicación genera visualizaciones interactivas y permite a los usuarios explorar las categorías de noticias de una manera dinámica e intuitiva. También proporciona una funcionalidad de categorización de noticias en tiempo real basada en el modelo entrenado.

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar tu inquietud al correo peresdaniel24@gmail.com





