import streamlit as st
import pandas as pd

st.set_page_config(page_title="Recomendador de financiación para custodia", layout="wide")

st.title("Recomendador de instrumentos financieros para custodia del territorio")

st.markdown("Esta herramienta permite seleccionar los factores que caracterizan una propuesta de custodia y calcular la idoneidad de distintos instrumentos de financiación innovadora.")

st.subheader("⚙️ Selección de factores (versión demostrativa)")
st.info("Esta es una versión de demostración. La evaluación automática basada en ponderaciones se implementará en la siguiente fase.")

uploaded_file = st.file_uploader("🔽 Sube la tabla Excel con los datos de simulación", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file, sheet_name="Factores", header=5)
        st.success("Archivo cargado correctamente. A continuación se muestra la tabla de simulación:")
        st.dataframe(df, use_container_width=True)
        st.markdown("➡️ En próximas versiones se mostrará el análisis de idoneidad de cada instrumento.")
    except Exception as e:
        st.error(f"Error al leer el archivo: {e}")
