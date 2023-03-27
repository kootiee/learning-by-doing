def movie(title, actors, year, genre, rating):
    return {
    	"title": title,
    	"actors": actors,
    	"year": year,
    	"genre": genre,
    	"rating": rating
    }

movies = [
    movie("Star Wars Episode IV: A New Hope", ["Mark Hamill", "Harrison Ford", "Carrie Fisher", "Alec Guiness"], 1977, "science fiction", 7),
    movie("Star Wars Episode I: The Phantom Menace", ["Liam Neeson", "Ewan McGregor", "Natalie Portman", "Jake Lloyd", "Brian Blessed"], 1999, "science fiction", 3),
    movie("Star Trek IV: The Voyage Home", ["William Shatner", "Leonard Nimoy", "Michelle Nichols"], 1986, "science fiction", 8),
    movie("Airplane!", ["Leslie Nielsen", "Robert Stack", "Lloyd Bridges"], 1980, "comedy", 9),
    movie("The Naked Gun: From The Files Of Police Squad!", ["Leslie Nielsen", "O. J. Simpson", "Priscilla Presley"], 1988, "comedy", 8),
    movie("Leprechaun", ["Warwick Davis", "Jennifer Aniston"], 1993, "horror", 6),
    movie("Leprechaun 4: In Space", ["Warwick Davis"], 1996, "horror", 10),
    movie("Flash Gordon", ["Brian Blessed", "Timothy Dalton", "Max von Sydow"], 1980, "science fiction", 6),
    movie("The Rock", ["Nicolas Cage", "Sean Connery", "Ed Harris", "Michael Biehn"], 1996, "action", 8),
    movie("Con Air", ["Nicolas Cage", "John Malkovich", "John Cusack", "Steve Buscemi", "Ving Rhames"], 1997, "action", 9),
    movie("Airheads", ["Brendan Fraser", "Adam Sandler", "Steve Buscemi", "Judd Nelson", "Lemmy Kilmister"], 1994, "comedy", 5),
    movie("The Breakfast Club", ["Judd Nelson", "Emilio Estevez", "Ally Sheedy", "Molly Ringwald"], 1985, "drama", 6),
    movie("Wargames", ["Matthew Broderick", "Ally Sheedy"], 1983, "drama", 8),
    movie("Godzilla", ["Matthew Broderick", "Jean Reno"], 1998, "action", 6),
    movie("The Transformers: The Movie", ["Peter Cullen", "Frank Welker", "Leonard Nimoy", "Judd Nelson", "Robert Stack", "Orson Welles"], 1986, "action", 9),
]

