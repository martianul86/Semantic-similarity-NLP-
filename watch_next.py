import spacy

# Loading method
nlp = spacy.load('en_core_web_md')

# Creating the function
def next_movie(description):
    movies = open("movies.txt", "r")
    # Initialize a list to store the movies
    split_list = []

    # Split movies into title and description
    for i in movies:
        split_list.append(i.split(':'))

    # Get number of movies in text file
    count = len(split_list)
    # Declare a list to store similarity values
    similarity_list = []

    model_sentence = nlp(description)

    # Iterate as many times as the number of movies in the text file
    for i in range(0, count):
        similarity_list.append(nlp(split_list[i][1]).similarity(model_sentence))

    # Get the maximum similarity value
    max_similarity = max(similarity_list)
    # Get index of highest similarity value
    max_similarity_index = similarity_list.index(max_similarity)

    # Return similar movie title
    return split_list[max_similarity_index][0]

# Movie description to comapare with
hulk_description = """Will he save
their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the
planet Sakaar where he is sold into slavery and trained as a gladiator."""

print("Next Movie Recommended to Watch: " + next_movie(hulk_description))