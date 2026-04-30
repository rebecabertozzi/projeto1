import streamlit as st
import random

st.set_page_config(
    page_title="Recomendador de Filmes 🎬",
    page_icon="🎥",
    layout="centered"
)

st.title("🎬 Recomendador de Filmes")
st.write("Escolha um gênero e descubra o que assistir!")

filmes = {
    "Ação": [
        {"nome": "Mad Max: Estrada da Fúria", "duracao": "2h", "imagem": "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg"},
        {"nome": "John Wick", "duracao": "1h 41min", "imagem": "https://upload.wikimedia.org/wikipedia/en/9/98/John_Wick_TeaserPoster.jpg"},
        {"nome": "Gladiador", "duracao": "2h 35min", "imagem": "https://upload.wikimedia.org/wikipedia/en/8/8d/Gladiator_ver1.jpg"},
        {"nome": "Batman: O Cavaleiro das Trevas", "duracao": "2h 32min", "imagem": "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg"},
        {"nome": "Pantera Negra", "duracao": "2h 14min", "imagem": "https://upload.wikimedia.org/wikipedia/en/d/d6/Black_Panther_%28film%29_poster.jpg"},
        {"nome": "Homem-Aranha: Sem Volta Para Casa", "duracao": "2h 28min", "imagem": "https://upload.wikimedia.org/wikipedia/en/0/00/Spider-Man_No_Way_Home_poster.jpg"}
    ],
    "Comédia": [
        {"nome": "As Branquelas", "duracao": "1h 49min", "imagem": "https://upload.wikimedia.org/wikipedia/en/3/3b/White_Chicks_poster.jpg"},
        {"nome": "Se Beber, Não Case", "duracao": "1h 40min", "imagem": "https://upload.wikimedia.org/wikipedia/en/b/b9/Hangoverposter09.jpg"},
        {"nome": "Gente Grande", "duracao": "1h 42min", "imagem": "https://upload.wikimedia.org/wikipedia/en/3/30/Grown_ups_poster.jpg"},
        {"nome": "Todo Mundo em Pânico", "duracao": "1h 28min", "imagem": "https://upload.wikimedia.org/wikipedia/en/6/6c/Scary_movie.jpg"},
        {"nome": "Click", "duracao": "1h 47min", "imagem": "https://upload.wikimedia.org/wikipedia/en/7/7f/Click_film.jpg"},
        {"nome": "Debi & Lóide", "duracao": "1h 47min", "imagem": "https://upload.wikimedia.org/wikipedia/en/6/64/Dumbanddumber.jpg"}
    ],
    "Romance": [
        {"nome": "Titanic", "duracao": "3h 14min", "imagem": "https://upload.wikimedia.org/wikipedia/en/2/22/Titanic_poster.jpg"},
        {"nome": "Diário de uma Paixão", "duracao": "2h 3min", "imagem": "https://upload.wikimedia.org/wikipedia/en/8/86/Posternotebook.jpg"},
        {"nome": "Como Eu Era Antes de Você", "duracao": "1h 50min", "imagem": "https://upload.wikimedia.org/wikipedia/en/0/0b/Me_Before_You_%28film%29.jpg"},
        {"nome": "A Culpa é das Estrelas", "duracao": "2h 6min", "imagem": "https://upload.wikimedia.org/wikipedia/en/4/41/The_Fault_in_Our_Stars_%282014%29.jpg"},
        {"nome": "Simplesmente Acontece", "duracao": "1h 42min", "imagem": "https://upload.wikimedia.org/wikipedia/en/1/1c/Love%2C_Rosie_poster.jpg"},
        {"nome": "La La Land", "duracao": "2h 8min", "imagem": "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png"}
    ],
    "Terror": [
        {"nome": "Invocação do Mal", "duracao": "1h 52min", "imagem": "https://upload.wikimedia.org/wikipedia/en/1/1f/Conjuring_poster.jpg"},
        {"nome": "Hereditário", "duracao": "2h 7min", "imagem": "https://upload.wikimedia.org/wikipedia/en/d/d9/Hereditary.png"},
        {"nome": "O Exorcista", "duracao": "2h 2min", "imagem": "https://upload.wikimedia.org/wikipedia/en/7/7b/Exorcist_ver2.jpg"},
        {"nome": "It: A Coisa", "duracao": "2h 15min", "imagem": "https://upload.wikimedia.org/wikipedia/en/5/5a/It_%282017%29_poster.jpg"},
        {"nome": "Annabelle", "duracao": "1h 39min", "imagem": "https://upload.wikimedia.org/wikipedia/en/9/9b/Annabelle_poster.jpg"},
        {"nome": "Corra!", "duracao": "1h 44min", "imagem": "https://upload.wikimedia.org/wikipedia/en/a/a3/Get_Out_poster.png"}
    ],
    "Animação": [
        {"nome": "Shrek", "duracao": "1h 30min", "imagem": "https://upload.wikimedia.org/wikipedia/en/4/4d/Shrek_%28film%29_poster.jpg"},
        {"nome": "Toy Story", "duracao": "1h 21min", "imagem": "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"},
        {"nome": "Frozen", "duracao": "1h 42min", "imagem": "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg"},
        {"nome": "Divertida Mente", "duracao": "1h 35min", "imagem": "https://upload.wikimedia.org/wikipedia/en/f/f7/Inside_Out_%282015_film%29_poster.jpg"},
        {"nome": "Up: Altas Aventuras", "duracao": "1h 36min", "imagem": "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg"},
        {"nome": "Ratatouille", "duracao": "1h 51min", "imagem": "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg"}
    ]
}

genero = st.selectbox("Escolha um gênero:", list(filmes.keys()))

if "recomendacoes" not in st.session_state:
    st.session_state.recomendacoes = []

if st.button("Recomendar 🎥"):
    st.session_state.recomendacoes = random.sample(filmes[genero], 3)

if st.session_state.recomendacoes:
    st.subheader("🍿 Sugestões para você:")

    for filme in st.session_state.recomendacoes:
        nome = filme["nome"]
        duracao = filme["duracao"]
        imagem = filme["imagem"]

        st.write(f"🎬 {nome} — ⏱️ {duracao}")
        st.image(imagem)

    if st.button("Não gostei, tentar de novo 🔄"):
        st.session_state.recomendacoes = random.sample(filmes[genero], 3)
        st.rerun()
