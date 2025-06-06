import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_parquet_data

# Titre principal
st.title("🎬 Analyse Générale des Films et Évaluations")
st.markdown("Une vue d'ensemble sur les genres, évaluations, films populaires et utilisateurs les plus actifs.")

# Chargement des données
genre_df = load_parquet_data("genre_df.parquet")
movies_by_year = load_parquet_data("movies_by_year.parquet")
top_movies = load_parquet_data("top_movies_by_ratings.parquet")
ratings_df = load_parquet_data("ratings.parquet")
# st.write(ratings_df.head(10))

# ========== Graphique 1 : Top genres par nombre de films ==========
st.markdown("### 🎞️ Répartition des genres")
st.markdown("_Ce graphique montre les 10 genres les plus représentés dans la base de données._")

fig_genre = px.bar(
    genre_df,
    x="count",
    y="genre",
    title="Top 10 genres par nombre de films",
    labels={"genre": "Genre", "count": "Nombre de films"},
    color="count",
    color_continuous_scale="viridis",
    orientation='h'
)
fig_genre.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    height=350,
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=10, r=10, t=40, b=40)
)

# ========== Graphique 3 : Top utilisateurs par nombre d’évaluations ==========
st.markdown("### 👤 Activité des utilisateurs")
st.markdown("_Top 10 des utilisateurs ayant effectué le plus grand nombre d’évaluations._")

ratings_per_user = ratings_df['userId'].value_counts().reset_index()
ratings_per_user.columns = ['userId', 'rating_count']
top_users = ratings_per_user.head(10)
top_users["userId_str"] = "Utilisateur " + top_users["userId"].astype(str)

fig_users = px.bar(
    top_users,
    x="rating_count",
    y="userId_str",
    orientation="h",
    title="👤 Top 10 des utilisateurs les plus actifs",
    labels={"userId_str": "Utilisateur", "rating_count": "Nombre d’évaluations"},
    color="rating_count",
    color_continuous_scale="blues"
)
fig_users.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    height=400,
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=10, r=10, t=40, b=40)
)

# ========== Graphique 4 : Films les plus évalués ==========
st.markdown("### 🌟 Films les plus populaires")
st.markdown("_Top 20 des films ayant reçu le plus d’évaluations, avec leur note moyenne._")

fig_top_movies = px.bar(
    top_movies.sort_values("rating_count", ascending=True),
    x="rating_count",
    y="title",
    color="avg_rating",
    orientation="h",
    title="Top 20 des films par nombre d'évaluations",
    labels={"title": "Titre du film", "rating_count": "Nombre d'évaluations", "avg_rating": "Note moyenne"},
    color_continuous_scale="viridis"
)
fig_top_movies.update_layout(
    yaxis={'categoryorder': 'total ascending'},
    height=800,
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=10, r=10, t=40, b=40)
)

# ========== Graphique 5 : Nombre de films par année ==========
st.markdown("### 📅 Évolution du nombre de films")
st.markdown("_Nombre total de films produits chaque année._")

fig_by_year = px.bar(
    movies_by_year,
    x="year",
    y="movie_count",
    title="Nombre total de films par année (basé sur le titre)",
    labels={"year": "Année", "movie_count": "Nombre de films"},
)
fig_by_year.update_layout(
    xaxis_title="Année",
    yaxis_title="Nombre de films",
    height=600,
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=10, r=10, t=40, b=40)
)

# ========== Mise en page ==========
col1, col2 = st.columns([1, 2])

with col1:
    st.plotly_chart(fig_genre, use_container_width=True)
    st.plotly_chart(fig_users, use_container_width=True)

with col2:
    st.plotly_chart(fig_top_movies, use_container_width=True)
    

st.divider()
st.plotly_chart(fig_by_year, use_container_width=True)


#-------------------------------------------------------------------------


# import streamlit as st
# import pandas as pd
# import plotly.express as px
# from pathlib import Path
# import os
# from utils import load_parquet_data

# st.title("🎬 Analyse Générale des Films et Évaluations")

# # Chargement des données
# genre_df = load_parquet_data("genre_df.parquet")
# movies_by_year = load_parquet_data("movies_by_year.parquet")
# top_movies = load_parquet_data("top_movies_by_ratings.parquet")
# ratings_df = load_parquet_data("ratings.parquet")

# # ---------------- Graphique 1 ----------------
# fig_genre = px.bar(
#     genre_df,
#     x="count",
#     y="genre",
#     title="Top 10 genres par nombre de films",
#     labels={"genre": "Genre", "count": "Nombre de films"},
#     color="count",
#     color_continuous_scale="viridis",
#     orientation='h'
# )
# fig_genre.update_layout(
#     yaxis={'categoryorder': 'total ascending'},
#     height=350
# )

# # ---------------- Préparation pour Graphique 2 ----------------
# # Fusion des notes avec les genres
# genre_ratings = pd.merge(ratings_df, genre_df, on="movieId", how="inner")

# # Statistiques par genre
# genre_rating_stats = (
#     genre_ratings.groupby("genre")["rating"]
#     .agg(["count", "mean"])
#     .reset_index()
#     .rename(columns={"count": "rating_count", "mean": "avg_rating"})
# )

# # Top 10 genres les plus évalués
# genre_rating_stats = genre_rating_stats.sort_values(by="rating_count", ascending=False).head(10)

# # ---------------- Graphique 2 ----------------
# fig_genre_rating = px.bar(
#     data_frame=genre_rating_stats,
#     x="rating_count",
#     y="genre",
#     orientation="h",
#     color="avg_rating",
#     color_continuous_scale="viridis",
#     title="Top 10 genres par nombre d’évaluations et note moyenne",
#     labels={"genre": "Genre", "rating_count": "Nombre d'évaluations", "avg_rating": "Note moyenne"}
# )
# fig_genre_rating.update_layout(
#     yaxis={'categoryorder': 'total ascending'},
#     height=350
# )

# # ---------------- Graphique 3 ----------------
# ratings_per_user = ratings_df['userId'].value_counts().reset_index()
# ratings_per_user.columns = ['userId', 'rating_count']
# top_users = ratings_per_user.head(10)
# fig_users = px.bar(
#     top_users,
#     x="rating_count",
#     y=top_users["userId"].astype(str),
#     orientation="h",
#     title="Top 10 des utilisateurs par nombre d’évaluations",
#     labels={"userId": "Utilisateur", "rating_count": "Nombre d’évaluations"},
#     color="rating_count",
#     color_continuous_scale="viridis"
# )
# fig_users.update_layout(
#     yaxis={'categoryorder': 'total ascending'},
#     height=350
# )

# # ---------------- Graphique 4 ----------------
# fig_top_movies = px.bar(
#     top_movies.sort_values("rating_count", ascending=True),
#     x="rating_count",
#     y="title",
#     color="avg_rating",
#     orientation="h",
#     title="Top 20 des films par nombre d'évaluations",
#     labels={"title": "Titre du film", "rating_count": "Nombre d'évaluations", "avg_rating": "Note moyenne"},
#     color_continuous_scale="viridis"
# )
# fig_top_movies.update_layout(
#     yaxis={'categoryorder': 'total ascending'},
#     height=700
# )

# # ---------------- Graphique 5 ----------------
# fig_by_year = px.bar(
#     movies_by_year,
#     x="year",
#     y="movie_count",
#     title="Nombre total de films par année (basé sur le titre)",
#     labels={"year": "Année", "movie_count": "Nombre de films"},
# )
# fig_by_year.update_layout(
#     xaxis_title="Année",
#     yaxis_title="Nombre de films",
#     height=500
# )

# # ---------------- Affichage Streamlit ----------------
# col1, col2 = st.columns([1, 2])

# with col1:
#     st.plotly_chart(fig_genre, use_container_width=True)
#     st.plotly_chart(fig_genre_rating, use_container_width=True)
#     st.plotly_chart(fig_users, use_container_width=True)

# with col2:
#     st.plotly_chart(fig_top_movies, use_container_width=True)

# st.divider()

# st.plotly_chart(fig_by_year, use_container_width=True)
