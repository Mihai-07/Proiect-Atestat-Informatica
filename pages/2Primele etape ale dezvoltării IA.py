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

# CSS suplimentar pentru stairs (specific paginii 2)
st.markdown(
    """
    <style>

    /* Stairs - Glass Morphism light + contur mai pronunțat */
    .stairs-container {
        display: flex;
        align-items: flex-end;
        justify-content: center;
        height: 500px;
        gap: 20px;
        font-family: sans-serif;
        position: relative;
        top: -150px;
    }

    .step {
        width: 80px;
        height: 80px;
        display: flex;
        align-items: flex-end;
        justify-content: center;
        position: relative;

        /* Glass Morphism light */
        background: rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(8px);
        border-radius: 10px;
        border: 2px solid rgba(255, 255, 255, 0.35); /* contur mai pronunțat permanent */
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        transition: transform 0.3s, box-shadow 0.3s;
    }

    .step:nth-of-type(1) { height: 80px; }
    .step:nth-of-type(2) { height: 120px; }
    .step:nth-of-type(3) { height: 160px; }
    .step:nth-of-type(4) { height: 200px; }

    .step:last-child::after {
        content: "👑";
        position: absolute;
        top: -100px;
        font-size: 4rem;
        text-shadow: 0 0 10px gold, 0 0 20px yellow;
    }

    .step:hover {
        transform: translateY(-5px);
        box-shadow: 0 0 25px rgba(255,255,255,0.6), 0 0 50px rgba(255,255,255,0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titlu
st.title("2. Primele etape ale dezvoltării IA")

# Paragrafe
p1 = """
Perioada **1950–1970** marchează începuturile inteligenței artificiale ca domeniu
științific. În 1950, Alan Turing a propus celebrul **„Test Turing”**, menit să stabilească dacă o
mașină poate demonstra comportament inteligent similar cu cel uman.
"""
p2 = """
Câțiva ani mai târziu, în 1956, John McCarthy a folosit pentru prima dată termenul **„Artificial Intelligence”**
la Conferința Dartmouth, eveniment considerat actul de naștere al IA.
"""
p3 = """
În această perioadă au fost create programe precum **Logic Theorist** și **ELIZA**, capabile să rezolve probleme
logice sau să simuleze conversații simple. Totuși, progresele au fost limitate de puterea
redusă de calcul și lipsa datelor, ceea ce a făcut ca IA să rămână, pentru moment, mai
mult o promisiune decât o realitate.
"""

# Coloane
col1, col2 = st.columns((1, 1))

with col1:
    st.markdown(p1)
    st.markdown(p2)
    st.markdown(p3)

# Trepte cu Glass Morphism și contur mai pronunțat
stairs_html = """
<div class="stairs-container">
    <div class="step"></div>
    <div class="step"></div>
    <div class="step"></div>
    <div class="step"></div>
</div>
"""

with col2:
    st.markdown(
        body=stairs_html,
        unsafe_allow_html=True
    )
