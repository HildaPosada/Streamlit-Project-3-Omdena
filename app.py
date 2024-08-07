import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

# Generar datos ficticios
np.random.seed(42)
dates = pd.date_range(start='2022-01-01', periods=100)
data1 = np.random.randn(100).cumsum()
data2 = np.random.randn(100).cumsum()

# Crear un dataframe
df1 = pd.DataFrame({'Date': dates, 'Value': data1, 'Dataset': 'Dataset 1'})
df2 = pd.DataFrame({'Date': dates, 'Value': data2, 'Dataset': 'Dataset 2'})
df = pd.concat([df1, df2])

# Layout de la aplicación
st.title('Aplicación de Gráfico de Línea de Tiempo con Streamlit y Plotly')

# Crear dos columnas
col1, col2 = st.columns(2)

# Columna 1: Gráfico de línea de tiempo
with col1:
    st.header('Gráfico de Línea de Tiempo')
    selected_dataset = st.session_state.get('selected_dataset', 'Dataset 1')
    filtered_df = df[df['Dataset'] == selected_dataset]
    fig = px.line(filtered_df, x='Date', y='Value', title=f'Valores de {selected_dataset}')
    st.plotly_chart(fig)

# Columna 2: Selector de datos y botón de calcular
with col2:
    st.header('Selecciona tus Datos')
    selected_dataset = st.selectbox('Seleccionar Dataset', df['Dataset'].unique())
    
    if st.button('Calcular'):
        st.session_state['selected_dataset'] = selected_dataset
        st.rerun()

# Mostrar datos seleccionados
st.write(f"Datos seleccionados: {selected_dataset}")
