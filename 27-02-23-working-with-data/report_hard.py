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
#   Actor appearring in most movies: Judd Nelson
#   Actor with best average rating: Robert Stack
#   Actor with best average rating: Lloyd Bridges
#   Actor with best average rating: John Malkovich
#   Actor with best average rating: John Cusack
#   Actor with best average rating: Ving Rhames
#   Actor with best average rating: Peter Cullen
#   Actor with best average rating: Frank Welker
#   Actor with best average rating: Orson Welles
#   Least popular genre in the 1980's: horror
#   Least popular genre in the 1980's: action
#   Least popular genre in the 1980's: drama

#   NOTES:
# - What makes these records easy to work with?
#  
# - What makes these records difficult to work with? 
# 
#   === === === IMPORT STATEMENTS === === ==== 

from movie_data import movies

#   === === === CODE === === ==== 

def main():
    list, dictionary = [], {}
    actor_amountmovies = extracting_data(list, dictionary)
    actors_most_movies(actor_amountmovies)
    actor_ratings =  actor_and_ratings(actor_amountmovies)
    best_average_rating(actor_amountmovies, actor_ratings)
    genre_dict = genres()
    genre_dict_1980 = genre_1980(genre_dict)
    least_popular_genre_1980(genre_dict_1980) 

def extracting_data(list, dictionary):
    for movie in movies:
        list.append(movie['actors'])
    for actors in list:
        for actor in actors:
            if actor not in dictionary:
                dictionary[actor] = 0 
            dictionary[actor] += 1
    return dictionary

def actors_most_movies(dictionary):
    for actor, most_movies in dictionary.items():
        if most_movies == max(dictionary.values()):
            print('Actor appearring in most movies:', actor)
   
def actor_and_ratings(dictionary):
    ratings = {}
    for actor in dictionary.keys():
        for movie in movies:
            if actor in movie['actors']:
                if actor not in ratings:
                    ratings[actor] = 0
                ratings[actor] += movie['rating']
    return ratings

def best_average_rating(actor_amountmovies, actor_ratings):
    actor_movies_rating = list(map(lambda x, y, z: [x , y/z], actor_amountmovies.keys(), actor_ratings.values(), actor_amountmovies.values()))
    highest_rating = ['Leonardo DiCaprio ', 0]
    for rate in actor_movies_rating:
        if rate[1] > highest_rating[1]:
            highest_rating = rate
    for actor, average_rate in actor_movies_rating:
        if average_rate == highest_rating[1]:
            print('Actor with best average rating:', actor)

def genres(): 
    genre_dict = dict()
    for genre in movies:
        genre_dict.update({genre['genre']: 0})
    return genre_dict
    
def genre_1980(genre_dict):
    for movie in movies:
        if movie['year'] == 1980:
            genre_dict[movie['genre']] += 1
    return genre_dict        

def least_popular_genre_1980(genre_dict_1980):
    for key, value in genre_dict_1980.items():
        if value == min(genre_dict_1980.values()):
            print('Least popular genre in the 1980\'s:', key)
    
#   === === === IMPORT GUARD === === ==== 
if __name__ == '__main__':
    main()