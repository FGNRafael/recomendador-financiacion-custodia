
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Recomendador de financiación para custodia", layout="wide")

st.title("Simulador de idoneidad para instrumentos financieros en custodia del territorio")
st.markdown("Introduce las características de tu propuesta de custodia para conocer qué instrumentos innovadores de financiación podrían ser más adecuados.")

# Cargar datos desde archivo subido previamente
@st.cache_data
def cargar_datos():
    archivo = "APP_web_financiacion_custodia_V2.xlsx"
    df_factores = pd.read_excel(archivo, sheet_name="Factores")
    df_instrumentos = pd.read_excel(archivo, sheet_name="Instrumentos")
    return df_factores, df_instrumentos

df_factores, df_instrumentos = cargar_datos()

# Mostrar una interfaz de prueba con selección de un conjunto limitado de factores para simplicidad
st.header("Formulario simplificado de prueba")
inclusion = st.selectbox("1.2 Inclusión", ["Prioritario", "Secundario", "No incluido"])
proteccion = st.selectbox("2 Protección", ["Espacio protegido UE", "Parque Nacional", "Parque Natural", "Reserva o LIC/ZEC", "Sin protección formal"])
propiedad = st.selectbox("3 Propiedad", ["Pública", "Comunal", "Privada colectiva", "Privada individual", "Desconocida o mixta"])
coste = st.selectbox("5 Coste estimado", ["Hasta 100.000 €", "De 100.001 a 400.000", "De 400.001 a 800.000", "De 800.001 a 1.500.000", "Más de 1.500.000"])
objetivo = st.selectbox("8.2 Incidencia del objetivo principal", ["Objetivo motor", "Objetivo estratégico", "Efecto multiplicador", "Efecto colateral", "Sin incidencia"])

# Definir equivalencias
mapeos = {
    "1.2 Inclusión": {"Prioritario": 1, "Secundario": 0.6, "No incluido": 0},
    "2 Protección": {"Espacio protegido UE": 1, "Parque Nacional": 0.9, "Parque Natural": 0.8, "Reserva o LIC/ZEC": 0.7, "Sin protección formal": 0},
    "3 Propiedad": {"Pública": 1, "Comunal": 0.8, "Privada colectiva": 0.7, "Privada individual": 0.6, "Desconocida o mixta": 0.4},
    "5 Coste estimado": {"Hasta 100.000 €": 0.2, "De 100.001 a 400.000": 0.4, "De 400.001 a 800.000": 0.6, "De 800.001 a 1.500.000": 0.8, "Más de 1.500.000": 1},
    "8.2 Incidencia": {"Objetivo motor": 1, "Objetivo estratégico": 0.8, "Efecto multiplicador": 0.6, "Efecto colateral": 0.4, "Sin incidencia": 0}
}
coeficientes = {"1.2 Inclusión": 1.0, "2 Protección": 0.8, "3 Propiedad": 0.7, "5 Coste estimado": 0.5, "8.2 Incidencia": 0.8}

# Calcular puntuación
puntuacion_total = sum([
    mapeos["1.2 Inclusión"][inclusion] * coeficientes["1.2 Inclusión"],
    mapeos["2 Protección"][proteccion] * coeficientes["2 Protección"],
    mapeos["3 Propiedad"][propiedad] * coeficientes["3 Propiedad"],
    mapeos["5 Coste estimado"][coste] * coeficientes["5 Coste estimado"],
    mapeos["8.2 Incidencia"][objetivo] * coeficientes["8.2 Incidencia"]
])
maxima = sum(coeficientes.values())

indice = puntuacion_total / maxima * 100

st.subheader("Resultado preliminar de idoneidad")
st.metric(label="Índice de adecuación del proyecto", value=f"{indice:.1f}%", delta=None)

st.markdown("### Interpretación del resultado")

if indice >= 80:
    st.success("El índice indica una alta idoneidad. Este proyecto de custodia presenta una gran compatibilidad con múltiples instrumentos de financiación innovadora.")
elif indice >= 60:
    st.info("Buena compatibilidad. Se identifican instrumentos viables, aunque puede haber margen de mejora en algunos factores.")
elif indice >= 40:
    st.warning("Compatibilidad parcial. El proyecto podría necesitar ajustes o enfoques complementarios para acceder a financiación adecuada.")
else:
    st.error("Idoneidad baja. Es recomendable replantear algunos factores clave o explorar otras fórmulas de financiación.")
