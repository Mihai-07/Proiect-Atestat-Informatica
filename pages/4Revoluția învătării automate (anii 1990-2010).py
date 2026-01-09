import streamlit as st
from pathlib import Path
from PIL import Image

# Cale absolută pentru imagine
BASE_DIR = Path(__file__).resolve().parent.parent
img_path = BASE_DIR / "images" / "ml.png"
img = Image.open(img_path)

# Sidebar glass morphism - cached pentru a evita flickering
@st.cache_data
def load_sidebar_html():
    with open("liquid_glass_sidebar.html", "r") as file:
        return file.read()

# CSS pentru header/footer - cached pentru a evita flickering
@st.cache_data
def get_header_footer_css():
    return """
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
    """

# CSS pentru background - cached pentru a evita flickering
@st.cache_data
def get_background_css():
    return """
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

    /* FADE-IN global pentru tot conținutul */
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
    """

css_liquid_sidebar = load_sidebar_html()
css_header_footer = get_header_footer_css()
css_background = get_background_css()

st.set_page_config(layout="wide")

st.markdown(css_header_footer, unsafe_allow_html=True)
st.markdown(body=css_liquid_sidebar, unsafe_allow_html=True)
st.markdown(css_background, unsafe_allow_html=True)

# Titlu
title = "4. Revoluția învătării automate (anii 1990-2010)"
st.title(title)

# Paragrafe
p1 = """
Anii 1990–2010 au marcat tranziția IA către metode bazate pe date, cunoscută sub
denumirea de **învățare automată (machine learning)**. În locul regulilor fixe, algoritmii au
început să învețe direct din informații, identificând modele și tipare complexe.
"""

p2 = """
Rețelele neuronale, mașinile cu suport vectorial și modelele bayesiene au devenit instrumente
esențiale în recunoașterea imaginilor, analiza datelor și procesarea limbajului natural.
"""

p3 = """
Dezvoltarea puternică a calculatoarelor și creșterea volumului de date disponibile au
permis antrenarea modelelor mai complexe și obținerea unor performanțe superioare.
Această perioadă a demonstrat că IA poate fi adaptabilă și scalabilă, pregătind terenul
pentru revoluția rețelelor neuronale profunde și apariția sistemelor capabile să învețe și să
generalizeze în mod autonom.
"""

# Coloane
col1, col2 = st.columns((1, 1))

with col1:
    st.markdown(p1)
    st.markdown(p2)
    st.markdown(p3)

with col2:
    st.image(img)
