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
# - This program will import the movie data, and print the answer to the following question. The answer is one single movie title, with double quotes. The question is: 
# - Matthew Broderick sucks. He makes every movie one point worse. 

#   Judd Nelson is harsh. He makes every movie one point better. Moreover, he's so cool, that his coolness is contagious and does not obey the laws of space-time. 
#   Anyone who has ever been in a movie with Judd Nelson, makes every other movie they're in one point better. 

# - In other words:
#   note1 ----> Matthew Broderick ----> rating of the movie goes down with one point. 
#   note2 ----> Judd Nelson ----> rating of the movie goes up with one point.
#   note3 ----> Actor who has acted with Judd Nelson ----> rating of the movie goes up with one point.

# - With all that in mind: 
#   What's the best Ally Sheedy movie?
#   The best Ally Sheedy movie is: Wargames

#   NOTES:
# - What makes these records easy to work with?
#  
# - What makes these records difficult to work with? 
# 
#   === === === IMPORT STATEMENTS === === ==== 

from movie_data import movies

#   === === === CODE === === ==== 

def main():
    movies_ratings = movie_ratings()
    note1_movies_ratings = Matthew_Broderick(movies_ratings)
    note2_movies_ratings = Judd_Nelson(note1_movies_ratings)
    actors = acted_with_JN()
    note3_movies_ratings = final_ratings(note2_movies_ratings, actors)
    Ally_movies_rating = Ally_movies(note3_movies_ratings)
    best_Ally_movie(Ally_movies_rating)
    

def movie_ratings():
    movies_ratings = dict()
    for rating in movies:
        movies_ratings.update({rating['title']: rating['rating']})
    return movies_ratings

def Matthew_Broderick(movies_ratings):
    for movie in movies:
        if 'Matthew Broderick' in movie['actors']:
            movies_ratings[movie['title']] -= 1
    return movies_ratings

def Judd_Nelson(note1_movies_ratings):
    for movie in movies:
        if 'Judd Nelson' in movie['actors']:
            note1_movies_ratings[movie['title']] += 1
    return note1_movies_ratings

def acted_with_JN():
    actors = []
    for movie in movies:
        if 'Judd Nelson' in movie['actors']:
            for actor in movie['actors']:
                if actor != 'Judd Nelson':
                    actors.append(actor)
    return actors

def final_ratings(note2_movies_ratings, actors):
    for movie in movies:
            for actor in actors:
                if actor in movie['actors'] and 'Judd Nelson' not in movie['actors']:
                    note2_movies_ratings[movie['title']] += 1
    return note2_movies_ratings

def Ally_movies(note3_movies_ratings):
    Ally_movies_list, Ally_movies_rating  = [], []
    for movie in movies:
        if 'Ally Sheedy' in movie['actors']:
            Ally_movies_list.append(movie['title'])
    for title in Ally_movies_list:
        Ally_movies_rating.append([title, note3_movies_ratings[title]])
    return Ally_movies_rating

def best_Ally_movie(Ally_movies_rating):
    highest_rating = ['Ally Sheedy', 0]
    for rate in Ally_movies_rating:
        if rate[1] > highest_rating[1]:
            highest_rating = rate
    for title, rating in Ally_movies_rating:
        if rating == highest_rating[1]:
            print('The best Ally Sheedy movie is:', title)
 
#   === === === IMPORT GUARD === === ==== 
if __name__ == '__main__':
    main()
