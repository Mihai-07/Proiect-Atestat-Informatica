import streamlit as st

# Configurarea paginii
st.set_page_config(layout="wide")

# Stilizare header, footer, paragrafe, tabel
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

# Sidebar glass-morphism
with open("liquid_glass_sidebar.html", "r") as file:
    css_liquid_sidebar = file.read()

st.markdown(css_liquid_sidebar, unsafe_allow_html=True)

# Fundal + fade-in global + stil text + efect pentru tabel
st.markdown(
    """
    <style>
    /* Fundal și text */
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
                          url("https://img.freepik.com/free-vector/gradient-speed-motion-background_52683-63639.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
        font-family: 'Inter', sans-serif;
    }

    /* Fade-in global */
    .stApp > div {
        opacity: 0;
        animation: fadeUp 1.2s ease forwards;
        animation-delay: 0.3s;
    }

    @keyframes fadeUp {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    /* Text paragraf */
    .stMarkdown p {
        font-size: 1.5rem;
        margin-bottom: 2rem;
    }

    /* Tabel HTML glass-morphism */
    .glass-table {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.2);
        border: 1px solid rgba(255,255,255,0.25);
        width: 100%;
        margin-top: 2rem;
        color: white;
        font-size: 1rem;
    }
    .glass-table td {
        padding: 10px;
    }
    .glass-table tr:nth-child(even) {
        background: rgba(255,255,255,0.05);
    }
    .glass-table a {
        color: white;
        text-decoration: underline;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titlu
st.title("9. Bibliografie")

# Lista surselor
sources = [
    "https://www.tensorflow.org/addons/tutorials/tqdm_progress_bar",
    "https://mdevelopers.com/blog/introduction-to-artificial-intelligence",
    "https://pythongeeks.org/expert-systems-in-ai/",
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://iticollege.edu/blog/machine-learning-basics-and-real-world-applications/",
    "https://www.ibm.com/think/topics/deep-learning",
    "https://savantlabs.io/blog/llms-in-business-analytics/",
    "https://www.mckbytes.com/the-impact-of-artificial-intelligence-on-the-job-market/",
    "https://gosharpener.com/blogs/544983/The-future-of-Artificial-Intelligence"
]

# Crearea tabelului HTML cu efect glass-morphism și link-uri clicabile
table_html = "<table class='glass-table'>"
for src in sources:
    table_html += f"<tr><td><a href='{src}' target='_blank'>{src}</a></td></tr>"
table_html += "</table>"

# Afișare tabel
st.markdown(table_html, unsafe_allow_html=True)
