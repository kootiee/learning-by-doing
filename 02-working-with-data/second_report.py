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
# - This program will import the movie data, and print the following information to the screen:
#   Total number of movies: 15
#   Average rating of movies: 7.2
#   Best movie: Leprechaun 4: In Space
#   Worst movie: Star Wars Episode I: The Phantom Menace


#   === === === IMPORT STATEMENTS === === ==== 


from movie_data import movies


#   === === === CODE === === ====


def main():
    ratings = rating(movies)
    best_movie = best_movies(movies)
    worst_movie = worst_movies(movies)
    printing(movies, ratings, best_movie, worst_movie)


def rating(movie_list):
    rating_list = []
    for movie in movie_list:
        rating_list.append(movie['rating'])
    return rating_list


def best_movies(movie_list):
    best_movie = {'rating' : 0}
    for movie in movie_list:
        if movie['rating'] > best_movie['rating']:
            best_movie = movie
    return best_movie
    

def worst_movies(movie_list):
    worst_movie = {'rating' : 10}
    for movie in movie_list:
        if movie['rating'] < worst_movie['rating']:
            worst_movie = movie
    return worst_movie


def printing(movie_list, ratings, best_movie, worst_movie):
    print('Total number of movies:', len(movie_list))
    print('Average rating of movies:', sum(ratings) / len(movie_list))
    print('Best movie:', best_movie['title'])
    print('Worst movie:', worst_movie['title'])


#   === === === IMPORT GUARD === === ==== 

if __name__ == '__main__':
    main()
