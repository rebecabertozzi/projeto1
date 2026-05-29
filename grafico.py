import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

# Dados embutidos diretamente no código — sem depender de arquivo CSV externo
CSV_DATA = """Marca,Avaliação Média (0-10),Nº de Produtos,Faixa de Preço Média (R$),Seguidores Instagram (milhões),Satisfação Clientes (%)
MAC,9.1,2800,185,13.2,92
Charlotte Tilbury,9.4,620,320,11.8,95
NARS,8.9,1100,210,7.4,90
Fenty Beauty,9.3,840,230,12.1,94
Maybelline,8.2,3200,65,14.5,85
L'Oréal,8.0,4100,75,10.3,83
Rare Beauty,9.2,310,195,9.8,96
Urban Decay,8.7,950,175,6.2,88
Too Faced,8.5,780,160,7.9,87
Anastasia Beverly Hills,9.0,520,250,20.1,91"""

df = pd.read_csv(StringIO(CSV_DATA), index_col="Marca")

st.title("💄 Melhores Marcas de Maquiagem")
st.markdown("Compare as principais marcas por diferentes indicadores.")

coluna = st.selectbox("Escolha o indicador:", df.columns)

cores = [
    "#FF69B4", "#FF85C2", "#FF99CC", "#FFB3D9", "#FFC6E5",
    "#FFADD6", "#FF94CA", "#FF7DBF", "#FF66B3", "#FF4DA6"
]

fig, ax = plt.subplots(figsize=(12, 6))
df_sorted = df[coluna].sort_values()
bars = ax.barh(df_sorted.index, df_sorted.values, color=cores)

ax.set_title(f"{coluna} por Marca", fontsize=15, fontweight="bold", pad=15)
ax.set_xlabel(coluna, fontsize=12)
ax.bar_label(bars, fmt="%.1f", padding=4, fontsize=10)
ax.spines[["top", "right"]].set_visible(False)
plt.tight_layout()

st.pyplot(fig)

st.dataframe(df.style.highlight_max(axis=0, color="#FFD6EC"), use_container_width=True)
