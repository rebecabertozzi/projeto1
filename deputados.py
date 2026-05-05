import streamlit as st
import pandas as pd

st.title("Consulta de Deputados 2022")

# ---- CARREGAMENTO ----
try:
    df = pd.read_csv('deputados_2022.csv')
except Exception as e:
    st.error(f"Erro ao carregar o arquivo: {e}")
    st.stop()

# ---- PADRONIZAÇÃO DE COLUNAS ----
df.columns = df.columns.str.lower()

# Verificar colunas necessárias
if 'partido' not in df.columns or 'uf' not in df.columns:
    st.error("O CSV precisa ter colunas chamadas 'partido' e 'uf'")
    st.stop()

# ---- PADRONIZAÇÃO DE DADOS ----
df['partido'] = df['partido'].astype(str).str.upper()
df['uf'] = df['uf'].astype(str).str.upper()

# Padronizar sexo (M/F)
if 'sexo' in df.columns:
    df['sexo'] = df['sexo'].astype(str).str.upper()
else:
    st.warning("Coluna 'sexo' não encontrada. Filtro de sexo não será aplicado.")

# ---- FILTROS ----
lista_partidos = sorted(df["partido"].dropna().unique())

partido_select = st.selectbox(
    "Escolha um partido (opcional)",
    [""] + lista_partidos
)

partido_input = st.text_input("Ou digite o partido:")
uf_input = st.text_input("Filtrar por UF:")

sexo_select = ""
if 'sexo' in df.columns:
    sexo_select = st.selectbox(
        "Filtrar por sexo:",
        ["", "M", "F"]
    )

# ---- FILTRAGEM ----
df_filtrado = df.copy()

if partido_input:
    df_filtrado = df_filtrado[df_filtrado['partido'] == partido_input.upper()]
elif partido_select:
    df_filtrado = df_filtrado[df_filtrado['partido'] == partido_select]

if uf_input:
    df_filtrado = df_filtrado[df_filtrado['uf'] == uf_input.upper()]

if sexo_select:
    df_filtrado = df_filtrado[df_filtrado['sexo'] == sexo_select]

# ---- RESULTADO ----
st.write(f"Total de registros: {len(df_filtrado)}")
st.dataframe(df_filtrado)
