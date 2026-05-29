import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("melhores_marcas_maquiagem.csv", index_col="Marca")

st.title("💄 Melhores Marcas de Maquiagem")

coluna = st.selectbox("Escolha o indicador:", df.columns)

fig, ax = plt.subplots(figsize=(12, 6))
df[coluna].sort_values().plot(kind="barh", ax=ax, color="hotpink")
ax.set_title(f"{coluna} por Marca")
ax.set_xlabel(coluna)
plt.tight_layout()

st.pyplot(fig)
