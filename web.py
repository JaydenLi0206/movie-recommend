import streamlit as st
import pickle
import pandas as pd
import requests


moviedict=pickle.load(open('movie_dict.pkl','rb'))


def get_poster(id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
          id)
     data = requests.get(url)
     data = data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
     return full_path


def recommend(movie):
     movie_index = movies[movies['title'] == movie].index[0]  # id
     dist = similarity[movie_index]
     rec_movies = sorted(list(enumerate(dist)), reverse=True, key=lambda x: x[1])
     rl=[]
     pos=[]
     for i in rec_movies[1:7]:

          movie_id=movies.iloc[i[0]].id
          pos.append(get_poster(movie_id))
          rl.append(movies.iloc[i[0]].title)
     return rl,pos

movies=pd.DataFrame(moviedict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')
movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    rl,pos = recommend(selected_movie)
    col1, col2, col3, col4, col5,col6= st.columns(6)
    with col1:
        st.text(rl[0])
        st.image(pos[0])
    with col2:
         st.text(rl[1])
         st.image(pos[1])

    with col3:
         st.text(rl[2])
         st.image(pos[2])
    with col4:
         st.text(rl[3])
         st.image(pos[3])
    with col5:
         st.text(rl[4])
         st.image(pos[4])
    with col6:
         st.text(rl[5])
         st.image(pos[5])

