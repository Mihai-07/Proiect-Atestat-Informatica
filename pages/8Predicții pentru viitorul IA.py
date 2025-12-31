import streamlit as st
from pathlib import Path
from PIL import Image

# Configurare pagină
st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    /* Header transparent și fără fundal */
    header[data-testid="stHeader"] {
        background: rgba(0,0,0,0); /* complet transparent */
        height: 50px;
        padding: 0;
        margin: 0;
        border: none;
    }

    /* Ascunde elementele inutile din header, dar păstrează toggle sidebar */
    header[data-testid="stHeader"] div:nth-child(1) > div:nth-child(2),
    header[data-testid="stHeader"] div:nth-child(1) > div:nth-child(3) {
        display: none;
    }

    /* Footer complet ascuns */
    footer[data-testid="stFooter"] {
        display: none;
    }

    /* Font și paragrafe compatibile cu restul paginilor */
    .stMarkdown p {
        font-size: 1.5rem;
        margin-bottom: 2.5rem;
    }

    /* Optional: aplicați același liquid glass și pe dataframe dacă e nevoie */
    .stDataFrameContainer {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(5px);
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Cale absolută pentru imagine
BASE_DIR = Path(__file__).resolve().parent.parent
img_path = BASE_DIR / "images" / "future.png"
img = Image.open(img_path)

# Sidebar glass morphism
with open("liquid_glass_sidebar.html", "r") as file:
    css_liquid_sidebar = file.read()

st.markdown(
    body=css_liquid_sidebar,
    unsafe_allow_html=True
)

# Fundal + FADE-IN GLOBAL
st.markdown(
    """
    <style>
    /* Fundal */
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                          url("https://img.freepik.com/free-vector/gradient-speed-motion-background_52683-63639.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
        font-family: 'Inter', sans-serif;
    }

    /* FADE-IN global */
    .stApp > div {
        opacity: 0;
        animation: fadeUp 1.2s ease forwards;
        animation-delay: 0.3s;
    }

    /* Ajustări text */
    .stMarkdown p {
        font-size: 1.5rem;
        margin-bottom: 2.5rem;
    }

    /* Border-radius pentru imagini */
    .stImage img {
        border-radius: 20px;
    }

    @keyframes fadeUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titlu
title = "8. Predicții pentru viitorul IA"
st.title(title)

# Coloane
col1, col2 = st.columns((1, 1))

# Paragrafe
p1 = """Viitorul **inteligenței artificiale** promite o integrare tot mai profundă între oameni și
mașini. Modelele vor deveni mai eficiente energetic, vor învăța cu mai puține date și vor
combina capabilități multimodale, procesând simultan text, imagini și sunet. Agenții
inteligenți vor putea acționa autonom în diverse domenii, sprijinind luarea deciziilor,
cercetarea și creația artistică."""

p2 = """Totuși, dezvoltarea rapidă a **IA** ridică provocări etice și de
confidențialitate, necesitatea reglementării și asigurarea unui control adecvat. Adaptarea
forței de muncă și educația continuă vor fi esențiale."""

p3 = """În ansamblu, **IA** va continua să transforme societatea, tehnologia și economia, 
iar evoluția sa responsabilă va determina modul în care oamenii și sistemele 
inteligente vor coexista în viitor."""

with col1:
    st.markdown(p1)
    st.markdown(p2)

with col2:
    st.image(img)

# Ultimul paragraf după coloane
st.markdown(p3)
