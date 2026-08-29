movies = ["Inception", "The Matrix", "Interstellar"]
new_movie = input("Enter a new movie name: ")
if new_movie in movies:
    print("Already Added! ")
else:
    movies.append(new_movie)
print("Alphabetical Playlist:",sorted(movies))