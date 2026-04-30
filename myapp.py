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
        {"nome": "John Wick", "duracao": "1h 41min", "imagem": "https://image.tmdb.org/t/p/w500/fZPSd91yGE9fCcCe6OoQr6E4VFb.jpg"},
        {"nome": "Gladiador", "duracao": "2h 35min", "imagem": "https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg"},
        {"nome": "Batman: O Cavaleiro das Trevas", "duracao": "2h 32min", "imagem": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"},
        {"nome": "Pantera Negra", "duracao": "2h 14min", "imagem": "https://image.tmdb.org/t/p/w500/uxzzxijgPIY7slzFvMotPv8wjKA.jpg"}
    ],
    "Comédia": [
        {"nome": "As Branquelas", "duracao": "1h 49min", "imagem": "https://image.tmdb.org/t/p/w500/7rhzEufovf6srsd2b5sW0kSxK0L.jpg"},
        {"nome": "Se Beber, Não Case", "duracao": "1h 40min", "imagem": "https://image.tmdb.org/t/p/w500/uluhlXubGu1VxU63X9VHCLWDAYP.jpg"},
        {"nome": "Click", "duracao": "1h 47min", "imagem": "https://image.tmdb.org/t/p/w500/5rL6dGZ0yW7h8TDIrS9KuX3sI5Y.jpg"},
        {"nome": "Debi & Lóide", "duracao": "1h 47min", "imagem": "https://image.tmdb.org/t/p/w500/9Qw7h8Q3n1C0n8u9W1R9mX4pQ8P.jpg"}
    ],
    "Romance": [
        {"nome": "Titanic", "duracao": "3h 14min", "imagem": "https://image.tmdb.org/t/p/w500/9xjZS2rlVxm8SFx8kPC3aIGCOYQ.jpg"},
        {"nome": "Diário de uma Paixão", "duracao": "2h 3min", "imagem": "https://image.tmdb.org/t/p/w500/qom1SZSENdmHFNZBXbtJAU0WTlC.jpg"},
        {"nome": "Como Eu Era Antes de Você", "duracao": "1h 50min", "imagem": "https://image.tmdb.org/t/p/w500/7qHO1eOz5bPlM6DgFZ0Q8h4J0zV.jpg"},
        {"nome": "La La Land", "duracao": "2h 8min", "imagem": "https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg"}
    ],
    "Terror": [
        {"nome": "Invocação do Mal", "duracao": "1h 52min", "imagem": "https://image.tmdb.org/t/p/w500/wVYREutTvI2tmxr6ujrHT704wGF.jpg"},
        {"nome": "Hereditário", "duracao": "2h 7min", "imagem": "https://image.tmdb.org/t/p/w500/lHV8HHlhwNup2VbpiACtlKzaGIQ.jpg"},
        {"nome": "O Exorcista", "duracao": "2h 2min", "imagem": "https://image.tmdb.org/t/p/w500/4ucLGcXVVSVnsfkGtbLY4XAius8.jpg"},
        {"nome": "It: A Coisa", "duracao": "2h 15min", "imagem": "https://image.tmdb.org/t/p/w500/9E2y5Q7WlCVNEhP5GiVTjhEhx1o.jpg"}
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

    try:
        st.image(filme["imagem"], width=250)
    except:
        st.image("https://via.placeholder.com/250x350?text=Imagem+indisponivel")

    if st.button("Não gostei, mostrar outro 🔄"):
        st.session_state.fila.pop(0)

        if not st.session_state.fila:
            st.warning("Acabaram os filmes desse gênero!")
        else:
            st.rerun()
