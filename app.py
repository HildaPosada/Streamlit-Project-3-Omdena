import streamlit as st
import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

# Descargar recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Preprocesamiento de texto
def preprocess_text(text):
    stop_words = set(stopwords.words('spanish'))
    words = nltk.word_tokenize(text.lower())
    return ' '.join([word for word in words if word.isalnum() and word not in stop_words])

# Definir categorías y datos de entrenamiento
train_data = [
    ("Nuevo smartphone lanzado al mercado", "Tecnología", "La última versión del smartphone de Apple ha sido lanzada con nuevas características innovadoras."),
    ("Equipo de fútbol gana el campeonato", "Deportes", "El equipo nacional de fútbol se coronó campeón en un emocionante partido final."),
    ("Presidente anuncia nuevas medidas económicas", "Política", "El presidente ha anunciado una serie de nuevas políticas destinadas a mejorar la economía."),
    ("Estreno de película bate récords de taquilla", "Entretenimiento", "La nueva película de Marvel ha superado todos los récords de taquilla en su primer fin de semana."),
    ("Bolsa de valores alcanza nuevo máximo histórico", "Economía", "El índice bursátil ha alcanzado un nuevo máximo histórico, impulsado por el crecimiento en el sector tecnológico."),
    # (Agregar más datos de entrenamiento aquí)
]

X_train, y_train, _ = zip(*train_data)

# Crear y entrenar el modelo
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# Función para categorizar texto
def categorize_text(text):
    return model.predict([text])[0]

# Aplicación Streamlit
st.title("Resumen de Categorías de Noticias")

uploaded_file = st.file_uploader("Cargar archivo CSV", type="csv")

if uploaded_file:
    news_df = pd.read_csv(uploaded_file)
    news_df['processed_content'] = news_df['content'].apply(preprocess_text)

    if st.button('Generar Resumen'):
        news_df['category'] = news_df['processed_content'].apply(categorize_text)
        category_counts = news_df['category'].value_counts()

        st.write(news_df[['title', 'category']])

        st.subheader("Distribución de Categorías")
        fig, ax = plt.subplots()
        category_counts.plot(kind='bar', ax=ax)
        st.pyplot(fig)
