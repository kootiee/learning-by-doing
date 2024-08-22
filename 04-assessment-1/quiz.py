#   === === === ASSESSMENT === === ===


#   THE MISSION:
#   - A game where you ask the player some quiz questions, check their answers, score them, and keep a high score for the next game.
#   - questions.txt contains trivia questions. They're laid out in the following order:
#       - The text of the actual question.
#       - A list of possible answers, separated by commas.
#       - The correct answer.


#   TO DO:
#   - Parsing questions.txt
#   - Select five questions at random
#   - Display the high score, along with the name of the high scorer.
#   - Ask these questions to the player:
#       - You'll need to show the question, and all four possible answers.
#       - The answers must be in a random order; they can't always be displayed in the same order as they are in the text file.
#       - The player should be able to enter something short to pick their answer (option A, B, C, D). 
#   - After the player has answered five questions, display their score.
#   - If their score is higher than or equal to the high score, they get to enter their name, and they're displayed as the high scorer at the start of the next run of the program.


#   RESTRICTIONS:
#   - Allowed:
#       - Imports
#       - Import guard - if __name__ == "__main__": main()
#       - Functions
#       - Constants
#   - Not allowed:
#       - Global variables
#       - Edit questions.txt


#   COMMENTS:
#1  - Open text file for reading. If the file does not exist, it will raise the I/O error. And the second error is the ValueError. This happens when the file is there but the code can't read it. 
#2  - The readlines() method returns a list containing each line in the file as a list item.
#3  - The iteration of the for loop: start 0, size of quiz_data_unfiltered and steps of three.
#4  - Append to quiz_data_per_question > per_question is a list of three items of the quiz_data_unfiltered.
#5  - One item of the quiz_data_per_question contains a list of question[0], possible answers[1] and a correct answer[2].
#6  - The sample() method is used to return the required list of items from a given sequence. This method does not allow duplicate elements in a sequence.
#7  - The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.
#8  - 'w+' is for both write and read mode


#benamingen
#functie verderling ;)


#   === === === CODE === === ===
import random


def main():
    highscore, highscore_player = score_file_handling()
    player_name = menu(highscore, highscore_player)
    quiz_data_per_question = file_handling()
    quiz_list_filtered = parsing_per_questions(quiz_data_per_question )
    list_of_five_questions = get_five_questions(quiz_list_filtered)
    player_score = quiz(list_of_five_questions)
    high_score_handling(player_score, player_name, highscore)
    get_score(player_name, player_score, highscore)



def score_file_handling():
    try:
        with open('score.txt', 'r') as score_file:
            highscore = int(score_file.readline())
            highscore_player = score_file.readline()
    except (IOError, ValueError): #1
        with open('score.txt', 'w+') as score_file:
            score_file.write('0\nbe the first!')
            highscore = int(score_file.readline())
            highscore_player = score_file.readline()
    return highscore, highscore_player



def menu(highscore, highscore_player):
    print(8 * ' === ', 'QUIZ', 8 * ' === ', '\n')
    print('''    Welcome! This quiz put the fun into learning.
    Your knowledge will be tested regarding a variety of subjects.
    But first let's check the high score! :) \n''')
    print('    > High scorer:', highscore)
    print('    > High score:', highscore_player)
    print('\n', 17 * ' === ', '\n')
    player_name = input('Are you ready? Enter your name to play :) -> ')
    return player_name



def file_handling():
    with open('questions.txt', 'r') as quiz_file:
        quiz_data_unfiltered = quiz_file.readlines() #2
        quiz_data_per_question = []
        for item in range(0, len(quiz_data_unfiltered), 3): #3
            per_question = quiz_data_unfiltered[item : item + 3] 
            quiz_data_per_question.append(per_question) #4
    return quiz_data_per_question



def parsing_per_questions(quiz_data_per_question):
    quiz_list_filtered = []
    for item in quiz_data_per_question: #5
        question, possible_answer, correct_answer = item[0], item[1], item[2]
        per_question_dict = {
            'question': question.strip('\n'),
            'possible_answers': possible_answer.strip('\n').split(','),
            'correct_answer': correct_answer.strip('\n')
            }
        quiz_list_filtered.append(per_question_dict)
    return quiz_list_filtered



def get_five_questions(quiz_list_filtered):
    return random.sample(quiz_list_filtered, 5) #6



def quiz(list_of_five_questions):
    player_score = 0
    for question in list_of_five_questions:
        print('\n' + question['question'])
        for (letter, possible_answer) in zip(['a - ', 'b -', 'c -', 'd -'], question['possible_answers']): #7
            print(letter, possible_answer)
        chosen_letter = input('Fill in the correct answer (option a, b, c or d): ').lower()
        if question['possible_answers'][{'a': 0, 'b':1, 'c':2, 'd':3}[chosen_letter]].lstrip() == question['correct_answer']:
            print('You guessed right! Yeah, you gained a point :)')
            player_score += 1
        else:
            print('> Oh no, the correct answer is:', question['correct_answer'])
    return player_score



def high_score_handling(player_score, player_name, highscore):
    if int(player_score) >= int(highscore):
        with open('score.txt', 'w+') as score_file: #8
            score_file.write(str(player_score))
            score_file.write('\n')
            score_file.write(player_name)



def get_score(player_name, player_score, highscore):
    if int(player_score) >= int(highscore):
        print('\n', 8 * ' === ', 'SCORE', 8 * ' === ', '\n')
        print(' > Total amount of points:', player_score)
        print(' > CONGRATZ! You beat the highscore', player_name)
        print('\n', 17 * ' === ', '\n')
    else:
        print('\n', 8 * ' === ', 'SCORE', 8 * ' === ', '\n')
        print('  You did not beat the highscore with a total amount of points of', player_score)
        print('  Let\'s play again! :)')
        print('\n', 17 * ' === ', '\n')


#   === === === IMPORT GUARD === === ==== 

if __name__ == '__main__':
    main()



#   === === === NOTES === === ==== 


