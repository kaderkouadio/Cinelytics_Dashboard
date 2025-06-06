import streamlit as st

def home():
    st.title("🏠 Home")
    st.write("Bienvenue")

def overview():
    st.title("🎬 Overview")
    st.write("Statistiques globales")

def tags_insights():
    st.title("📊 Tags Insights")
    st.write("Analyse des tags")

def movie_explorer():
    st.title("🔎 Movie Explorer")
    st.write("Explorer les films")

pages = {
    "🏠 Home": home,
    "🎬 Overview": overview,
    "📊 Tags Insights": tags_insights,
    "🔎 Movie Explorer": movie_explorer,
}

selection = st.sidebar.radio("Navigation", list(pages.keys()))
pages[selection]()
