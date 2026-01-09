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

# Configurare pagină
st.set_page_config(layout="wide")

st.markdown(css_header_footer, unsafe_allow_html=True)
st.markdown(body=css_liquid_sidebar, unsafe_allow_html=True)
st.markdown(css_background, unsafe_allow_html=True)

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
st.title("6. Epoca modelelor lingvistice mari (2020-prezent)")

# Coloane
col1, col2 = st.columns((2, 1))

# Conținut text
p1 = """
Începând cu 2020, **IA** a intrat în era modelelor lingvistice mari **(Large Language
Models – LLM)**, precum **GPT-3**, **PaLM** sau **Claude**. Aceste rețele neuronale, 
antrenate pe volume uriașe de text, pot genera conținut coerent, traduce, rezuma și chiar programa.
"""
p2 = """
Integrarea **LLM** cu memorie, instrumente externe și capacități multimodale a condus la
apariția **agenților inteligenți** capabili să acționeze autonom în sarcini complexe. Acești
agenți sunt folosiți în educație, cercetare, afaceri și creație artistică.
"""
p3 = """
Epoca actuală evidențiază potențialul **IA** de a înțelege și produce limbaj natural la nivel 
avansat și deschide noi perspective pentru sisteme capabile să colaboreze cu oamenii și să rezolve
probleme complexe, extinzând semnificativ aplicabilitatea inteligenței artificiale.
"""

with col1:
    st.markdown(p1)
    st.markdown(p2)
    st.markdown(p3)

# Animație completă LLM cu st.html()
llm_chip_animation = """
<!DOCTYPE html>
<html lang="ro">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GPU Chip LLM</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: radial-gradient(ellipse at center, #0a0520 0%, #000000 100%);
            overflow: hidden;
            perspective: 2000px;
        }

        .chip-container {
            position: relative;
            width: 350px;
            height: 350px;
            transform-style: preserve-3d;
            transform: rotateX(5deg);
        }

        .chip {
            position: absolute;
            width: 100%;
            height: 100%;
            background: linear-gradient(135deg, 
                rgba(10, 5, 40, 0.9) 0%, 
                rgba(20, 10, 60, 0.85) 50%, 
                rgba(10, 5, 40, 0.9) 100%);
            backdrop-filter: blur(30px);
            border-radius: 30px;
            border: 3px solid rgba(255, 255, 255, 0.1);
            box-shadow: 
                0 20px 60px 0 rgba(0, 0, 0, 0.8),
                0 0 100px rgba(100, 50, 255, 0.3),
                inset 0 0 80px rgba(0, 100, 255, 0.1);
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .chip::before {
            content: '';
            position: absolute;
            top: -3px;
            left: -3px;
            right: -3px;
            bottom: -3px;
            background: linear-gradient(135deg, 
                rgba(255, 50, 150, 0.4), 
                rgba(100, 50, 255, 0.5), 
                rgba(0, 150, 255, 0.4));
            border-radius: 30px;
            z-index: -1;
            filter: blur(25px);
            opacity: 0.6;
            animation: glow 3s ease-in-out infinite;
        }

        @keyframes glow {
            0%, 100% {
                opacity: 0.6;
                filter: blur(25px);
            }
            50% {
                opacity: 1;
                filter: blur(35px);
            }
        }

        .chip::after {
            content: '';
            position: absolute;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at 30% 30%, 
                rgba(255, 255, 255, 0.15) 0%, 
                transparent 50%);
            border-radius: 30px;
        }

        .center-chip {
            position: relative;
            width: 112px;
            height: 112px;
            background: linear-gradient(135deg, 
                rgba(0, 0, 0, 0.9) 0%, 
                rgba(20, 10, 40, 0.95) 50%, 
                rgba(0, 0, 0, 0.9) 100%);
            backdrop-filter: blur(15px);
            border: 3px solid rgba(150, 100, 255, 0.5);
            border-radius: 15px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: 'Arial Black', sans-serif;
            font-size: 34px;
            font-weight: bold;
            color: #ffaa00;
            text-shadow: 
                0 0 20px #ffaa00,
                0 0 40px #ffaa00,
                0 0 60px #ff6600,
                0 0 80px #ff6600;
            z-index: 10;
            box-shadow: 
                0 0 40px rgba(255, 150, 0, 0.6),
                0 0 80px rgba(150, 100, 255, 0.4),
                inset 0 0 30px rgba(100, 50, 255, 0.3);
        }

        .center-chip::before {
            content: '';
            position: absolute;
            top: 7px;
            left: 7px;
            right: 7px;
            bottom: 7px;
            border: 2px solid rgba(0, 150, 255, 0.3);
            border-radius: 8px;
        }

        .wire {
            position: absolute;
            height: 4px;
            transform-origin: left center;
            border-radius: 2px;
            animation: pulse 2s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% {
                opacity: 0.7;
                box-shadow: 0 0 15px currentColor;
            }
            50% {
                opacity: 1;
                box-shadow: 0 0 30px currentColor;
            }
        }

        .wire:nth-child(1),
        .wire:nth-child(5),
        .wire:nth-child(9),
        .wire:nth-child(13) {
            background: linear-gradient(90deg, 
                rgba(255, 50, 150, 0.9), 
                rgba(150, 50, 255, 0.7), 
                rgba(0, 150, 255, 0.4),
                transparent);
            color: rgba(255, 50, 150, 0.9);
        }

        .wire:nth-child(3),
        .wire:nth-child(7),
        .wire:nth-child(11),
        .wire:nth-child(15) {
            background: linear-gradient(90deg, 
                rgba(150, 50, 255, 0.9), 
                rgba(100, 100, 255, 0.7), 
                rgba(0, 200, 255, 0.4),
                transparent);
            color: rgba(150, 50, 255, 0.9);
        }

        .wire:nth-child(2),
        .wire:nth-child(6),
        .wire:nth-child(10),
        .wire:nth-child(14) {
            background: linear-gradient(90deg, 
                rgba(0, 150, 255, 0.9), 
                rgba(100, 150, 255, 0.7), 
                rgba(150, 100, 255, 0.4),
                transparent);
            color: rgba(0, 150, 255, 0.9);
        }

        .wire:nth-child(4),
        .wire:nth-child(8),
        .wire:nth-child(12),
        .wire:nth-child(16) {
            background: linear-gradient(90deg, 
                rgba(100, 100, 255, 0.9), 
                rgba(150, 100, 255, 0.7), 
                rgba(255, 50, 150, 0.4),
                transparent);
            color: rgba(100, 100, 255, 0.9);
        }

        .wire:nth-child(n+17) {
            background: linear-gradient(90deg, 
                rgba(255, 100, 200, 0.8), 
                rgba(150, 100, 255, 0.6), 
                rgba(0, 150, 255, 0.3),
                transparent);
            color: rgba(255, 100, 200, 0.8);
            height: 3px;
        }

        .wire:nth-child(1) { width: 126px; top: 50%; left: 50%; transform: rotate(0deg); animation-delay: 0s; }
        .wire:nth-child(2) { width: 119px; top: 50%; left: 50%; transform: rotate(22.5deg); animation-delay: 0.1s; }
        .wire:nth-child(3) { width: 126px; top: 50%; left: 50%; transform: rotate(45deg); animation-delay: 0.2s; }
        .wire:nth-child(4) { width: 119px; top: 50%; left: 50%; transform: rotate(67.5deg); animation-delay: 0.3s; }
        .wire:nth-child(5) { width: 126px; top: 50%; left: 50%; transform: rotate(90deg); animation-delay: 0.4s; }
        .wire:nth-child(6) { width: 119px; top: 50%; left: 50%; transform: rotate(112.5deg); animation-delay: 0.5s; }
        .wire:nth-child(7) { width: 126px; top: 50%; left: 50%; transform: rotate(135deg); animation-delay: 0.6s; }
        .wire:nth-child(8) { width: 119px; top: 50%; left: 50%; transform: rotate(157.5deg); animation-delay: 0.7s; }
        .wire:nth-child(9) { width: 126px; top: 50%; left: 50%; transform: rotate(180deg); animation-delay: 0.8s; }
        .wire:nth-child(10) { width: 119px; top: 50%; left: 50%; transform: rotate(202.5deg); animation-delay: 0.9s; }
        .wire:nth-child(11) { width: 126px; top: 50%; left: 50%; transform: rotate(225deg); animation-delay: 1s; }
        .wire:nth-child(12) { width: 119px; top: 50%; left: 50%; transform: rotate(247.5deg); animation-delay: 1.1s; }
        .wire:nth-child(13) { width: 126px; top: 50%; left: 50%; transform: rotate(270deg); animation-delay: 1.2s; }
        .wire:nth-child(14) { width: 119px; top: 50%; left: 50%; transform: rotate(292.5deg); animation-delay: 1.3s; }
        .wire:nth-child(15) { width: 126px; top: 50%; left: 50%; transform: rotate(315deg); animation-delay: 1.4s; }
        .wire:nth-child(16) { width: 119px; top: 50%; left: 50%; transform: rotate(337.5deg); animation-delay: 1.5s; }

        .wire:nth-child(17) { width: 91px; top: 50%; left: 50%; transform: rotate(11.25deg); animation-delay: 0.05s; }
        .wire:nth-child(18) { width: 91px; top: 50%; left: 50%; transform: rotate(33.75deg); animation-delay: 0.15s; }
        .wire:nth-child(19) { width: 91px; top: 50%; left: 50%; transform: rotate(56.25deg); animation-delay: 0.25s; }
        .wire:nth-child(20) { width: 91px; top: 50%; left: 50%; transform: rotate(78.75deg); animation-delay: 0.35s; }
        .wire:nth-child(21) { width: 91px; top: 50%; left: 50%; transform: rotate(101.25deg); animation-delay: 0.45s; }
        .wire:nth-child(22) { width: 91px; top: 50%; left: 50%; transform: rotate(123.75deg); animation-delay: 0.55s; }
        .wire:nth-child(23) { width: 91px; top: 50%; left: 50%; transform: rotate(146.25deg); animation-delay: 0.65s; }
        .wire:nth-child(24) { width: 91px; top: 50%; left: 50%; transform: rotate(168.75deg); animation-delay: 0.75s; }
        .wire:nth-child(25) { width: 91px; top: 50%; left: 50%; transform: rotate(191.25deg); animation-delay: 0.85s; }
        .wire:nth-child(26) { width: 91px; top: 50%; left: 50%; transform: rotate(213.75deg); animation-delay: 0.95s; }
        .wire:nth-child(27) { width: 91px; top: 50%; left: 50%; transform: rotate(236.25deg); animation-delay: 1.05s; }
        .wire:nth-child(28) { width: 91px; top: 50%; left: 50%; transform: rotate(258.75deg); animation-delay: 1.15s; }
        .wire:nth-child(29) { width: 91px; top: 50%; left: 50%; transform: rotate(281.25deg); animation-delay: 1.25s; }
        .wire:nth-child(30) { width: 91px; top: 50%; left: 50%; transform: rotate(303.75deg); animation-delay: 1.35s; }
        .wire:nth-child(31) { width: 91px; top: 50%; left: 50%; transform: rotate(326.25deg); animation-delay: 1.45s; }
        .wire:nth-child(32) { width: 91px; top: 50%; left: 50%; transform: rotate(348.75deg); animation-delay: 1.55s; }

        .corner-pad {
            position: absolute;
            width: 30px;
            height: 30px;
            background: linear-gradient(135deg, 
                rgba(255, 100, 200, 0.3), 
                rgba(150, 100, 255, 0.3));
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 5px;
            box-shadow: 
                0 0 20px rgba(150, 100, 255, 0.5),
                inset 0 0 10px rgba(255, 100, 200, 0.3);
        }

        .corner-pad:nth-child(1) { top: 30px; left: 30px; }
        .corner-pad:nth-child(2) { top: 30px; right: 30px; }
        .corner-pad:nth-child(3) { bottom: 30px; left: 30px; }
        .corner-pad:nth-child(4) { bottom: 30px; right: 30px; }

        .particle {
            position: absolute;
            width: 3px;
            height: 3px;
            background: rgba(255, 255, 255, 0.8);
            border-radius: 50%;
            animation: float 4s ease-in-out infinite;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
        }

        @keyframes float {
            0%, 100% {
                transform: translateY(0) scale(1);
                opacity: 0.8;
            }
            50% {
                transform: translateY(-20px) scale(1.5);
                opacity: 1;
            }
        }

        .particle:nth-child(37) { top: 15%; left: 20%; animation-delay: 0s; }
        .particle:nth-child(38) { top: 25%; right: 25%; animation-delay: 0.5s; }
        .particle:nth-child(39) { top: 70%; left: 15%; animation-delay: 1s; }
        .particle:nth-child(40) { top: 60%; right: 20%; animation-delay: 1.5s; }
        .particle:nth-child(41) { top: 40%; left: 10%; animation-delay: 2s; }
        .particle:nth-child(42) { top: 35%; right: 12%; animation-delay: 2.5s; }
    </style>
</head>
<body>
    <div class="chip-container">
        <div class="chip">
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            <div class="wire"></div>
            
            <div class="center-chip">LLM</div>
            
            <div class="corner-pad"></div>
            <div class="corner-pad"></div>
            <div class="corner-pad"></div>
            <div class="corner-pad"></div>
            
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
        </div>
    </div>
</body>
</html>
"""

with col2:
    st.html(llm_chip_animation)
