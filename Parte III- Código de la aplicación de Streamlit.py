import streamlit as st
import pandas as pd
import plotly.express as px
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Preprocess the text
def preprocess_text(text):
    stop_words = set(stopwords.words('spanish'))
    words = nltk.word_tokenize(text.lower())
    return ' '.join([word for word in words if word.isalnum() and word not in stop_words])

# Function to categorize text using the model
def categorize_text(model, text):
    return model.predict([text])[0]

# Streamlit app layout
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>News Categorization App</h1>", unsafe_allow_html=True)

# Sidebar with Upload and Options
st.sidebar.title("Options")
uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv"])

# Main Layout
if uploaded_file is not None:
    # Load the CSV into a DataFrame
    news_df = pd.read_csv(uploaded_file)
    
    # Ensure the dataframe has necessary columns
    if 'content' in news_df.columns and 'title' in news_df.columns and 'publishedAt' in news_df.columns:
        
        # Preprocess text data
        news_df['processed_content'] = news_df['content'].apply(preprocess_text)
        
        # Sample training data
        train_data = [
            ("Nuevo smartphone lanzado al mercado", "Tecnología"),
            ("Equipo de fútbol gana el campeonato", "Deportes"),
            ("Presidente anuncia nuevas medidas económicas", "Política"),
            ("Estreno de película bate récords de taquilla", "Entretenimiento"),
            ("Bolsa de valores alcanza nuevo máximo histórico", "Economía"),
            ("Microsoft lanza nueva versión de Windows", "Tecnología"),
            ("Jugador de baloncesto firma contrato millonario", "Deportes"),
            ("Elecciones presidenciales se llevarán a cabo en noviembre", "Política"),
            ("Actor famoso protagoniza nueva serie de televisión", "Entretenimiento"),
            ("Crecimiento del PIB supera las expectativas", "Economía"),
            ("Investigadores desarrollan nueva tecnología de inteligencia artificial", "Tecnología"),
            ("Torneo de tenis comienza esta semana", "Deportes"),
            ("Gobierno aprueba nueva ley de impuestos", "Política"),
            ("Festival de música atrae a miles de personas", "Entretenimiento"),
            ("Inflación alcanza su nivel más bajo en una década", "Economía"),
            ("Apple presenta sus nuevos dispositivos en conferencia anual", "Tecnología"),
            ("Equipo de béisbol consigue importante victoria", "Deportes"),
            ("Debate presidencial se centra en temas económicos", "Política"),
            ("Nueva película de superhéroes es un éxito en taquilla", "Entretenimiento"),
            ("Mercado de valores muestra signos de recuperación", "Economía"),
            ("Samsung lanza nuevo modelo de smartphone con tecnología avanzada", "Tecnología"),
            ("Selección nacional de fútbol se prepara para el mundial", "Deportes"),
            ("Parlamento discute reformas políticas", "Política"),
            ("Festival de cine presenta las mejores películas del año", "Entretenimiento"),
            ("Tasa de desempleo cae por tercer mes consecutivo", "Economía"),
            ("Google desarrolla nuevo algoritmo de búsqueda", "Tecnología"),
            ("Maratón de la ciudad atrae a corredores de todo el mundo", "Deportes"),
            ("Nuevo ministro de economía promete reducir la deuda", "Política"),
            ("Serie de televisión recibe premios internacionales", "Entretenimiento"),
            ("Exportaciones aumentan por quinto mes consecutivo", "Economía"),
            ("Tesla anuncia avances en conducción autónoma", "Tecnología"),
            ("Equipo de hockey gana el torneo internacional", "Deportes"),
            ("Candidato presidencial promete reformas educativas", "Política"),
            ("Documental sobre la naturaleza es aclamado por la crítica", "Entretenimiento"),
            ("Inversiones extranjeras crecen en el último trimestre", "Economía"),
            ("Facebook lanza nueva funcionalidad para empresas", "Tecnología"),
            ("Copa del mundo de cricket genera gran expectación", "Deportes"),
            ("Protestas en la capital por nuevas políticas gubernamentales", "Política"),
            ("Obra de teatro local se convierte en un éxito", "Entretenimiento"),
            ("Venta de viviendas crece en el último año", "Economía"),
            ("Huawei introduce nueva línea de dispositivos móviles", "Tecnología"),
            ("Equipo de natación rompe récords en campeonato", "Deportes"),
            ("Políticos debaten sobre el cambio climático", "Política"),
            ("Concierto benéfico recauda fondos para la caridad", "Entretenimiento"),
            ("Producción industrial se expande en la región", "Economía"),
            ("IBM desarrolla supercomputadora para investigación", "Tecnología"),
            ("Campeonato de voleibol atrae a equipos de todo el país", "Deportes"),
            ("Parlamento aprueba ley de protección ambiental", "Política"),
            ("Película animada recibe excelentes críticas", "Entretenimiento"),
            ("Consumo de energía renovable aumenta significativamente", "Economía"),
        ]
        
        # Extract text and labels from training data
        X_train, y_train = zip(*train_data)
        
        # Create and train the model
        model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        model.fit(X_train, y_train)
        
        # Categorize articles in the dataframe
        news_df['category'] = news_df['processed_content'].apply(lambda x: categorize_text(model, x))
        
        # Date filtering with slider
        min_date = pd.to_datetime(news_df['publishedAt']).min().date()
        max_date = pd.to_datetime(news_df['publishedAt']).max().date()
        selected_date_range = st.sidebar.slider("Select Date Range", min_date, max_date, (min_date, max_date))
        filtered_df = news_df[
            (pd.to_datetime(news_df['publishedAt']).dt.date >= selected_date_range[0]) &
            (pd.to_datetime(news_df['publishedAt']).dt.date <= selected_date_range[1])
        ]
        
        # Display the filtered dataframe with categories
        st.subheader("Dataframe of Articles with Categories")
        st.dataframe(filtered_df[['title', 'category', 'publishedAt']])
        
        # Bar chart: Distribution of news categories
        st.subheader("Bar Chart: Distribution of News Categories")
        category_distribution = filtered_df['category'].value_counts()
        fig_bar = px.bar(category_distribution, x=category_distribution.index, y=category_distribution.values, labels={'x': 'Category', 'y': 'Count'}, title="Distribution of News Categories")
        st.plotly_chart(fig_bar)
        
        # Interactive time series plot
        if 'publishedAt' in filtered_df.columns:
            st.subheader("Interactive Time Series Plot")
            time_series_data = filtered_df.groupby([pd.to_datetime(filtered_df['publishedAt']).dt.date, 'category']).size().reset_index(name='counts')
            fig_time_series = px.line(time_series_data, x='publishedAt', y='counts', color='category', title="Time Series of News Categories")
            st.plotly_chart(fig_time_series)
        
    else:
        st.error("CSV must contain 'content', 'title', and 'publishedAt' columns.")
else:
    st.write("Please upload a CSV file to begin.")
