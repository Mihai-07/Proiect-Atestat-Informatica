import streamlit as st

# Sidebar glass morphism
with open("liquid_glass_sidebar.html", "r") as file:
    css_liquid_sidebar = file.read()

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

st.markdown(
    body=css_liquid_sidebar,
    unsafe_allow_html=True
)

# Fundal + fade-in global rapid
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

    /* FADE-IN GLOBAL pentru tot conținutul */
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

    /* HERO SECTION */
    .hero {
        position: fixed;
        inset: 0;
        background-size: cover;
        background-position: center;
        display: flex;
        align-items: center;
        justify-content: center;
        font-family: "Inter", system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .hero::before {
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55));
        z-index: 0;
    }

    .hero-content {
        position: relative;
        text-align: center;
        color: white;
        max-width: 900px;
        padding: 2rem;
        opacity: 0;
        transform: translateY(20px);
        animation: fadeUp 1.2s ease forwards; /* timing identic cu restul paginii */
    }

    .hero-title {
        font-size: clamp(2.5rem, 5vw, 4.5rem);
        font-weight: 700;
        line-height: 1.15;
        margin-bottom: 1.2rem;
        letter-spacing: -0.02em;
    }

    .hero-subtitle {
        font-size: clamp(1.2rem, 2vw, 1.6rem);
        font-weight: 400;
        opacity: 0.9;
    }
    </style>

    <div class="hero">
        <div class="hero-content">
            <div class="hero-title">
                Evoluția Inteligenței Artificiale
            </div>
            <div class="hero-subtitle">
                De la primele modele la agenți moderni
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
