import streamlit as st
import pandas as pd
import pickle

# Load pickled data
movies = pickle.load(open('movies.pkl', 'rb'))
cosine_sim = pickle.load(open('cosine_sim.pkl', 'rb'))

# Fix column naming issue
if 'title_y' in movies.columns:
    movies.rename(columns={'title_y': 'title'}, inplace=True)

# Define the recommendation function
def get_recommendations(title, cosine_sim=cosine_sim):
    if title not in movies['title'].values:
        return ["Movie not found."]
    
    # Get the index of the movie
    idx = movies[movies['title'] == title].index[0]
    
    # Compute similarity scores
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    # Get the top 10 similar movies
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]
    
    return movies['title'].iloc[movie_indices].tolist()

# Streamlit app layout
st.title("🎬 Movie Recommendation System")

# Dropdown for movie selection
selected_movie = st.selectbox("Select a movie", movies['title'].values)

# Show recommendations on button click
if st.button("Show Recommendations"):
    recommendations = get_recommendations(selected_movie)
    st.write("### Recommended Movies:")
    for movie in recommendations:
        st.write(f"🎥 {movie}")

st.write("🔹 Select a movie and click 'Show Recommendations' to get similar movies!")
