movies = ["Interstellar", "Oppenheimer", "Arrival", "Inception", "Gladiator"]

new_movie = input("Enter another movie: ")

movies.append(new_movie) #user input for movie
movies.sort() #sort Alphabetically
movies.reverse() #Flip it and reverse it

print(movies)