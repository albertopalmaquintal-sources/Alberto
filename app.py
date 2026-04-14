import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="Dashboard de Ventas", layout="wide")

st.title("?? Dashboard de Análisis de Ventas")

# 1. Cargar Datos (Sustituye con tu archivo .csv)
@st.cache_data
def load_data():
    # Simulando datos para el ejemplo
    data = pd.DataFrame({
        'Fecha': pd.date_range(start='2023-01-01', periods=100),
        'Producto': ['A', 'B', 'C', 'D'] * 25,
        'Ventas': [100, 150, 200, 250] * 25,
        'Ciudad': ['Mérida', 'Valladolid', 'Tizimín', 'Progreso'] * 25,
        'lat': [20.967, 20.690, 21.142, 21.283] * 25,
        'lon': [-89.623, -88.201, -88.149, -89.663] * 25
    })
    return data

df = load_data()

# --- FILTRO (Requisito 1) ---
st.sidebar.header("Filtros")
ciudad_selected = st.sidebar.multiselect(
    "Selecciona la Ciudad:",
    options=df["Ciudad"].unique(),
    default=df["Ciudad"].unique()
)

df_selection = df[df["Ciudad"].isin(ciudad_selected)]

# --- DATAFRAME (Requisito 1) ---
st.subheader("Datos Filtrados")
st.dataframe(df_selection)

# --- GRÁFICAS (Requisito 2: Al menos 3) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### Ventas por Producto")
    fig_bar = px.bar(df_selection, x="Producto", y="Ventas", color="Producto")
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    st.markdown("### Proporción por Ciudad")
    fig_pie = px.pie(df_selection, values='Ventas', names='Ciudad')
    st.plotly_chart(fig_pie, use_container_width=True)

with col3:
    st.markdown("### Tendencia Temporal")
    fig_line = px.line(df_selection, x="Fecha", y="Ventas")
    st.plotly_chart(fig_line, use_container_width=True)

# --- MAPA (Requisito 3) ---
st.subheader("?? Ubicación de Ventas en Yucatán")
st.map(df_selection)