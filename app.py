"""
import streamlit as st
import pandas as pd 
import pickle
import requests


combined_df = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = combined_df['title'].values

def fetch(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=6b07482f2fb6f5e6f6fec523ccb0586e&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data.get('poster_path')
    
    if poster_path:
        full_path = "https://image.tmdb.org/t/p/original" + poster_path
        return full_path
    else:
        st.warning("Poster not available for this movie.")
        return ""


def recommend (movie):
    #movie_index = [combined_df["title"] == movie].index[0]

    try:
        movie_index = combined_df.index[combined_df["title"] == movie].tolist()[0]
    except IndexError:
        st.error("Movie not found in the database. Please choose another movie.")
        return []

    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),\
                              reverse=True, key= lambda x:x[1])[1:11]
    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = i[0]
         # fetch poster from API
        posters = fetch(movie_id)
        recommended_movies_posters.append(posters)
       
        recommended_movies.append(combined_df.iloc[i[0]].title)
        
    return recommended_movies,recommended_movies_posters





st.header("Movie Recommender System")
st.subheader("By Anand Kumar")



option = st.selectbox(
    'Input Movie Name Here:',
    movie_list)

if st.button('Recommend'):
    recommended_movie,recommended_movie_posters = recommend(option)
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.caption(recommended_movie[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.caption(recommended_movie[1])
        

    with col3:
        st.image(recommended_movie_posters[2])
        st.caption(recommended_movie[2])
        
    with col4:
        st.image(recommended_movie_posters[3])
        st.caption(recommended_movie[3])
        
    with col5:
        st.image(recommended_movie_posters[4])
        st.caption(recommended_movie[4])

        
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[5])
        st.caption(recommended_movie[5])
    with col2:
        st.image(recommended_movie_posters[6])
        st.caption(recommended_movie[6])
        

    with col3:
        st.image(recommended_movie_posters[7])
        st.caption(recommended_movie[7])
        
    with col4:
        st.image(recommended_movie_posters[8])
        st.caption(recommended_movie[8])
        
    with col5:
        st.image(recommended_movie_posters[9])
        st.caption(recommended_movie[9])
    


if not recommended_movie_posters:
        st.warning("No recommendations available.")
else:
        
    col1, col2, col3, col4, col5 = st.columns(5)
    for i in range(min(5, len(recommended_movie_posters))):
        with col1:
            if recommended_movie_posters[i] != "":
                    st.image(recommended_movie_posters[i])
                    st.caption(recommended_movie[i])

col1, col2, col3, col4, col5 = st.columns(5)
for i in range(5, min(10, len(recommended_movie_posters))):
    with col1:
        if recommended_movie_posters[i] != "":
            st.image(recommended_movie_posters[i])
            st.caption(recommended_movie[i])
            
"""


import pickle
import streamlit as st
import requests
import pandas as pd
#from PIL import Image

movies = pd.read_csv("movies.csv")


#background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #e5e5f7 10px ), repeating-linear-gradient( #444cf755, #444cf7 );

page_bg_img = """
<style>
[data-testid= "stAppViewContainer"] {
background-image: url(https://images.unsplash.com/photo-1579548122080-c35fd6820ecb?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8fHx8fHx8MTY4MTMyNjA5Ng&ixlib=rb-4.0.3&q=80&utm_campaign=api-credit&utm_medium=referral&utm_source=unsplash_source&w=1080);
background-size: cover;
}

[data-testid="stHeader"]{
background-color: rgba(0, 0, 0, 0);
}

[data-testid="stToolbar"]{
right: 2rem;
}
</style> 
"""

st.markdown(page_bg_img, unsafe_allow_html=True)





final_df = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))




def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=6b07482f2fb6f5e6f6fec523ccb0586e&language=en-US"
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/original" + poster_path
    return full_path

def recommend(movie_name):
    movie_index = final_df[final_df["title"] == movie_name].index[0]
    distances = similarity[movie_index]
    index_list = list(enumerate(distances))
    similar_movie = sorted(index_list, reverse = True, key = lambda x: x[1])[1:11]
    
    recommended_movie_names = []
    recommended_movie_posters = []
    
    for i in similar_movie:
        # fetch the movie poster
        movie_id = final_df.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(final_df.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters



#image = Image.open('hollywood-records8386.logowik.com.webp')

#st.image(image, width=120)

st.title("Movie Recommender System")
st.subheader("By Anand Kumar")
#st.pydeck_chart(movies)

movie_list = final_df['title'].values
selected_movie = st.selectbox(
    "Input the name of a movie or choose one from the provided list",
    movie_list
)

if st.button('Recommend'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.caption(recommended_movie_names[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.caption(recommended_movie_names[1])
        

    with col3:
        st.image(recommended_movie_posters[2])
        st.caption(recommended_movie_names[2])
        
    with col4:
        st.image(recommended_movie_posters[3])
        st.caption(recommended_movie_names[3])
        
    with col5:
        st.image(recommended_movie_posters[4])
        st.caption(recommended_movie_names[4])

        
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[5])
        st.caption(recommended_movie_names[5])
    with col2:
        st.image(recommended_movie_posters[6])
        st.caption(recommended_movie_names[6])
        

    with col3:
        st.image(recommended_movie_posters[7])
        st.caption(recommended_movie_names[7])
        
    with col4:
        st.image(recommended_movie_posters[8])
        st.caption(recommended_movie_names[8])
        
    with col5:
        st.image(recommended_movie_posters[9])
        st.caption(recommended_movie_names[9])
    


