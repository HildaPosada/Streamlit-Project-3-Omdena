
# Análisis de Noticias de Tecnología en Colombia

Este proyecto permite obtener y analizar noticias de tecnología en Colombia utilizando la API de News API. El objetivo es extraer, procesar y visualizar datos relevantes sobre el tema.

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

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.




