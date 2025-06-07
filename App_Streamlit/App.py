import streamlit as st

# Interface utilisateur avec Streamlit
st.set_page_config(
    layout="wide",
    page_title="API_Developer & Data_Analysis",
    page_icon="🎬",
)

st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>
        Dashboard Cinelytics : <strong>API Developer & Data Analysis</strong>
    </h1>
    """,
    unsafe_allow_html=True
)

# Conteneur pour aligner les éléments horizontalement
col1, col2, col3 = st.columns([1, 4, 1])

# Colonne gauche : Image
with col1:
    st.image(
        "C:\\Users\\kkade\\Desktop\\Cinelytics_Dashboard\\App_Streamlit\\Images\\profil.jpg",
        width=80,
        use_container_width=False,
    )


# Colonne centrale : Titre
with col2:
    st.markdown(
        """
        <h1 style='text-align: center; margin-bottom: 0.2em;'>🎬 Exploration des Données MovieLens</h1>
        <p style='text-align: center; font-size: 1.1em; margin-top: 0; margin-bottom: 0.5em;'>
            Analyse des films les mieux notés, des genres, des tendances de notation et des préférences des utilisateurs.
        </p>
        <p style='text-align: center;'>
            <a href='https://grouplens.org/datasets/movielens/' target='_blank' style='color: #1f77b4; text-decoration: none;'>
                🔗 Accéder à la base de données MovieLens
            </a>
        </p>
        """,
        unsafe_allow_html=True
    )

# Colonne droite : Nom et lien LinkedIn
with col3:
    st.markdown(
        """
        <div style='text-align: right;'>
            <a href="https://www.linkedin.com/in/koukou-kader-kouadio-2a32371a4/" target="_blank" style='text-decoration: none; color: #0077b5;'>
                <strong>KOUADIO KADER</strong>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write(" ")
st.write(" ")

#################################### ============  Phase 1  ==============  ####################################
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>
        Phase 1 : <strong>Développeur Python & Architecte API</strong>
    </h1>
    """,
    unsafe_allow_html=True
)

# Colonnes : image (gauche) + bouton centré (droite)
col1, col2 = st.columns([2, 1])

with col1:
    st.image("C:\\Users\\kkade\\Desktop\\Cinelytics_Dashboard\\App_Streamlit\\Images\\Backend_Developer.png", width=600)

# with col2:
#     st.markdown(
#         """
#         <div style="display: flex; align-items: center; justify-content: center; height: 100%;">
#             <a href="https://github.com/kaderkouadio/Cinema_Insights" target="_blank">
#                 <button style="background-color: #28a745; color: white; padding: 12px 24px;
#                                border: none; border-radius: 8px; font-size: 16px; cursor: pointer;">
#                     📊 Cliquer pour voir le Code de la Phase 1
#                 </button>
#             </a>
#         </div>
#         """,
#         unsafe_allow_html=True
#     )

# Description de la phase
st.markdown(
    """
    <div style='text-align: justify; font-size: 16px; padding: 10px 30px;'>
        Cette première phase vise à construire une infrastructure technique robuste pour 
        manipuler et exposer les données du projet via une API. Le développeur conçoit 
        la base de données, développe une API REST sécurisée avec <strong>FastAPI</strong>, 
        la conteneurise via <strong>Docker</strong>, puis la déploie sur le cloud (Render).
        Un SDK Python est ensuite publié pour simplifier l’intégration de l’API dans d’autres outils.
    </div>
    """,
    unsafe_allow_html=True
)

# Boutons vers l'API et le SDK
st.markdown(
    """
    <div style="display: flex; gap: 20px; justify-content: center; margin-top: 30px;">
        <a href="https://cinema-insights.onrender.com" target="_blank">
            <button style="background-color: #28a745; color: white; padding: 10px 20px;
                           border: none; border-radius: 8px; font-size: 16px; cursor: pointer;">
                🌍 Voir l'API (Render)
            </button>
        </a>
        <a href="https://pypi.org/project/cinelytics_sdk" target="_blank">
            <button style="background-color: #007bff; color: white; padding: 10px 20px;
                           border: none; border-radius: 8px; font-size: 16px; cursor: pointer;">
                📦 Voir le SDK sur PyPI
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)
st.write(" ")
st.write(" ")

#################################### ============  Phase 2  ==============  ####################################
st.markdown(
    """
    <h1 style='text-align: center; color: #4CAF50;'>
        Phase 2 : <strong>Data Analyst – Exploration et Visualisation</strong>
    </h1>
    """,
    unsafe_allow_html=True
)

# Deux colonnes : image à gauche, bouton à droite
col1, col2 = st.columns([2, 1])

with col1:
    st.image("C:\\Users\\kkade\\Desktop\\Cinelytics_Dashboard\\App_Streamlit\\Images\\Data_Analyst.png", width=600)

# with col2:
    # st.markdown(
    #     """
    #     <div style="display: flex; align-items: center; justify-content: center; height: 100%;">
    #         <a href="https://github.com/kaderkouadio/Cinelytics_Dashboard" target="_blank">
    #             <button style="background-color: #28a745; color: white; padding: 12px 24px;
    #                            border: none; border-radius: 8px; font-size: 16px; cursor: pointer;">
    #                 📊 Cliquer pour voir le Code de la Phase 2
    #             </button>
    #         </a>
    #     </div>
    #     """,
    #     unsafe_allow_html=True
    # )

# Présentation de la phase 2
st.markdown(
    """
    <div style='text-align: justify; font-size: 16px; padding: 10px 30px;'>
        Lors de cette phase, l’accent est mis sur l’analyse exploratoire des données du box-office et 
        des films. Grâce à <strong>Pandas</strong>, <strong>Plotly</strong> et <strong>Streamlit</strong>, le Data Analyst 
        explore les tendances du marché, évalue les performances des films, 
        visualise les patterns cachés et structure des tableaux de bord dynamiques pour fournir des insights décisionnels.
    </div>
    """,
    unsafe_allow_html=True
)

 #################################### ============  boîte d'information   ==============  ####################################
st.markdown(
    """
    <div style='
        margin-top: 30px;
        background-color: #e8f4fd;
        border-left: 5px solid #2196F3;
        padding: 15px 20px;
        border-radius: 5px;
        font-size: 16px;
        color: #333;
    '>
        ℹ️ <strong>Note :</strong> l’API hébergée sur <strong>Render</strong> peut mettre quelques secondes à démarrer si elle est en veille.
    </div>
    """,
    unsafe_allow_html=True
)
