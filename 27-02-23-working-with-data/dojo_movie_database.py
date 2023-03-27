#   === === === Working With Data === === ==== 

#   GOOD TO KNOW:
# - Record (also called a structure, struct, or compound data): 
#   A basic data structure. Records in a database or spreadsheet are usually called "rows". 
#   A record is a collection of fields, possibly of different data types, typically in a fixed number and sequence.
# - Records are provided. The exercise will be about sorting, searching, and altering those records. 
# - 'My First IMDB':
#   The Internet Movie Database (IMDb) is an online database containing information and statistics.
#   It's all about movies, TV shows and video games as well as actors, directors and other film industry professionals.


#   THE MISSION:
# -  This program will import the movie data, and then provide a menu of options to the user. 
#    The user can select an option, the program will do it, and afterwards the program should return to the main menu. The options are:
#    -  List : List the name and year of all movies, separated by a comma.
#    -  Actor Search : Prompt for an actor's name, then list the name and year of all their movies.
#    -  Genre Search : Prompt for a genre name, then list the name and year of every movie in that genre.
#    -  Add : Prompts for a title, actors, year, genre, and a rating, then adds that movie to the database in memory. This new movie should show up in the other searches.
#    -  Quit : Ends the program.

#   NOTES:
# - What makes these records easy to work with?
#  
# - What makes these records difficult to work with? 
# 
#   === === === IMPORT STATEMENTS === === ==== 

from movie_data import movies

#   === === === CODE === === ==== 

def main():
    data_movies = movies
    option = 0
    while option <= 4:
        option = menu()
        title_year_actors_genre = extracting_moviedata(data_movies)
        chosen_option(option, data_movies, title_year_actors_genre)
    print('\n'' You have chosen option 5. The program closes. Have a nice day!''\n''\n', 67 * "-", '\n')
    
def menu():
    print('\n', 30 * "-" , "MENU" , 30 * "-", '\n''\n', "1. Menu Option 1 - Display all movies")
    print(" 2. Menu Option 2 - Search movies by actor")
    print(" 3. Menu Option 3 - Search movies by genre")
    print(" 4. Menu Option 4 - Add movie")
    print(" 5. Exit",'\n')
    option = int(input(' What action do you want to take?\n> Menu Option: '))
    print('\n', 67 * "-", '\n')
    return option

def extracting_moviedata(data_movies):
    title_year_actors_genre = []
    for movie in data_movies:
        title_year_actors_genre.append([movie['title'], movie['year'], movie['actors'], movie['genre']])
    return title_year_actors_genre

def chosen_option(option, data_movies, title_year_actors_genre):
    if option == 1: 
        title_year_actors_genre = movies_year(title_year_actors_genre)
    elif option == 2:
        search_by_actor(title_year_actors_genre)
    elif option == 3:
        search_by_genre(title_year_actors_genre) 
    elif option == 4:
        data_movies = add_movie(data_movies)
    elif option >= 6:
        option = int(input(' You must make a choice from 1 to 5. Choose a Menu Option: '))
    return option
     
def movies_year(title_year_actors_genre):
    for movie_year in title_year_actors_genre:
        print('-', movie_year[0] + ',', movie_year[1]) 
    return title_year_actors_genre

def search_by_actor(title_year_actors_genre):
    search_actor = input('Display all movies. Search by actor:\n> ')
    search_actor = search_actor.title()
    for title, year, actors, genre in title_year_actors_genre:
        for actor in actors:
            if search_actor.title() in actor: 
                    print('-', title + ',', year)
    return not_found_search_by_actor(title_year_actors_genre, search_actor)

def not_found_search_by_actor(title_year_actors_genre, search_actor):
    actor_not_found = []
    for title, year, actors, genres in title_year_actors_genre:
        for actor in actors:
            if search_actor in actor:
                actor_not_found.append(actor) 
    if actor_not_found == []:
        print('\nOur sincere apologies. An actor named', search_actor, 'doesn\'t exist in the database.')
    return search_actor

def search_by_genre(title_year_actors_genre):
    search_genre = input('Display all movies. Search by genre:\n> ')
    search_genre = search_genre.lower()
    for title, year, actors, genres in title_year_actors_genre:
            if search_genre in genres: 
                    print('-', title + ',', year)
    return not_found_search_by_genre(title_year_actors_genre, search_genre)

def not_found_search_by_genre(title_year_actors_genre, search_genre):
    genre_not_found = []
    for title, year, actors, genres in title_year_actors_genre:
            if search_genre in genres:
                genre_not_found.append(genres) 
    if genre_not_found == []:
        print('\nOur sincere apologies. A genre named', search_genre, 'doesn\'t exist in the database.')
    return search_by_genre

def add_movie(data_movies):
    add_title = input('To add a new movie to the database enter the title:\n> ').capitalize()
    add_actor = input('To add a new movie to the database enter the actor(s):\n> ').title().split(', ')
    add_year = int(input('To add a new movie to the database enter the release year:\n> '))
    add_genre = input('To add a new movie to the database enter the genre:\n> ')
    add_rating = int(input('To add a new movie to the database enter the rating:\n> '))
    return add_movie_to_database(data_movies, add_title, add_actor, add_year, add_genre, add_rating)

def add_movie_to_database(data_movies, add_title, add_actor, add_year, add_genre, add_rating):
    new_movie = {}
    new_movie['title'] = add_title
    new_movie['actors'] = add_actor
    new_movie['year'] = add_year
    new_movie['genre'] = add_genre
    new_movie['rating'] = add_title
    data_movies.append(new_movie)
    return extracting_moviedata(data_movies)

#   === === === IMPORT GUARD === === ==== 
if __name__ == '__main__':
    main()