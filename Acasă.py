import streamlit as st

# Citim secretele pentru header și footer
header_text = st.secrets["header"]["header"]
footer_left = st.secrets["footer"]["footer_left"]
footer_right = st.secrets["footer"]["footer_right"]
footer_center = st.secrets["footer"]["footer_center"]

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
    </style>
    """

css_liquid_sidebar = load_sidebar_html()
css_header_footer = get_header_footer_css()
css_background = get_background_css()

st.set_page_config(layout="wide")

st.markdown(css_header_footer, unsafe_allow_html=True)
st.markdown(body=css_liquid_sidebar, unsafe_allow_html=True)

# Fundal + fade-in global rapid
st.markdown(css_background, unsafe_allow_html=True)

# CSS suplimentar pentru hero section (specific paginii Acasă)
st.markdown(
    """
    <style>

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

    /* CUSTOM HEADER - Complet Transparent */
    .custom-header {
        position: fixed;
        top: 60px;
        left: 0;
        right: 0;
        z-index: 999;
        padding: 1rem 2rem;
        text-align: center;
        background: transparent;
        color: white;
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        line-height: 1.6;
        white-space: pre-line;
        opacity: 0;
        animation: fadeUp 1.2s ease forwards;
        animation-delay: 0.5s;
    }

    /* CUSTOM FOOTER - Complet Transparent */
    .custom-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        z-index: 999;
        padding: 1.5rem 2rem 2rem;
        background: transparent;
        color: white;
        font-family: 'Inter', sans-serif;
        opacity: 0;
        animation: fadeUp 1.2s ease forwards;
        animation-delay: 0.6s;
    }

    .footer-top {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 1rem;
        gap: 2rem;
    }

    .footer-left, .footer-right {
        flex: 1;
        font-size: 0.95rem;
        line-height: 1.6;
        white-space: pre-line;
    }

    .footer-left {
        text-align: left;
    }

    .footer-right {
        text-align: right;
    }

    .footer-center {
        text-align: center;
        font-size: 0.9rem;
        line-height: 1.5;
        opacity: 0.85;
        padding-top: 0.5rem;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        white-space: pre-line;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header customizat
st.markdown(
    f"""
    <div class="custom-header">
        {header_text}
    </div>
    """,
    unsafe_allow_html=True
)

# Hero section
st.markdown(
    """
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

# Footer customizat
st.markdown(
    f"""
    <div class="custom-footer">
        <div class="footer-top">
            <div class="footer-left">
                {footer_left}
            </div>
            <div class="footer-right">
                {footer_right}
            </div>
        </div>
        <div class="footer-center">
            {footer_center}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)