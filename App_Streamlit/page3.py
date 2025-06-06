import streamlit as st
import pandas as pd
from pathlib import Path
import re

 ##### ====== Mise en cache de l'initialisation du Client ===
from cinelytics_sdk import MovieClient, MovieConfig

@st.cache_resource
def get_movie_client():
    config = MovieConfig(movie_base_url="https://cinema-insights.onrender.com")
    client = MovieClient(config=config)
    client.health_check()
    return client

client = get_movie_client()

# === Configuration et chargement des fichiers ===
output_dir = Path(__file__).resolve().parents[1] / "output"

movie_stats = pd.read_parquet(output_dir / "top_movies_by_ratings.parquet")
genre_df = pd.read_parquet(output_dir / "genre_df.parquet")
tags_df = pd.read_parquet(output_dir / "user_tag_stats.parquet")
ratings_df = pd.read_parquet(output_dir / "ratings.parquet")

# === Chargement des métadonnées enrichies ===
meta_links_df = pd.read_parquet(output_dir / "links_enriched.parquet")
meta_links = meta_links_df.set_index("movieId")[["imdb_url", "poster_url"]].to_dict(orient="index")

# === Filtres de recherche ===
st.title("🔎 Explorateur de films")

with st.expander("🎯 Filtres avancés", expanded=True):
    col1, col2, col3 = st.columns([1, 1, 2])

    all_genres = sorted(set(genre_df['genre']))
    selected_genres = col1.multiselect("Genres", all_genres, default=all_genres[:3])

    movie_stats["year"] = movie_stats["title"].apply(
        lambda x: int(re.search(r"\((\d{4})\)", x).group(1)) if re.search(r"\((\d{4})\)", x) else None
    )
    years = movie_stats['year'].dropna().astype(int)
    selected_years = col2.slider("Année de sortie", min_value=int(years.min()), max_value=int(years.max()), value=(1990, 2018))

    selected_rating = col1.slider("Note moyenne min.", 0.5, 5.0, 3.5, 0.1)
    selected_votes = col2.slider("Nombre de votes min.", 0, int(movie_stats['rating_count'].max()), 50, 10)

    tag_options = sorted(tags_df['tag'].unique())
    selected_tags = col3.multiselect("Tags à inclure", tag_options)

    keyword = col3.text_input("Mot-clé dans le titre")


# Bouton pour lancer la recherche
if st.button("🔍 Lancer la recherche"):

    # === Filtrage des films ===
    filtered_movies = movie_stats.copy()

    ########## Ajout de la colonne 'genre' #####################

    # Mise en cache locale des genres
    genre_cache = {}

    def get_genres_with_cache(movie_id: int):
        if movie_id in genre_cache:
            return genre_cache[movie_id]
        try:
            movie = client.get_movie(movie_id)
            genres = movie.genres  # Ex: "Comedy|Drama"
            genre_cache[movie_id] = genres
            return genres
        except Exception:
            return None

    # Application sur la DataFrame
    filtered_movies['genre'] = filtered_movies['movieId'].apply(get_genres_with_cache)

    #################################################################


    if selected_genres:
        filtered_movies = filtered_movies[filtered_movies['genre'].apply(lambda g: any(genre in g for genre in selected_genres))]

    filtered_movies = filtered_movies[
        (filtered_movies['avg_rating'] >= selected_rating) &
        (filtered_movies['rating_count'] >= selected_votes) &
        (filtered_movies['year'].between(*selected_years))
    ]

    if keyword:
        filtered_movies = filtered_movies[filtered_movies['title'].str.contains(keyword, case=False)]

    if selected_tags:
        def has_tags(row):
            return all(tag in row.get('tags', '') for tag in selected_tags)
        if 'tags' in filtered_movies.columns:
            filtered_movies = filtered_movies[filtered_movies.apply(has_tags, axis=1)]

    # === Résumé en haut ===
    st.markdown("## 🔎 Résultats de la recherche")
    k1, k2, k3 = st.columns(3)
    k1.metric("🎞️ Nombre de films", len(filtered_movies))
    k2.metric("⭐ Note moyenne", f"{filtered_movies['avg_rating'].mean():.2f}" if not filtered_movies.empty else "N/A")
    k3.metric("👥 Votes moyens", f"{filtered_movies['rating_count'].mean():.0f}" if not filtered_movies.empty else "N/A")

    # === Affichage des films sous forme de cartes ===
    def generate_card(movie):
        movie_id = int(movie['movieId'])  # S'assurer que la clé est bien un int
        imdb_url = meta_links.get(movie_id, {}).get('imdb_url', "#")
        poster_url = meta_links.get(movie_id, {}).get('poster_url', "https://via.placeholder.com/120x180?text=No+Image")

        with st.container():
            cols = st.columns([1, 4])
            with cols[0]:
                st.image(poster_url, width=120)
            with cols[1]:
                st.markdown(
                    f"""<h4><a href="{imdb_url}" target="_blank" rel="noopener noreferrer">{movie['title']}</a></h4>""",
                    unsafe_allow_html=True
                )
                st.markdown(f"**Genres :** {movie['genre']}")
                st.markdown(f"**Note moyenne :** ⭐ {movie['avg_rating']:.2f}")
                st.markdown(f"**Nombre d'évaluations :** {movie['rating_count']}")
                if 'tags' in movie:
                    st.markdown(f"**Tags :** *{movie['tags']}*")
            st.divider()

    # Afficher les cartes pour les 30 premiers films
    if filtered_movies.empty:
        st.warning("Aucun film ne correspond à vos critères.")
    else:
        for _, movie in filtered_movies.sort_values("avg_rating", ascending=False).iterrows():
            generate_card(movie)

else:
    st.info("🧭 Définissez vos filtres, puis cliquez sur **Lancer la recherche** pour explorer les films.")





#-------------------------------------------------------------------------------------




# import streamlit as st
# import pandas as pd
# from pathlib import Path
# import re

# from cinelytics_sdk import MovieClient, MovieConfig

# # ========== Client Movie API ==========
# @st.cache_resource
# def get_movie_client():
#     config = MovieConfig(movie_base_url="https://cinema-insights.onrender.com")
#     client = MovieClient(config=config)
#     client.health_check()
#     return client

# client = get_movie_client()

# # ========== Chargement des données ==========
# @st.cache_data
# def load_data():
#     output_dir = Path(__file__).resolve().parents[1] / "output"

#     movie_stats = pd.read_parquet(output_dir / "top_movies_by_ratings.parquet")
#     genre_df = pd.read_parquet(output_dir / "genre_df.parquet")
#     tags_df = pd.read_parquet(output_dir / "user_tag_stats.parquet")
#     meta_links_df = pd.read_parquet(output_dir / "links_enriched.parquet")
#     ratings_df = pd.read_parquet(output_dir / "ratings.parquet")

#     meta_links = meta_links_df.set_index("movieId")[["imdb_url", "poster_url"]].to_dict(orient="index")

#     return movie_stats, genre_df, tags_df, meta_links, ratings_df

# movie_stats, genre_df, tags_df, meta_links, _ = load_data()

# # ========== Extraction année ==========
# if "year" not in movie_stats.columns:
#     movie_stats["year"] = movie_stats["title"].apply(
#         lambda x: int(re.search(r"\((\d{4})\)", x).group(1)) if re.search(r"\((\d{4})\)", x) else None
#     )

# # ========== Mise en cache des genres ==========
# genre_cache = {}

# @st.cache_data
# def get_genres_with_cache(movie_id: int):
#     if movie_id in genre_cache:
#         return genre_cache[movie_id]
#     try:
#         movie = client.get_movie(movie_id)
#         genres = movie.genres  # Ex: "Comedy|Drama"
#         genre_cache[movie_id] = genres
#         return genres
#     except Exception:
#         return None

# # Ajout des genres si manquant
# if "genre" not in movie_stats.columns:
#     movie_stats["genre"] = movie_stats["movieId"].apply(get_genres_with_cache)

# # ========== Interface Utilisateur ==========
# st.title("🔎 Explorateur de films")

# with st.expander("🎯 Filtres avancés", expanded=True):
#     col1, col2, col3 = st.columns([1, 1, 2])

#     all_genres = sorted(set(genre_df['genre']))
#     selected_genres = col1.multiselect("Genres", all_genres, default=all_genres[:3])

#     years = movie_stats['year'].dropna().astype(int)
#     selected_years = col2.slider("Année de sortie", min_value=int(years.min()), max_value=int(years.max()), value=(1990, 2018))

#     selected_rating = col1.slider("Note moyenne min.", 0.5, 5.0, 3.5, 0.1)
#     selected_votes = col2.slider("Nombre de votes min.", 0, int(movie_stats['rating_count'].max()), 50, 10)

#     tag_options = sorted(tags_df['tag'].unique())
#     selected_tags = col3.multiselect("Tags à inclure", tag_options)

#     keyword = col3.text_input("Mot-clé dans le titre")

# # ========== Bouton de recherche ==========
# if st.button("🔍 Lancer la recherche"):

#     # Copie du dataset de base
#     filtered_movies = movie_stats.copy()

#     # Filtrage par genre
#     if selected_genres:
#         filtered_movies = filtered_movies[
#             filtered_movies['genre'].apply(lambda g: any(genre in g for genre in selected_genres) if isinstance(g, str) else False)
#         ]

#     # Filtrage par note, votes, année
#     filtered_movies = filtered_movies[
#         (filtered_movies['avg_rating'] >= selected_rating) &
#         (filtered_movies['rating_count'] >= selected_votes) &
#         (filtered_movies['year'].between(*selected_years))
#     ]

#     # Filtrage par mot-clé
#     if keyword:
#         filtered_movies = filtered_movies[filtered_movies['title'].str.contains(keyword, case=False)]

#     # Fusion avec les tags
#     filtered_movies = filtered_movies.merge(tags_df[['movieId', 'tags']], on='movieId', how='left')

#     # Filtrage par tags
#     if selected_tags:
#         def has_all_tags(tags):
#             if not isinstance(tags, str):
#                 return False
#             return all(tag in tags for tag in selected_tags)

#         filtered_movies = filtered_movies[filtered_movies['tags'].apply(has_all_tags)]

#     # ========== Résumé ==========
#     st.markdown("## 🔎 Résultats de la recherche")
#     k1, k2, k3 = st.columns(3)
#     k1.metric("🎞️ Nombre de films", len(filtered_movies))
#     k2.metric("⭐ Note moyenne", f"{filtered_movies['avg_rating'].mean():.2f}" if not filtered_movies.empty else "N/A")
#     k3.metric("👥 Votes moyens", f"{filtered_movies['rating_count'].mean():.0f}" if not filtered_movies.empty else "N/A")

#     # ========== Affichage des cartes ==========
#     def render_movie_card(movie):
#         movie_id = int(movie['movieId'])
#         imdb_url = meta_links.get(movie_id, {}).get('imdb_url', "#")
#         poster_url = meta_links.get(movie_id, {}).get('poster_url', "https://via.placeholder.com/120x180?text=No+Image")

#         with st.container():
#             cols = st.columns([1, 4])
#             with cols[0]:
#                 st.image(poster_url, width=120)
#             with cols[1]:
#                 st.markdown(
#                     f"""<h4><a href="{imdb_url}" target="_blank" rel="noopener noreferrer">{movie['title']}</a></h4>""",
#                     unsafe_allow_html=True
#                 )
#                 st.markdown(f"**Genres :** {movie['genre']}")
#                 st.markdown(f"**Note moyenne :** ⭐ {movie['avg_rating']:.2f}")
#                 st.markdown(f"**Nombre d'évaluations :** {movie['rating_count']}")
#                 if 'tags' in movie and isinstance(movie['tags'], str):
#                     st.markdown(f"**Tags :** *{movie['tags']}*")
#             st.divider()

#     if filtered_movies.empty:
#         st.warning("Aucun film ne correspond à vos critères.")
#     else:
#         for _, movie in filtered_movies.sort_values("avg_rating", ascending=False).head(30).iterrows():
#             render_movie_card(movie)

# else:
#     st.info("🧭 Définissez vos filtres, puis cliquez sur **Lancer la recherche** pour explorer les films.")
