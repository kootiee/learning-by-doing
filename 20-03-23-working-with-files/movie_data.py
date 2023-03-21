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
# - You're getting a text file, and you'll have to read that in, and process the text into records yourself. 
#   It's the same movies in the same order, your queries should give the same answers. 
#   However you'll have to read the file line by line, and put them in some sort of record structure.
#   After you've added a movie to your database, you need to save that new movie to the text file. 
#   If you add a movie, it needs to be visible in subsequent runs of your program.


#   === === === IMPORT STATEMENTS === === ==== 

#   Does not apply

#   === === === CODE === === ==== 

def movie_data():
    moviedata_list = extracting_moviedata()
    per_movie_list = split_moviedata_list(moviedata_list)
    moviedata = split_moviedata_dictionary(per_movie_list)
    return moviedata
    

def extracting_moviedata():    
    file = open('movie_data.txt', 'r')
    grimy_moviedata_list = file.readlines()
    moviedata_list = [i.strip() for i in grimy_moviedata_list]
    return moviedata_list

def split_moviedata_list(moviedata_list):
    per_movie_list = []
    while len(moviedata_list) > 5:
        movie = moviedata_list[:5]
        per_movie_list.append(movie)
        moviedata_list = moviedata_list[5:]
    per_movie_list.append(moviedata_list)
    return per_movie_list

def split_moviedata_dictionary(per_movie_list):
    moviedata = []
    data_sequence = ['title', 'actors', 'year', 'genre', 'rating']
    for movie in per_movie_list:
        movie_dict = zip(data_sequence, movie)
        moviedata.append(dict(movie_dict))
    return moviedata

#   === === === IMPORT GUARD === === ==== 

if __name__ == '__main__':
    movie_data()
