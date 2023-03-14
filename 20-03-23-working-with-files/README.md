# Working With Files

As I am fond of saying, all programs have three steps:
* input
* process
* output

So far we've concentrated on the middle step, process, which is super important. However, in most real world applications, input and output are if anything, *more* important. Some programs are 90% input and output. So we're going to start looking at that in more detail.

## Your Mission

Your mission this time is very similar to last time. We're going to be building the dojo_movie_database again! However, there are two differences.

1. You're not getting `movie_data.py`. This time, you're getting a text file, and you'll have to read that in, and process the text into records yourself. It's the same movies in the same order, your queries should give the same answers. However you'll have to read the file line by line, and put them in some sort of record structure.
2. After you've added a movie to your database, you need to save that new movie to the text file. If you add a movie, it needs to be visible in subsequent runs of your program. 

Now we've highlighted the differences, here's the specification:

* **dojo_movie_database.py :** This program will import the movie data, and then provide a menu of options to the user. The user can select an option, the program will do it, and afterwards the program should return to the main menu. The options are:
    1. *List :* List the name and year of all movies, separated by a comma.
    2. *Actor Search :* Prompt for an actor's name, then list the name and year of all their movies.
    3. *Genre Search :* Prompt for a genre name, then list the name and year of every movie in that genre.
    4. *Add :* Prompts for a title, actors, year, genre, and a rating, then adds that movie to the database. This new movie should show up in the other searches, every time the program is run.
    5. *Quit :* Ends the program.
    
# Restrictions
* The only things allowed in your program are:
    * imports
    * an import guard `if __name__ == '__main__': main()`
    * functions
    * constants
* You are not allowed other code or variables at the top level of your module. Inside functions however, you can do whatever you like.
* No global variables. At all. We do not accept The Gijs Scenario. :)
* Try to have no more than eight lines of code per function.
* You should not change the structure of the text file database. 
* You should be able to give your database file to another student, and have their program read it successfully.
