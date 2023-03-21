#   === === === Working With Files === === ==== 

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
#    -  After you've added a movie to your database, you need to save that new movie to the text file. If you add a movie, it needs to be visible in subsequent runs of your program.
#    -  Quit : Ends the program.


#   === === === IMPORT STATEMENTS === === ==== 

from movie_data import movie_data

#   === === === CODE === === ==== 

def main():
    option = 0
    while option <= 4:
        data_movie = movie_data()
        option = menu()
        chosen_option(option, data_movie)
    print(' You have chosen option 5. The program closes. Have a nice day!''\n''\n', 67 * "-", '\n')
    
def menu():
    print('\n', 30 * "-" , "MENU" , 30 * "-", '\n''\n', "1. Menu Option 1 - Display all movies")
    print(" 2. Menu Option 2 - Search movies by actor")
    print(" 3. Menu Option 3 - Search movies by genre")
    print(" 4. Menu Option 4 - Add movie")
    print(" 5. Exit",'\n')
    option = int(input('  What action do you want to take?\n> Menu Option: '))
    print('\n', 67 * "-", '\n')
    return option

def chosen_option(option, data_movie):
    if option == 1: 
        list_movie(data_movie)
    elif option == 2:
        actor_search(data_movie)
    elif option == 3:
        genre_search(data_movie)
    elif option == 4:
        add_movie(data_movie)
    elif option >= 6:
        option = int(input(' You must make a choice from 1 to 5. Choose a Menu Option: '))
    return option

def list_movie(data_movie):
    for movie in data_movie:
        print('-', movie['title']+ ',', movie['year'])

def actor_search(data_movie):
    actor = input('Display all movies. Search by actor:\n> ').title()
    for movie in data_movie:
        if actor in movie['actors']:
            print('-', movie['title'] + ',', movie['year'])
    return actor_not_found(actor, data_movie)

def actor_not_found(actor, data_movie):
    actor_not_found = []
    for movie in data_movie:
        if actor in movie['actors']:
            actor_not_found.append(actor)
    if actor_not_found == []:
        print('\nOur sincere apologies. An actor named', actor, 'doesn\'t exist in the database.')
    return actor    
    
def genre_search(data_movie):
    genre = input('Display all movies. Search by genre:\n> ').lower()
    for movie in data_movie:
        if genre in movie['genre']:
            print('-', movie['title'] + ',', movie['year'])
    return genre_not_found(genre, data_movie)

def genre_not_found(genre, data_movie):
    genre_not_found = []
    for movie in data_movie:
        if genre in movie['genre']:
            genre_not_found.append(genre)
    if genre_not_found == []:
        print('\nOur sincere apologies. An genre named', genre, 'doesn\'t exist in the database.')
    return genre  

def add_movie(data_movie):
    add_title = input('To add a new movie to the database enter the title:\n> ').capitalize()
    add_actor = ' '.join(input('To add a new movie to the database enter the actor(s):\n> ').title().split(', '))
    add_year = input('To add a new movie to the database enter the release year:\n> ')
    add_genre = input('To add a new movie to the database enter the genre:\n> ')
    add_rating = input('To add a new movie to the database enter the rating:\n> ')  
    return add_movie_to_database(data_movie, add_title, add_actor, add_year, add_genre, add_rating)

def add_movie_to_database(data_movie, add_title, add_actor, add_year, add_genre, add_rating):
    file = open('movie_data.txt', 'a')
    for item in [add_title, add_actor, add_year, add_genre, add_rating]:
        file.write('\n')
        file.write(item)
        
    file.close()

#   === === === IMPORT GUARD === === ==== 

if __name__ == '__main__':
    main()
