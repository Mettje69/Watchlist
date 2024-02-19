import streamlit as st
import json

# Load movie data from JSON file
with open("pages/movies.json", "r") as json_file:
    movies = json.load(json_file)

    # Extract unique movie titles
    movie_titles = [movie["Title"] for movie in movies]

    # Select a movie
    # List of movie titles
    # movie_titles = ["Movie 1", "Movie 2", "Movie 3"]  # Replace with your list of movie titles

    # Search box with autocomplete functionality
    selected_movie_title = st.selectbox("Search for a Movie", options=movie_titles)



    # Find details of the selected movie
    selected_movie_details = None
    for movie in movies:
        if movie["Title"] == selected_movie_title:
            selected_movie_details = movie
            break

    if selected_movie_details is not None:
        st.header(selected_movie_details["Title"])
        st.image(selected_movie_details["Poster"])

        st.subheader("Movie Details")
        st.write(f"Year: {selected_movie_details['Year']}")
        st.write(f"Rated: {selected_movie_details['Rated']}")
        st.write(f"Released: {selected_movie_details['Released']}")
        st.write(f"Runtime: {selected_movie_details['Runtime']}")
        st.write(f"Genre: {selected_movie_details['Genre']}")
        st.write(f"Director: {selected_movie_details['Director']}")
        st.write(f"Writer: {selected_movie_details['Writer']}")
        st.write(f"Actors: {selected_movie_details['Actors']}")
        st.write(f"Language: {selected_movie_details['Language']}")
        st.write(f"Country: {selected_movie_details['Country']}")
        st.write(f"Awards: {selected_movie_details['Awards']}")

        st.subheader("Plot")
        st.write(selected_movie_details["Plot"])

        st.subheader("Ratings")
        for rating in selected_movie_details["Ratings"]:
            st.write(f"{rating['Source']}: {rating['Value']}")

        st.subheader("Additional Information")
        st.write(f"Metascore: {selected_movie_details['Metascore']}")
        st.write(f"IMDb Rating: {selected_movie_details['imdbRating']}")
        st.write(f"IMDb Votes: {selected_movie_details['imdbVotes']}")
        st.write(f"IMDb ID: {selected_movie_details['imdbID']}")
        st.write(f"Type: {selected_movie_details['Type']}")
        st.write(f"DVD: {selected_movie_details['DVD']}")
        st.write(f"BoxOffice: {selected_movie_details['BoxOffice']}")
        st.write(f"Website: {selected_movie_details['Website']}")
        st.write(f"Response: {selected_movie_details['Response']}")
    else:
        st.write("Movie not found!")
