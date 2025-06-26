import streamlit as st
import random

proverbes = [
    "L’endurance est la clé de la réussite.",
    "Un cœur content est un trésor.",
    "Le silence est la sagesse des sages.",
    "Qui veut, peut.",
    "Ce que tu sèmes aujourd'hui, tu le récolteras demain."
]

objectifs = [
    "Bois un verre d’eau 💧",
    "Écris une chose positive ✍️",
    "Respire profondément 🌬️",
    "Range ton espace 🧺",
    "Écoute une chanson que tu aimes 🎵"
]

st.set_page_config(page_title="Moroccan Mindset", page_icon="🌿")
st.title("🌿 Moroccan Mindset – Sérénité et Sagesse")

if st.button("✨ Commencer ma journée"):
    st.success("📜 Proverbe du jour : " + random.choice(proverbes))
    st.info("🌸 Soin bien-être : " + random.choice(objectifs))
import random
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://www.pinterest.com/pin/15833036183317010/");
        background-position: center;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)
