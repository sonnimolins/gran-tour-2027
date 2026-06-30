import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Gran Tour China & Corea 2027",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Ocultar toda la UI de Streamlit para que solo se vea la guía
st.markdown("""
<style>
#MainMenu, header, footer, .stDeployButton, [data-testid="stToolbar"] {
    visibility: hidden !important;
    height: 0 !important;
    min-height: 0 !important;
}
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
.stApp { margin: 0; }
iframe { border: none !important; display: block; }
</style>
""", unsafe_allow_html=True)

with open("app.html", "r", encoding="utf-8") as f:
    html = f.read()

components.html(html, height=8000, scrolling=True)
