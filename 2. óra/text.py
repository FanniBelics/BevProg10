
def main():
    genre = 'Japanese animation'
    title = "Howl's moving Castle"
    author = 'Miyazaki Hayao'
    language = 'Japanese'
    mainC = 'Sophie'
    year = 2004
    imdb  = 8.2
    mins = 119
    job = 'hatmaker'
    text = """    {0} is a {1} film, written by {2}.
    The film was produced in {3}. It's IMDB rating is {4}.
    The main character's name is {5} who is a {6}.
    The film is {7} mins long. The original language is {8}."""

    print(text.format(title,genre, author, year, imdb, mainC, job, mins, language))

if __name__ == "__main__":
    main()