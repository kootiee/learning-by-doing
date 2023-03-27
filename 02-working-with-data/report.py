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

#   NOTES:
# - What makes these records easy to work with?
#  
# - What makes these records difficult to work with? 
#  

#   === === === IMPORT STATEMENTS === === ==== 

from movie_data import movies

#   === === === CODE === === ==== 

def main():
    title_list = number_of_movies()
    rating_list = average_of_movies(title_list)
    title_number_list = best_movie(title_list, rating_list)
    worst_movie(title_number_list)

def number_of_movies(): #naming convention -> look at the return.
    title_list = []
    for title in movies:
        title_list.append(title['title'])
    print('Total number of movies:',len(title_list)) #It is better to not print it whithin the function. Why? If it is a large function, you can use it efficient -> You can make a different function or do it in the main(). You can also put it in the function that calls the function.
    return title_list

def average_of_movies(title_list):
    rating_list = []
    for rate in movies:
        rating_list.append(rate['rating'])
    print('Average rating of movies:', sum(rating_list) / len(title_list))
    return rating_list

def best_movie(title_list, rating_list):
    title_number_rating = list(map(lambda x, y: [x , y], title_list, rating_list))
    highest_rating = ['Sad', 0]
    for rate in title_number_rating:
        if rate[1] > highest_rating[1]:
            highest_rating = rate 
    print('Best movie:', highest_rating[0])
    return title_number_rating

def worst_movie(title_number_list):
    lowest_rating = ['Coco', 10]
    for rate in title_number_list:
        if rate[1] < lowest_rating[1]:
            lowest_rating = rate
    print('Worst movie:', lowest_rating[0])


#   === === === IMPORT GUARD === === ==== 

if __name__ == '__main__':
    main()
