import streamlit as st

# Navigation
App = st.Page("App.py", title="Home", icon="🏠")         # House
page_1 = st.Page("page1.py", title="Statistiques globales", icon="🎬")     # Film clapperboard
page_2 = st.Page("page2.py", title="Analyse des tags", icon="📊")  # Bar chart
page_3 = st.Page("page3.py", title="Explorer les films", icon="🔎") # Magnifying glass

pg = st.navigation([ App, page_1, page_2, page_3])
pg.run()