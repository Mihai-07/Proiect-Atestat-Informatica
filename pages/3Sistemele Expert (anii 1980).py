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
    /* Fundal full-page cu overlay */
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

    /* Stil paragrafe */
    .stMarkdown p {
        font-size: 1.5rem;
        margin-bottom: 2.5rem;
    }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(20px); }
        to   { opacity: 1; transform: translateY(0); }
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
title = "3. Sistemele Expert (anii 1980)"
st.title(title)

# Paragrafe
p1 = """
Anii 1980 au adus o etapă importantă în dezvoltarea **inteligenței artificiale** prin apariția **sistemelor expert**. Aceste programe foloseau baze de cunoștințe și reguli logice pentru a reproduce deciziile experților umani în domenii specifice, precum medicina, finanțele sau ingineria.
"""
p2 = """
Exemple celebre includ **MYCIN**, utilizat pentru diagnosticarea infecțiilor bacteriene, și **XCON**, folosit în configurarea sistemelor de calcul. Sistemele expert erau eficiente în probleme bine definite și repetitive, dar se confruntau cu dificultăți în adaptarea la situații noi sau în actualizarea rapidă a cunoștințelor.
"""
p3 = """
Această perioadă a demonstrat potențialul **IA** în aplicarea practică, dar și limitările abordării bazate exclusiv pe reguli fixe, ceea ce a condus ulterior la interesul pentru metodele de învățare automată.
"""

# Coloane
col1, col2 = st.columns((1, 2))

with col1:
    st.markdown(p1)

# Schema expert system (col2) cu Glass Morphism subtil
schema = """
<style>
.expert-system {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 80px;
    margin-top: 40px;
    font-family: Inter, sans-serif;
    color: white;
}

/* Glass Morphism pe box-uri */
.box {
    padding: 22px 26px;
    border-radius: 12px;
    min-width: 220px;
    text-align: center;
    position: relative;

    /* Efect Glass Morphism */
    background: rgba(255, 255, 255, 0.1);
    border: 1.5px solid rgba(255, 255, 255, 0.3);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);

    box-shadow: 0 0 20px rgba(255,255,255,0.05);
}

.box strong {
    display: block;
    margin-bottom: 8px;
    font-size: 1.1rem;
}

.box:not(:last-child)::after {
    content: "→";
    position: absolute;
    right: -55px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 3rem;
    color: #ddd;
}

.engine {
    border-color: gold;
    box-shadow: 0 0 25px rgba(255,215,0,0.5);
}

.output {
    border-color: #7dd3fc;
    box-shadow: 0 0 25px rgba(125,211,252,0.4);
}
</style>

<div class="expert-system">
    <div class="box"> <strong>Bază de cunoștințe</strong> Fapte și reguli </div>
    <div class="box engine"> <strong>Motor de inferență</strong> Raționament logic </div>
    <div class="box output"> <strong>Decizie</strong> Recomandare expert </div>
</div>
"""

with col2:
    st.markdown(
        body=schema,
        unsafe_allow_html=True
    )

# Paragrafe finale
st.markdown(p2)
st.markdown(p3)
