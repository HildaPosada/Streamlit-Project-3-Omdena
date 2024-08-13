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

# Load the CSV file
csv_file_path = "noticias_categorizadas_20240803131627.csv"
news_df = pd.read_csv(csv_file_path)

# Extract text and labels from the data
train_data = list(zip(news_df['content'], news_df['category']))
X_train, y_train = zip(*train_data)

# Create and train the model
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)

# Custom CSS for styling
st.markdown("""
    <style>
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        padding: 10px 24px;
        margin: 10px 0;
    }
    .stTextInput>div>div>textarea {
        border-radius: 10px;
        border: 1px solid #ddd;
    }
    .reportview-container {
        background-color: #0E1117;
        color: white;
    }
    .result-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit app layout
st.markdown("<h1 style='text-align: center; color: #FFD700;'>Colombian News Categorization App</h1>", unsafe_allow_html=True)

# Date filtering with slider
news_df['publishedAt'] = pd.to_datetime(news_df['publishedAt'])
min_date = news_df['publishedAt'].min().date()
max_date = news_df['publishedAt'].max().date()
selected_date_range = st.sidebar.slider("Select Date Range", min_date, max_date, (min_date, max_date))

# Real-time news categorization
st.sidebar.subheader("Real-time News Categorization")
real_time_input = st.sidebar.text_area("Enter news content for categorization:")
categorize_button = st.sidebar.button("Categorize🔍", key="sidebar_button")

if categorize_button and real_time_input:
    with st.spinner('Categorizing...'):
        predicted_category = categorize_text(model, preprocess_text(real_time_input))
        st.sidebar.markdown(f"<div class='result-container'><b>Predicted Category:</b> {predicted_category}</div>", unsafe_allow_html=True)

# Filter data based on selected date range
filtered_df = news_df[
    (news_df['publishedAt'].dt.date >= selected_date_range[0]) &
    (news_df['publishedAt'].dt.date <= selected_date_range[1])
]

# Display the filtered dataframe with categories and published date
st.subheader("Dataframe of Articles with Categories📰")
filtered_df = filtered_df.rename(columns={'title': 'Title', 'category': 'Category', 'publishedAt': 'Published Date'})
st.dataframe(filtered_df[['Title', 'Category', 'Published Date']])

# Bar chart: Distribution of news categories
st.subheader("Bar Chart: Distribution of News Categories")
category_distribution = filtered_df['Category'].value_counts()
fig_bar = px.bar(category_distribution, x=category_distribution.index, y=category_distribution.values, labels={'x': 'Category', 'y': 'Counts'}, title="Distribution of News Categories")
fig_bar.update_layout(
    hovermode="x",
    title={
        'text': "Distribution of News Categories",
        'y': 0.9,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    margin=dict(l=0, r=0, t=30, b=0),
    paper_bgcolor="#0E1117",
    plot_bgcolor="#0E1117",
)
st.plotly_chart(fig_bar)

# Interactive time series plot
if 'Published Date' in filtered_df.columns:
    st.subheader("Interactive Time Series Plot")
    time_series_data = filtered_df.groupby([filtered_df['Published Date'].dt.date, 'Category']).size().reset_index(name='Counts')
    fig_time_series = px.line(time_series_data, x='Published Date', y='Counts', color='Category', title="Time Series of News Categories")
    st.plotly_chart(fig_time_series)
