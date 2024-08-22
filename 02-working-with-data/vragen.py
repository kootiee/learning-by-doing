# def main():
#     selected_program = interface()
#     movie_data = extracting_movie_data(movies)
#     program_actions(selected_program)
#     list_movie_name_year(movie_data)


# def interface():
#     print('╔══════════════════════════════════════════════════╗')
#     print('║                         MENU                     ║')
#     print('╠══════════════════════════════════════════════════╣')
#     print('║ 1 - List of the names and years of all movies.   ║')
#     print('╠══════════════════════════════════════════════════╣')
#     print('║ 2 - Search by actor.                             ║')
#     print('╠══════════════════════════════════════════════════╣')
#     print('║ 3 - Search by genre.                             ║')
#     print('╠══════════════════════════════════════════════════╣')
#     print('║ 4 - Add a movie to the database.                 ║')
#     print('╠══════════════════════════════════════════════════╣')
#     print('║ 5 - Quit program.                                ║')
#     print('╚══════════════════════════════════════════════════╝')

#     selected_program = int(input(' What action do you want to take? \n - Menu option: '))
#     return selected_program

# def extracting_movie_data(movies):
#     movie_data = list(movies)
#     return movie_data
 
# def program_actions(selected_program):
#     pass
    
# def list_movie_name_year(movie_data):
#     list_movie_year = []
#     for movie in movie_data:
#         list_movie_year + [movie['title'], movie['year']]
#     print(list_movie_year) #?

# if __name__ == '__main__':
#     main()

[{'title': 'Star Wars Episode IV: A New Hope', 'actors': ['Mark Hamill', 'Harrison Ford', 'Carrie Fisher', 'Alec Guiness'], 'year': 1977, 'genre': 'science fiction', 'rating': 7}, {'title': 'Star Wars Episode I: The Phantom Menace', 'actors': ['Liam Neeson', 'Ewan McGregor', 'Natalie Portman', 'Jake Lloyd', 'Brian Blessed'], 'year': 1999, 'genre': 'science fiction', 'rating': 3}, {'title': 'Star Trek IV: The Voyage Home', 'actors': ['William Shatner', 'Leonard Nimoy', 'Michelle Nichols'], 'year': 1986, 'genre': 'science fiction', 'rating': 8}, {'title': 'Airplane!', 'actors': ['Leslie Nielsen', 'Robert Stack', 'Lloyd Bridges'], 'year': 1980, 'genre': 'comedy', 'rating': 9}, {'title': 'The Naked Gun: From The Files Of Police Squad!', 'actors': ['Leslie Nielsen', 'O. J. Simpson', 'Priscilla Presley'], 'year': 1988, 'genre': 'comedy', 'rating': 8}, {'title': 'Leprechaun', 'actors': ['Warwick Davis', 'Jennifer Aniston'], 'year': 1993, 'genre': 'horror', 'rating': 6}, {'title': 'Leprechaun 4: In Space', 'actors': ['Warwick Davis'], 'year': 1996, 'genre': 'horror', 'rating': 10}, {'title': 'Flash Gordon', 'actors': ['Brian Blessed', 'Timothy Dalton', 'Max von Sydow'], 'year': 1980, 'genre': 'science fiction', 'rating': 6}, {'title': 'The Rock', 'actors': ['Nicolas Cage', 'Sean Connery', 'Ed Harris', 'Michael Biehn'], 'year': 1996, 'genre': 'action', 'rating': 8}, {'title': 'Con Air', 'actors': ['Nicolas Cage', 'John Malkovich', 'John Cusack', 'Steve Buscemi', 'Ving Rhames'], 'year': 1997, 'genre': 'action', 'rating': 9}, {'title': 'Airheads', 'actors': ['Brendan Fraser', 'Adam Sandler', 'Steve Buscemi', 'Judd Nelson', 'Lemmy Kilmister'], 'year': 1994, 'genre': 'comedy', 'rating': 5}, {'title': 'The Breakfast Club', 'actors': ['Judd Nelson', 'Emilio Estevez', 'Ally Sheedy', 'Molly Ringwald'], 'year': 1985, 'genre': 'drama', 'rating': 6}, {'title': 'Wargames', 'actors': ['Matthew Broderick', 'Ally Sheedy'], 'year': 1983, 'genre': 'drama', 'rating': 8}, {'title': 'Godzilla', 'actors': ['Matthew Broderick', 'Jean Reno'], 'year': 1998, 'genre': 'action', 'rating': 6}, {'title': 'The Transformers: The Movie', 'actors': ['Peter Cullen', 'Frank Welker', 'Leonard Nimoy', 'Judd Nelson', 'Robert Stack', 'Orson Welles'], 'year': 1986, 'genre': 'action', 'rating': 9}]

