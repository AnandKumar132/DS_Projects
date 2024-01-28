# DS_Projects
This repository is dedicated to hosting Data Science-related projects.
Movie Recommender System Web App: A Journey into Data and Recommendations

Embark on a cinematic journey with my Movie Recommender System Web App! I've integrated the power of data preprocessing, model creation, and web app development to bring you personalized movie recommendations. Let's dive into the key components of this project.

Data Preprocessing:
Cleaning and organizing data is the first step to success. Leveraging pandas and sklearn, I meticulously cleaned and preprocessed the dataset, handling missing values and ensuring data consistency. Stemming and root word extraction were applied to streamline the textual information, and Count Vectorization was used to convert movie descriptions into numerical vectors.

Model Creation:
The heart of the system lies in the recommendation model. Through a combination of techniques like stemming, root words, and vectorization, I transformed movie data into a format suitable for analysis. The bag-of-words technique allowed me to capture the essence of each movie, and the cosine similarity metric became the magic wand to measure the similarity between vectors.

Web App Development:
Turning the model into an interactive experience is where Streamlit comes into play. The web app is not just functional but visually engaging. Utilizing the TMDB API, I fetched real-time movie data, and the pickle library ensured seamless integration of the model. Requests library facilitated communication with external APIs, creating a dynamic and responsive user interface.

User Interface Design:
Aesthetics matter! I enhanced the user interface with Streamlit intuitive features, offering a visually pleasing and user-friendly experience. The background image sets the cinematic tone, creating a seamless blend of technology and art.

How it Works:
Input Movie Name: Users can select a movie from the dropdown list or input their favorite movie.
Recommendation: With a click of a button, the magic unfolds. The system uses a sophisticated model to recommend 10 movies similar to the user's selection.
Visual Delight: Movie posters accompany each recommendation, creating an immersive and visually delightful experience.

Key Achievements:
Successfully implemented a recommendation system using advanced NLP techniques.
Seamlessly integrated external API (TMDB) for real-time movie data.

Results and Impact:
The Movie Recommender System has received positive feedback for its accuracy and user-friendly design. Users are delighted with the personalized recommendations and the immersive visual experience.
