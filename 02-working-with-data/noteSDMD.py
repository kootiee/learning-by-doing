#   === === === Working With Data === === ==== 


#   THE MISSION:
# -  This program will import the movie data, and then provide a menu of options to the user. 
#    The user can select an option, the program will do it, and afterwards the program should return to the main menu. The options are:
#    -  List : List the name and year of all movies, separated by a comma.
#    -  Actor Search : Prompt for an actor's name, then list the name and year of all their movies.
#    -  Genre Search : Prompt for a genre name, then list the name and year of every movie in that genre.
#    -  Add : Prompts for a title, actors, year, genre, and a rating, then adds that movie to the database in memory. This new movie should show up in the other searches.
#    -  Quit : Ends the program.


#   === === === IMPORT STATEMENTS === === ==== 

from movie_data import movies

#   === === === CODE === === ==== 


def main():
    movie_data = extracting_movie_data(movies)
    selected_program = interface(movie_data)
    

def extracting_movie_data(movies):
    movie_data = list(movies)
    return movie_data


def interface(movie_data):
    print('''
    ╔══════════════════════════════════════════════════╗
    ║                         MENU                     ║
    ╠══════════════════════════════════════════════════╣
    ║ 1 - List of the names and years of all movies.   ║
    ╠══════════════════════════════════════════════════╣
    ║ 2 - Search by actor.                             ║
    ╠══════════════════════════════════════════════════╣
    ║ 3 - Search by genre.                             ║
    ╠══════════════════════════════════════════════════╣
    ║ 4 - Add a movie to the database.                 ║
    ╠══════════════════════════════════════════════════╣
    ║ 5 - Quit program.                                ║
    ╚══════════════════════════════════════════════════╝
    ''')

    selected_program = int(input(' What action do you want to take? \n - Menu option: '))
    program_actions(selected_program, movie_data)

 
def program_actions(selected_program, movie_data):
    while selected_program <= 5:
        if selected_program == 1:
            list_movie_name_year(movie_data)
        elif selected_program == 2:
            search_by_actor(movie_data)
        elif selected_program == 3:
            search_by_genre(movie_data)
        elif selected_program == 4:
            movie_data = getting_info_for_new_movie(movie_data)     
        elif selected_program == 5:
            print(' - Option 5: Ends the program. Have a nice day!')
            break

    
    
def list_movie_name_year(movie_data):
    print('\nOption 1 - A list of the name and year of all movies:')
    for movie in movie_data:
        print(' -', movie['title'] + ',', movie['year'])
    interface(movie_data)

def search_by_actor(movie_data):
    not_found = 'true'
    chosen_actor = input('\n Option 2 - Search by actor to get a list of the name and year of all their movies. Choose your actor: ')
    for movie in movie_data:
        for actor in movie['actors']:
            if chosen_actor.title() == actor:
                print(' -', movie['title'] + ',', movie['year'])
                not_found = 'false'
    movie_or_genre_not_found(movie_data, not_found)

def search_by_genre(movie_data):
    not_found = 'true'
    chosen_genre = input('\n Option 3 - Search by genre to get a list of the name and year of every movie in that genre. Choose your genre: ')
    for movie in movie_data:
        if chosen_genre.lower() == movie['genre']:
                print(' -', movie['title'] + ',', movie['year'])
                not_found = 'false'
    movie_or_genre_not_found(movie_data, not_found)

def movie_or_genre_not_found(movie_data, not_found):
    if not_found == 'true':
        print(' - Our sincere apologies. It doesn\'t exist in the database.')
    interface(movie_data)

def getting_info_for_new_movie(movie_data):
    title = input('\n Option 4 - To add a new movie to the database enter the title: ').capitalize()
    actors_list = []
    amount = int(input(' - Enter how many actors plays in this new movie: '))
    for actors in range(amount):
        actors_list.append(input(' - Enter the actor: ').title())
    year = int(input(' - To add a new movie to the database enter the year: '))
    genre = input(' - To add a new movie to the database enter the genre: ').lower()
    rating = input(' - To add a new movie to the database enter the rating: ')
    adding_movie_to_database(title, actors_list, year, genre, rating, movie_data)

def adding_movie_to_database(title, actors_list, year, genre, rating, movie_data):
    dict_new_movie = {}
    dict_new_movie['title'] = title
    dict_new_movie['actors'] = actors_list
    dict_new_movie['year'] = year
    dict_new_movie['genre'] = genre
    dict_new_movie['rating'] = rating
    movie_data.append(dict_new_movie)
    interface(movie_data)



#   === === === IMPORT GUARD === === ==== 
    

if __name__ == '__main__':
    main()