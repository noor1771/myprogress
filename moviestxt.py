# Import the spaCy library
import spacy

# Load the English medium-sized language model
nlp = spacy.load('en_core_web_md')

# Import the os module
import os

# Define the file path for the movies text file
file_path = os.path.expanduser('~/Downloads/movies.txt')

# Create an empty dictionary to store movie titles and descriptions
movies_dict = {}

# Open the movies text file for reading
with open(file_path, 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Split each line into two parts using the colon ':' as the separator
        line = line.strip().split(":", 1)
        # Extract the movie title and description
        movie, description = line[0], line[1]
        # Store the title and description in the movies_dict dictionary
        movies_dict[movie.strip()] = description.strip()

# Create a dictionary to store spaCy processed descriptions for each movie
movies_nlp = {movie: nlp(description) for movie, description in movies_dict.items()}

# Define a function to find the movie with the highest similarity to an input description
def which_movie(x):
    # Process the input description using spaCy
    x_nlp = nlp(x)
    
    # Initialize variables to keep track of the top similarity and movie
    top_similarity = -1.0
    top_movie = nlp(x)  # Initialize with the input description
    
    # Iterate through the movies in movies_dict
    for movie, description in movies_dict.items():
        # Calculate the similarity between the input description and each movie's description
        similarity = movies_nlp[movie].similarity(x_nlp)
        
        # Update the top_similarity and top_movie if a higher similarity is found
        if similarity > top_similarity:
            top_similarity = similarity
            top_movie = movie
    
    # Return the movie with the highest similarity and its similarity score
    return top_movie, top_similarity

# Example usage: Input a description and find the best matching movie
description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."
best_movie, similarity_score = which_movie(description)

# Print the result
print(f"The movie that best matches the description is '{best_movie}' with a similarity score of {similarity_score:.2f}")
