import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "melhores_marcas_maquiagem.csv")

df = pd.read_csv(csv_path, index_col="Marca")

st.title("💄 Melhores Marcas de Maquiagem")

coluna = st.selectbox("Escolha o indicador:", df.columns)

fig, ax = plt.subplots(figsize=(12, 6))
df[coluna].sort_values().plot(kind="barh", ax=ax, color="hotpink")
ax.set_title(f"{coluna} por Marca")
ax.set_xlabel(coluna)
plt.tight_layout()

st.pyplot(fig)
