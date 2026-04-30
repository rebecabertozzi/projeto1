import streamlit as st
import random

st.set_page_config(
    page_title="Recomendador de Filmes 🎬",
    page_icon="🎥",
    layout="centered"
)

st.title("🎬 Recomendador de Filmes")
st.write("Escolha um gênero e descubra um filme!")

filmes = {
    "Ação": [
        {"nome": "Gladiador", "duracao": "2h 35min", "imagem": "https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg"},
        {"nome": "Batman: O Cavaleiro das Trevas", "duracao": "2h 32min", "imagem": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"},
        {"nome": "Pantera Negra", "duracao": "2h 14min", "imagem": "https://image.tmdb.org/t/p/w500/uxzzxijgPIY7slzFvMotPv8wjKA.jpg"},
        {"nome": "Vingadores: Ultimato", "duracao": "3h 1min", "imagem": "https://image.tmdb.org/t/p/w500/or06FN3Dka5tukK1e9sl16pB3iy.jpg"}
    ],
    "Comédia": [
        {"nome": "Se Beber, Não Case", "duracao": "1h 40min", "imagem": "https://image.tmdb.org/t/p/w500/uluhlXubGu1VxU63X9VHCLWDAYP.jpg"},
        {"nome": "Gente Grande", "duracao": "1h 42min", "imagem": "https://image.tmdb.org/t/p/w500/tmQKjHcZcR3pPpQ3h3zX5i7z3vV.jpg"},
        {"nome": "Todo Mundo em Pânico", "duracao": "1h 28min", "imagem": "https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg"},
        {"nome": "Esposa de Mentirinha", "duracao": "1h 56min", "imagem": "https://image.tmdb.org/t/p/w500/e4fZ1sRkQn8g4w5zW0fvkYlCYwY.jpg"}
    ],
    "Romance": [
        {"nome": "Titanic", "duracao": "3h 14min", "imagem": "https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg"},
        {"nome": "Diário de uma Paixão", "duracao": "2h 3min", "imagem": "https://image.tmdb.org/t/p/w500/qom1SZSENdmHFNZBXbtJAU0WTlC.jpg"},
        {"nome": "A Culpa é das Estrelas", "duracao": "2h 6min", "imagem": "https://image.tmdb.org/t/p/w500/iB6GM6I2GJH0Zx8F6K5j3YF5d4E.jpg"},
        {"nome": "La La Land", "duracao": "2h 8min", "imagem": "https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg"}
    ],
    "Terror": [
        {"nome": "Invocação do Mal", "duracao": "1h 52min", "imagem": "https://image.tmdb.org/t/p/w500/wVYREutTvI2tmxr6ujrHT704wGF.jpg"},
        {"nome": "Hereditário", "duracao": "2h 7min", "imagem": "https://image.tmdb.org/t/p/w500/lHV8HHlhwNup2VbpiACtlKzaGIQ.jpg"},
        {"nome": "O Exorcista", "duracao": "2h 2min", "imagem": "https://image.tmdb.org/t/p/w500/4ucLGcXVVSVnsfkGtbLY4XAius8.jpg"},
        {"nome": "Corra!", "duracao": "1h 44min", "imagem": "https://image.tmdb.org/t/p/w500/tFXcEccSQMf3lfhfXKSU9iRBpa3.jpg"}
    ],
    "Animação": [
        {"nome": "Shrek", "duracao": "1h 30min", "imagem": "https://image.tmdb.org/t/p/w500/iB64vpL3dIObOtMZgX3RqdVdQDc.jpg"},
        {"nome": "Toy Story", "duracao": "1h 21min", "imagem": "https://image.tmdb.org/t/p/w500/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg"},
        {"nome": "Frozen", "duracao": "1h 42min", "imagem": "https://image.tmdb.org/t/p/w500/kgwjIb2JDHRhNk13lmSxiClFjVk.jpg"},
        {"nome": "Divertida Mente", "duracao": "1h 35min", "imagem": "https://image.tmdb.org/t/p/w500/2H1TmgdfNtsKlU9jKdeNyYL5y8T.jpg"}
    ]
}

genero = st.selectbox("Escolha um gênero:", list(filmes.keys()))

if "fila" not in st.session_state:
    st.session_state.fila = []

def carregar():
    lista = filmes[genero].copy()
    random.shuffle(lista)
    return lista

if st.button("Começar 🎬"):
    st.session_state.fila = carregar()

if st.session_state.fila:
    filme = st.session_state.fila[0]

    st.write(f"🎬 {filme['nome']} — ⏱️ {filme['duracao']}")
    st.image(filme["imagem"], width=250)

    if st.button("Não gostei, mostrar outro 🔄"):
        st.session_state.fila.pop(0)

        if not st.session_state.fila:
            st.warning("Acabaram os filmes desse gênero!")
        else:
            st.rerun()
