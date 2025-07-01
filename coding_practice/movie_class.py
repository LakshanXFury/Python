class Movie:
    def __init__(self, name, actor, genre):
        self.name = name
        self.actor = actor
        self.genre = genre

    def display(self):
        print("The movie name is :", self.name)
        print("The actor name is :", self.actor)
        print("The genre that the movie belong to is :", self.genre)


all_movies = []

while True:
    movie_name = input("What is the movie name ? ")
    actor_name = input("What is the Actor name ? ")
    genre_name = input("Which Genre does the movie belong to ? ")
    m = Movie(movie_name, actor_name, genre_name)
    all_movies.append(m)
    option = input("Do you want to enter one more movie ?? [Yes/No] ")
    if option.lower() == "no":
        break

for movies in all_movies:
    movies.display()
    print()
