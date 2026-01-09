import streamlit as st

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

    /* FADE-IN GLOBAL – IDENTIC */
    .stApp > div {
        opacity: 0;
        animation: fadeUp 1.2s ease forwards;
        animation-delay: 0.3s;
    }

    /* Text */
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
st.title("Argumentarea Temei")

# Coloane
col1, col2 = st.columns((1, 1))

# Conținut
p1 = """
**Inteligența Artificială** (IA) reprezintă una dintre cele mai importante inovații ale
epocii moderne, influențând modul în care oamenii trăiesc, lucrează și comunică.
"""

p2 = """
Alegerea acestei teme este motivată de importanța crescândă a IA și de ritmul accelerat
al dezvoltării sale, de la modelele simbolice din anii 1950 până la agenții inteligenți actuali.
"""

p3 = """
Lucrarea urmărește prezentarea etapelor esențiale ale evoluției IA, precum și impactul
său asupra pieței muncii și a societății în ansamblu. Totodată, proiectul evidențiază
beneficiile și provocările automatizării, oferind o perspectivă echilibrată asupra
modului în care IA transformă lumea contemporană și contribuie la progresul tehnologic global.
"""

with col1:
    st.markdown(p1)
    st.markdown(p2)

# Animație 3D – semn de întrebare
question_mark = """
<style>
.question-container {
    width: 320px;
    height: 320px;
    perspective: 1200px;
    margin: auto;
}
.question-mark {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14rem;
    font-weight: 800;
    color: white;
    transform-style: preserve-3d;
    animation: spinYReverse 8s linear infinite;
    text-shadow:
        0 0 14px rgba(255,255,255,0.35),
        0 0 34px rgba(120,180,255,0.55);
}
@keyframes spinYReverse {
    from { transform: rotateY(360deg); }
    to   { transform: rotateY(0deg); }
}
</style>

<div class="question-container">
    <div class="question-mark">?</div>
</div>
"""

with col2:
    st.markdown(question_mark, unsafe_allow_html=True)

st.markdown(p3)
