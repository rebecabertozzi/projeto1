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
        {"nome": "Gladiador", "duracao": "2h 35min", "imagem": "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg"},
        {"nome": "Batman: O Cavaleiro das Trevas", "duracao": "2h 32min", "imagem": "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg"},
        {"nome": "Pantera Negra", "duracao": "2h 14min", "imagem": "https://upload.wikimedia.org/wikipedia/en/d/d6/Black_Panther_%28film%29_poster.jpg"},
        {"nome": "Vingadores: Ultimato", "duracao": "3h 1min", "imagem": "https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg"}
    ],
    "Comédia": [
        {"nome": "Se Beber, Não Case", "duracao": "1h 40min", "imagem": "https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg"},
        {"nome": "Todo Mundo em Pânico", "duracao": "1h 28min", "imagem": "https://upload.wikimedia.org/wikipedia/en/6/6c/Scary_movie.jpg"},
        {"nome": "Meninas Malvadas", "duracao": "1h 37min", "imagem": "https://upload.wikimedia.org/wikipedia/en/a/ac/Mean_Girls_film_poster.png"},
        {"nome": "Superbad", "duracao": "1h 53min", "imagem": "https://upload.wikimedia.org/wikipedia/en/8/8b/Superbad_Poster.png"}
    ],
    "Romance": [
        {"nome": "Titanic", "duracao": "3h 14min", "imagem": "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg"},
        {"nome": "Diário de uma Paixão", "duracao": "2h 3min", "imagem": "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg"},
        {"nome": "Simplesmente Acontece", "duracao": "1h 42min", "imagem": "https://upload.wikimedia.org/wikipedia/en/1/1c/Love%2C_Rosie_poster.jpg"},
        {"nome": "La La Land", "duracao": "2h 8min", "imagem": "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png"}
    ],
    "Terror": [
        {"nome": "Invocação do Mal", "duracao": "1h 52min", "imagem": "https://upload.wikimedia.org/wikipedia/en/1/1f/Conjuring_poster.jpg"},
        {"nome": "Hereditário", "duracao": "2h 7min", "imagem": "https://upload.wikimedia.org/wikipedia/en/d/d9/Hereditary.png"},
        {"nome": "O Exorcista", "duracao": "2h 2min", "imagem": "https://upload.wikimedia.org/wikipedia/en/7/7b/Exorcist_ver2.jpg"},
        {"nome": "It: A Coisa", "duracao": "2h 15min", "imagem": "https://upload.wikimedia.org/wikipedia/en/5/5a/It_%282017%29_poster.jpg"}
    ],
    "Animação": [
        {"nome": "Shrek", "duracao": "1h 30min", "imagem": "https://upload.wikimedia.org/wikipedia/en/4/4d/Shrek_%28film%29_poster.jpg"},
        {"nome": "Toy Story", "duracao": "1h 21min", "imagem": "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"},
        {"nome": "Frozen", "duracao": "1h 42min", "imagem": "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg"},
        {"nome": "Divertida Mente", "duracao": "1h 35min", "imagem": "https://upload.wikimedia.org/wikipedia/en/f/f7/Inside_Out_%282015_film%29_poster.jpg"}
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
