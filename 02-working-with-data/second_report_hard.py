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
#   Actor appearring in most movies: Julia Roberts
#   Actor with best average rating: Jean Claude Van Damme
#   Least popular genre in the 1980's: music videos


#   === === === IMPORT STATEMENTS === === ==== 


from movie_data import movies


#   === === === CODE === === ==== 


def main():
    actors_dict = get_actor_moviecount_dict(movies)
    print_most_movies(actors_dict)
    rating_dict = get_actor_rating(movies)
    average_dict = get_actor_average(actors_dict, rating_dict)
    print_best_average(average_dict)
    mark_genre = get_genres_1980_1989(movies)
    least_popular_genre(mark_genre)


def get_actor_moviecount_dict(movie_list):
    actors_dict = {}
    for film in movie_list:
        for actor in film['actors']:
            if actor not in actors_dict:
                actors_dict[actor] = 1
            else:
                actors_dict[actor] += 1
    return actors_dict


def print_most_movies(actors_dict):
    max_count_films = max(actors_dict.values())
    for actor in actors_dict:
        if actors_dict[actor] == max_count_films:
            print('Actor appearring in most movies:', actor)


def get_actor_rating(movie_list):
    rating_dict = {}
    for film in movie_list:
        for actor in film['actors']:
            if actor not in rating_dict:
                rating_dict[actor] = film['rating']
            else:
                rating_dict[actor] += film['rating']
    return rating_dict


def get_actor_average(actors_dict, rating_dict):
    average_dict = {}
    for actor in actors_dict: 
        average_dict[actor] = rating_dict[actor] / actors_dict[actor]
    return average_dict


def print_best_average(average_dict):
    max_average_rating = max(average_dict.values())
    for actor in average_dict:
        if average_dict[actor] == max_average_rating:
            print('Actor with best average rating: ', actor)


def get_genres_1980_1989(movie_list):
    genre_dict = {}
    for film in movie_list:
        if 1980 <= film['year'] < 1990:
            if film['genre'] not in genre_dict:
                genre_dict.update({film['genre'] : 1})
            else:
                genre_dict[film['genre']] += 1
    return genre_dict


def least_popular_genre(mark_genre):
    mark_genres = min(mark_genre.values())
    for genre in mark_genre:
        if mark_genre[genre] == mark_genres:
            print('Least popular genre in the 1980\'s: ', genre)

        
#   === === === IMPORT GUARD === === ==== 


if __name__ == '__main__':
    main()

