import streamlit as st
from groq import Groq
import pandas as pd
from PIL import Image
import json
import io
import base64
import random

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

# ─────────────────────────────────────────────
# Configuração da página
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Gerador Inteligente de Legendas",
    page_icon="#",
    layout="centered",
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Inter:wght@400;500;600&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(180deg, #E9F7F0 0%, #F3FBF7 30%, #FFFFFF 70%);
    }

    /* ── Header do app (logo + titulo) ── */
    .app-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 0.3rem;
    }
    .app-logo {
        width: 42px;
        height: 42px;
        border-radius: 12px;
        background: linear-gradient(135deg, #7FD8A0, #5FAE82);
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'Poppins', sans-serif;
        font-weight: 800;
        font-size: 1.3rem;
        color: white;
        flex-shrink: 0;
    }
    .app-header-text {
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 1.05rem;
        color: #1E2A24;
        line-height: 1.25;
    }

    .main-title {
        font-family: 'Poppins', sans-serif;
        font-size: 2.1rem;
        font-weight: 800;
        margin: 1.2rem 0 0.3rem 0;
        color: #1E2A24;
        line-height: 1.2;
    }
    .main-title .accent {
        color: #5FAE82;
    }
    .subtitle {
        color: #6B8077;
        font-size: 0.98rem;
        margin-bottom: 1.6rem;
        line-height: 1.5;
    }

    /* ── Barra de passos numerados ── */
    .steps-bar {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0;
        margin: 0.5rem 0 2rem 0;
    }
    .step-item {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 6px;
    }
    .step-circle {
        width: 34px;
        height: 34px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 0.9rem;
        color: white;
        background: #C9E8D6;
    }
    .step-circle.active {
        background: linear-gradient(135deg, #7FD8A0, #5FAE82);
        box-shadow: 0 3px 10px rgba(95, 174, 130, 0.4);
    }
    .step-label {
        font-size: 0.72rem;
        font-weight: 600;
        color: #8FA89B;
    }
    .step-label.active {
        color: #2F8F5C;
    }
    .step-line {
        width: 60px;
        height: 2px;
        background: #C9E8D6;
        margin: 0 6px;
        margin-bottom: 22px;
    }

    .hashtag-pill {
        display: inline-block;
        background: #E3F5EA;
        color: #2F8F5C;
        font-size: 0.8rem;
        font-weight: 600;
        padding: 4px 14px;
        border-radius: 99px;
        margin: 3px;
        border: 1px solid #CDEBDA;
    }
    .step-header {
        font-family: 'Poppins', sans-serif;
        font-size: 1.05rem;
        font-weight: 700;
        color: #1E2A24;
        margin-bottom: 0.2rem;
    }
    .step-subtext {
        font-size: 0.85rem;
        color: #8FA89B;
        margin-bottom: 1.1rem;
    }

    .post-preview-card {
        background: #fff;
        border: 1px solid #DDF0E4;
        border-radius: 16px;
        overflow: hidden;
        max-width: 400px;
        margin: 0 auto 1.5rem auto;
        box-shadow: 0 4px 18px rgba(95, 174, 130, 0.12);
    }
    .post-preview-header {
        display: flex;
        align-items: center;
        gap: 10px;
        padding: 10px 14px;
        border-bottom: 1px solid #F0FAF4;
    }
    .post-avatar {
        width: 32px;
        height: 32px;
        border-radius: 50%;
        background: linear-gradient(135deg, #7FD8A0, #6FA8F0);
    }
    .post-username {
        font-weight: 600;
        font-size: 0.85rem;
        color: #1E2A24;
    }
    .post-preview-image {
        width: 100%;
        aspect-ratio: 1;
        object-fit: cover;
        display: block;
    }
    .post-preview-caption {
        padding: 12px 14px;
        font-size: 0.85rem;
        line-height: 1.5;
        color: #1E2A24;
        border-top: 1px solid #F0FAF4;
    }
    .post-preview-caption b {
        font-weight: 600;
    }
    .post-preview-hashtags {
        padding: 0 14px 12px;
        font-size: 0.8rem;
        color: #2F8F5C;
    }

    /* Cards de secao */
    .section-card {
        background: #FFFFFF;
        border: 1px solid #E3F5EA;
        border-radius: 20px;
        padding: 1.5rem 1.6rem;
        margin-bottom: 1.2rem;
        box-shadow: 0 2px 14px rgba(95, 174, 130, 0.08);
    }

    /* ── Cards numerados de legenda (estilo prototipo) ── */
    .legenda-card {
        display: flex;
        align-items: flex-start;
        gap: 14px;
        background: #F7FCF9;
        border: 1px solid #E3F5EA;
        border-radius: 14px;
        padding: 1rem 1.1rem;
        margin-bottom: 0.9rem;
    }
    .legenda-numero {
        width: 32px;
        height: 32px;
        min-width: 32px;
        border-radius: 9px;
        background: linear-gradient(135deg, #7FD8A0, #5FAE82);
        color: white;
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        font-size: 0.85rem;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .legenda-conteudo {
        flex: 1;
    }
    .legenda-estilo-tag {
        font-size: 0.7rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #5FAE82;
        margin-bottom: 4px;
    }
    .legenda-texto-preview {
        font-size: 0.88rem;
        color: #1E2A24;
        line-height: 1.5;
    }

    /* Botoes primarios */
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #7FD8A0, #5FAE82);
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: 700;
        padding: 0.6rem 1rem;
        box-shadow: 0 4px 12px rgba(95, 174, 130, 0.35);
        transition: transform 0.15s ease;
    }
    div.stButton > button[kind="primary"]:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 16px rgba(95, 174, 130, 0.45);
    }

    /* Botoes secundarios — azul claro */
    div.stButton > button[kind="secondary"] {
        background: #FFFFFF;
        color: #3D6FD1;
        border: 1.5px solid #A8C5F0;
        border-radius: 12px;
        font-weight: 600;
        padding: 0.6rem 1rem;
        transition: all 0.15s ease;
    }
    div.stButton > button[kind="secondary"]:hover {
        background: #EEF4FE;
        border-color: #6FA8F0;
    }

    div[data-baseweb="select"] > div {
        border-radius: 10px !important;
        border-color: #DDF0E4 !important;
    }
    textarea {
        border-radius: 10px !important;
    }

    section[data-testid="stFileUploaderDropzone"] {
        background: #F4FBF8;
        border: 2px dashed #A8E6C5;
        border-radius: 14px;
    }

    div[data-testid="stExpander"] {
        border: 1px solid #E3F5EA !important;
        border-radius: 14px !important;
        box-shadow: 0 2px 10px rgba(95, 174, 130, 0.06);
    }

    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #E3F5EA 0%, #F4FBF8 100%);
    }
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Sidebar
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("### # Gerador Inteligente de Legendas")
    st.markdown("---")
    st.markdown("**Como usar:**")
    st.markdown("1. Envie uma imagem (opcional)")
    st.markdown("2. Responda o questionario")
    st.markdown("3. Clique em **Gerar Legendas**")
    st.markdown("4. Copie a legenda favorita!")
    st.markdown("---")
    st.markdown("*Feito com Streamlit + Groq*")


# ─────────────────────────────────────────────
# Inicializar session_state
# ─────────────────────────────────────────────
if "resultado" not in st.session_state:
    st.session_state.resultado = None
if "image_b64" not in st.session_state:
    st.session_state.image_b64 = None
if "params" not in st.session_state:
    st.session_state.params = None
if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0


# ─────────────────────────────────────────────
# Header (logo + nome do app)
# ─────────────────────────────────────────────
st.markdown("""
<div class="app-header">
    <div class="app-logo">#</div>
    <div class="app-header-text">Gerador Inteligente<br/>de Legendas</div>
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Barra de passos numerados
# ─────────────────────────────────────────────
etapa_atual = 3 if st.session_state.resultado else 2

def step_circle(numero, label, ativo):
    classe_circulo = "step-circle active" if ativo else "step-circle"
    classe_label = "step-label active" if ativo else "step-label"
    return f"""
    <div class="step-item">
        <div class="{classe_circulo}">{numero}</div>
        <div class="{classe_label}">{label}</div>
    </div>
    """

st.markdown(f"""
<div class="steps-bar">
    {step_circle(1, "Imagem", True)}
    <div class="step-line"></div>
    {step_circle(2, "Quiz", etapa_atual >= 2)}
    <div class="step-line"></div>
    {step_circle(3, "Resultado", etapa_atual >= 3)}
</div>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Título
# ─────────────────────────────────────────────
st.markdown('<p class="main-title">Crie legendas <span class="accent">incriveis</span> para suas redes sociais com IA</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Envie uma imagem, responda algumas perguntas e receba sugestoes de legendas personalizadas para o seu conteudo.</p>', unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Passo 1 — Upload de imagem
# ─────────────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<p class="step-header">Envie a imagem do seu post</p>', unsafe_allow_html=True)
st.markdown('<p class="step-subtext">Arraste e solte sua imagem aqui ou clique para selecionar</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "Imagem do post (opcional)",
    type=["jpg", "jpeg", "png", "webp"],
    label_visibility="collapsed",
    key=f"uploader_{st.session_state.uploader_key}"
)

image_b64 = None

if uploaded_file:
    image_obj = Image.open(uploaded_file)
    st.image(image_obj, caption="Imagem carregada", use_column_width=True)
    buf = io.BytesIO()
    image_obj.save(buf, format="PNG")
    image_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")
    st.session_state.image_b64 = image_b64
st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Passo 2 — Quiz
# ─────────────────────────────────────────────
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown('<p class="step-header">Responda algumas perguntas</p>', unsafe_allow_html=True)
st.markdown('<p class="step-subtext">Isso vai nos ajudar a criar legendas perfeitas para voce!</p>', unsafe_allow_html=True)

objetivo = st.selectbox(
    "Qual o objetivo da publicacao?",
    options=[
        "Vender ou promover um produto/servico",
        "Engajar e interagir com a audiencia",
        "Educar ou informar o publico",
        "Inspirar e motivar",
    ]
)

tom = st.selectbox(
    "Qual o estilo da legenda?",
    options=[
        "Engracado e descontraido",
        "Profissional e formal",
        "Motivacional e inspirador",
        "Casual e amigavel",
    ]
)

publico = st.selectbox(
    "Qual e o seu publico-alvo?",
    options=[
        "Jovens (18-25 anos)",
        "Adultos (26-40 anos)",
        "Empreendedores e profissionais",
        "Publico geral",
    ]
)

rede_social = st.selectbox(
    "Para qual rede social?",
    options=["Instagram", "TikTok", "LinkedIn", "Twitter/X"]
)

contexto = st.text_area(
    "Contexto extra (opcional)",
    placeholder="Ex: lancamento de produto, promocao de fim de semana, dia do cliente...",
    height=90,
)
st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Funções auxiliares
# ─────────────────────────────────────────────
def render_post_preview(legenda_texto, hashtags, image_b64=None, username="seu_perfil"):
    hashtags_str = " ".join(hashtags) if hashtags else ""
    if image_b64:
        img_html = f'<img class="post-preview-image" src="data:image/png;base64,{image_b64}" />'
    else:
        img_html = '<div style="width:100%;aspect-ratio:1;background:linear-gradient(135deg,#E3F5EA,#A8E6C5);display:flex;align-items:center;justify-content:center;font-size:1.2rem;color:#5FAE82;">sem imagem</div>'

    st.markdown(f"""
    <div class="post-preview-card">
        <div class="post-preview-header">
            <div class="post-avatar"></div>
            <span class="post-username">{username}</span>
        </div>
        {img_html}
        <div class="post-preview-caption">
            <b>{username}</b> {legenda_texto}
        </div>
        <div class="post-preview-hashtags">{hashtags_str}</div>
    </div>
    """, unsafe_allow_html=True)


ESTILOS = [
    ("Direto ao ponto", "Uma frase curta e impactante, sem rodeios. Va direto ao beneficio ou mensagem principal."),
    ("Storytelling", "Conte uma mini historia ou situacao do dia a dia que conecte com o publico antes de chegar na mensagem."),
    ("Engajamento", "Termine com uma pergunta ou chamada para acao que incentive comentarios e interacao."),
    ("Humor", "Use leveza, ironia ou uma virada de expectativa para fazer o publico sorrir."),
    ("Prova social", "Mencione resultados, numeros, depoimentos ou situacoes que gerem credibilidade."),
    ("Curiosidade", "Comece com uma afirmacao surpreendente ou pergunta que faca o usuario querer ler mais."),
]


def gerar_legendas(objetivo, rede_social, tom, publico, contexto, image_b64, seed=None):
    estilos_escolhidos = random.sample(ESTILOS, 3)

    estilos_str = "\n".join(
        [f'- "{e[0]}": {e[1]}' for e in estilos_escolhidos]
    )

    prompt = f"""
Voce e um especialista em marketing digital e copywriting.

Crie 3 legendas para redes sociais, cada uma com um estilo completamente diferente das outras.
Use estruturas, comprimentos e abordagens distintas — nao repita padroes entre elas.

Objetivo: {objetivo}
Rede social: {rede_social}
Tom: {tom}
Publico-alvo: {publico}
Contexto: {contexto}
Variacao aleatoria (use para criar algo diferente): {seed}

Os 3 estilos que voce deve usar desta vez sao:
{estilos_str}

Retorne SOMENTE JSON valido, sem texto fora do JSON.

Formato:

{{
  "legendas": [
    {{
      "estilo": "{estilos_escolhidos[0][0]}",
      "texto": "Legenda aqui"
    }},
    {{
      "estilo": "{estilos_escolhidos[1][0]}",
      "texto": "Legenda aqui"
    }},
    {{
      "estilo": "{estilos_escolhidos[2][0]}",
      "texto": "Legenda aqui"
    }}
  ],
  "hashtags": [
    "#hashtag1",
    "#hashtag2",
    "#hashtag3",
    "#hashtag4",
    "#hashtag5",
    "#hashtag6"
  ]
}}
"""

    if image_b64:
        content = [
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/png;base64,{image_b64}"}
            },
            {
                "type": "text",
                "text": prompt
            }
        ]
        model = "meta-llama/llama-4-scout-17b-16e-instruct"
    else:
        content = prompt
        model = "llama-3.3-70b-versatile"

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": content}],
        temperature=0.99,
        max_tokens=1500,
        response_format={"type": "json_object"}
    )

    raw = response.choices[0].message.content

    try:
        return json.loads(raw)
    except Exception:
        st.write("Resposta recebida:")
        st.code(raw)
        raise


def exibir_resultados(resultado, image_b64):
    hashtags = resultado.get("hashtags", [])
    legendas = resultado.get("legendas", [])

    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    st.markdown('<p class="step-header">Suas legendas estao prontas!</p>', unsafe_allow_html=True)
    st.markdown('<p class="step-subtext">Confira as sugestoes criadas especialmente para voce.</p>', unsafe_allow_html=True)

    for i, leg in enumerate(legendas):
        numero = f"{i+1:02d}"
        st.markdown(f"""
        <div class="legenda-card">
            <div class="legenda-numero">{numero}</div>
            <div class="legenda-conteudo">
                <div class="legenda-estilo-tag">{leg['estilo']}</div>
                <div class="legenda-texto-preview">{leg['texto']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        with st.expander(f"Ver pre-visualizacao e copiar — opcao {numero}"):
            st.markdown("**Pre-visualizacao do post**")
            render_post_preview(leg["texto"], hashtags, image_b64)

            st.markdown("**Legenda completa**")
            legenda_completa = leg["texto"] + "\n\n" + " ".join(hashtags)
            st.text_area(
                label="",
                value=legenda_completa,
                height=130,
                key=f"legenda_{i}_{id(resultado)}",
                help="Selecione o texto e copie (Ctrl+A, Ctrl+C)"
            )
            st.caption("Ou use o botao de copia abaixo:")
            st.code(legenda_completa, language=None)

    if hashtags:
        st.markdown("---")
        st.markdown("**Hashtags sugeridas**")
        pills_html = "".join(
            f'<span class="hashtag-pill">{h}</span>' for h in hashtags
        )
        st.markdown(f'<div style="margin:0.5rem 0 1rem">{pills_html}</div>', unsafe_allow_html=True)
        st.code(" ".join(hashtags), language=None)

    st.markdown("---")
    st.markdown("**Historico desta geracao**")
    df = pd.DataFrame(legendas)
    df.insert(0, "Rede Social", rede_social)
    df.insert(1, "Tom", tom)
    df.insert(2, "Objetivo", objetivo)
    st.dataframe(df, use_container_width=True)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Baixar como CSV",
        data=csv,
        file_name="legendas_geradas.csv",
        mime="text/csv",
        key=f"csv_{id(resultado)}"
    )
    st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────
# Botao principal — Gerar Legendas
# ─────────────────────────────────────────────
if st.button("Gerar legendas", type="primary", use_container_width=True):
    with st.spinner("Gerando suas legendas com IA..."):
        try:
            resultado = gerar_legendas(
                objetivo, rede_social, tom, publico, contexto,
                image_b64, seed=random.randint(1, 99999)
            )
            st.session_state.resultado = resultado
            st.session_state.params = {
                "objetivo": objetivo,
                "rede_social": rede_social,
                "tom": tom,
                "publico": publico,
                "contexto": contexto,
            }
            st.rerun()
        except json.JSONDecodeError:
            st.error("Erro ao interpretar a resposta da IA. Tente novamente.")
        except Exception as e:
            st.error(f"Erro: {str(e)}")


# ─────────────────────────────────────────────
# Resultados + botoes pos-geracao
# ─────────────────────────────────────────────
if st.session_state.resultado:
    exibir_resultados(st.session_state.resultado, st.session_state.image_b64 or image_b64)

    col_novas, col_recomecar = st.columns([2, 1])

    with col_novas:
        if st.button("Gerar novas legendas", type="secondary", use_container_width=True):
            with st.spinner("Gerando novas legendas..."):
                try:
                    p = st.session_state.params
                    novo_resultado = gerar_legendas(
                        p["objetivo"], p["rede_social"], p["tom"],
                        p["publico"], p["contexto"],
                        st.session_state.image_b64,
                        seed=random.randint(1, 99999)
                    )
                    st.session_state.resultado = novo_resultado
                    st.rerun()
                except json.JSONDecodeError:
                    st.error("Erro ao interpretar a resposta da IA. Tente novamente.")
                except Exception as e:
                    st.error(f"Erro: {str(e)}")

    with col_recomecar:
        if st.button("Recomecar", type="secondary", use_container_width=True):
            st.session_state.resultado = None
            st.session_state.image_b64 = None
            st.session_state.params = None
            st.session_state.uploader_key += 1
            st.rerun()
