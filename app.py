import streamlit as st
import random

# Configuração da página (o professor pediu)
st.set_page_config(
    page_title="Recomendador de Filmes 🎬",
    page_icon="🎥",
    layout="centered"
)

st.title("🎬 Recomendador de Filmes")
st.write("Escolha um gênero e receba sugestões com duração!")

# Lista de filmes com duração
filmes = {
    "Ação": [
        {"nome": "Mad Max: Estrada da Fúria", "duracao": "2h"},
        {"nome": "John Wick", "duracao": "1h 41min"},
        {"nome": "Velozes e Furiosos", "duracao": "1h 47min"},
        {"nome": "Missão Impossível", "duracao": "1h 50min"},
        {"nome": "Gladiador", "duracao": "2h 35min"},
        {"nome": "Batman: O Cavaleiro das Trevas", "duracao": "2h 32min"},
        {"nome": "Homem-Aranha: Sem Volta Para Casa", "duracao": "2h 28min"}
    ],
    "Comédia": [
        {"nome": "As Branquelas", "duracao": "1h 49min"},
        {"nome": "Se Beber, Não Case", "duracao": "1h 40min"},
        {"nome": "Gente Grande", "duracao": "1h 42min"},
        {"nome": "Todo Mundo em Pânico", "duracao": "1h 28min"},
        {"nome": "Superbad", "duracao": "1h 53min"},
        {"nome": "Click", "duracao": "1h 47min"},
        {"nome": "Debi & Lóide", "duracao": "1h 47min"}
    ],
    "Romance": [
        {"nome": "Diário de uma Paixão", "duracao": "2h 3min"},
        {"nome": "Como Eu Era Antes de Você", "duracao": "1h 50min"},
        {"nome": "A Culpa é das Estrelas", "duracao": "2h 6min"},
        {"nome": "Simplesmente Acontece", "duracao": "1h 42min"},
        {"nome": "Titanic", "duracao": "3h 14min"},
        {"nome": "Orgulho e Preconceito", "duracao": "2h 9min"},
        {"nome": "Para Todos os Garotos que Já Amei", "duracao": "1h 39min"}
    ],
    "Terror": [
        {"nome": "Invocação do Mal", "duracao": "1h 52min"},
        {"nome": "Hereditário", "duracao": "2h 7min"},
        {"nome": "O Exorcista", "duracao": "2h 2min"},
        {"nome": "Atividade Paranormal", "duracao": "1h 26min"},
        {"nome": "It: A Coisa", "duracao": "2h 15min"},
        {"nome": "A Freira", "duracao": "1h 36min"},
        {"nome": "O Iluminado", "duracao": "2h 26min"}
    ],
    "Animação": [
        {"nome": "Toy Story", "duracao": "1h 21min"},
        {"nome": "Shrek", "duracao": "1h 30min"},
        {"nome": "Frozen", "duracao": "1h 42min"},
        {"nome": "Procurando Nemo", "duracao": "1h 40min"},
        {"nome": "Divertida Mente", "duracao": "1h 35min"},
        {"nome": "Os Incríveis", "duracao": "1h 55min"},
        {"nome": "Up: Altas Aventuras", "duracao": "1h 36min"}
    ],
    "Ficção Científica": [
        {"nome": "Interestelar", "duracao": "2h 49min"},
        {"nome": "Matrix", "duracao": "2h 16min"},
        {"nome": "Star Wars", "duracao": "2h 1min"},
        {"nome": "De Volta para o Futuro", "duracao": "1h 56min"},
        {"nome": "Blade Runner", "duracao": "1h 57min"},
        {"nome": "Avatar", "duracao": "2h 42min"},
        {"nome": "Duna", "duracao": "2h 35min"}
    ]
}

# Escolher gênero
genero = st.selectbox("Escolha um gênero:", list(filmes.keys()))

# Botão de recomendação
if st.button("Recomendar filmes 🎥"):
    recomendacoes = random.sample(filmes[genero], 3)

    st.subheader("🍿 Sugestões para você:")
    for filme in recomendacoes:
        st.write(f"🎬 {filme['nome']} — ⏱️ {filme['duracao']}")

    st.info("Perfeito para escolher algo pra assistir hoje 🍿")
