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


#   === === === CODE === === ===

def main():
    file_handling()



def per_question():
    per_question_dict = {'quiz' : 'no_value', 'possible_answer' : 'no_value', 'correct_answer' : 'no_value'}
    return per_question_dict



def file_handling():
    with open('questions.txt') as quiz_file:
        per_question_dict = per_question()
        questions_list = []
        for line in quiz_file: #teller van drie?(bekijk comments. Heb je eerder gecodeerd!) | handmatig met readline() (3x) |  
            for key in per_question_dict:
                per_question_dict[key] = line
            questions_list.append(per_question_dict) 
            per_question_dict = per_question()
    print(questions_list)



#   === === === IMPORT GUARD === === ==== 



if __name__ == '__main__':
    main()



#   === === === NOTES === === ==== 

# Bekijk goed de loop! Hoe itereert die?

# while loop - want je weet niet wanneer het einde nadert
    # readline() 3x

#als de lengte van de txt file weet, kan je delen door middel van drie! Zo weet je hoe vaak je moet loopen. 

#add dict to questions_dictionary
#pas op! per_question_dict verandert no_value. Mogelijk in een functie zetten icm. main()
#zie voorbeeld van Robin

# quiz = quiz_text.readline().splitlines() #This splits one string on line separators and returns a list of lines without those separators
# per_question = []
# for item in range(0, len(quiz), 3): #Loop through code a specified number of times. Start at 0, ends before the integer value of the length of the quiz. The third value is the step value. Item is 3, increased by 3 every loop.
#     split_questions = quiz[item : item+3] #split the quiz by slicing. Every time this variable contains a list with question, possible answers and answer.
#     per_question.append(split_questions)
# print(quiz)

# per_question = {}
# for item in range(0, len(quiz), 3): #Loop through code a specified number of times. Start at 0, ends before the integer value of the length of the quiz. The third value is the step value. Item is 3, increased by 3 every loop.
#     split_questions = quiz[item : item+3] #split the quiz by slicing. Every time this variable contains a list with question, possible question and answer.
#     for item in split_questions:
#         if split_questions[0] == item:
#             per_question['question'] = item
#         elif split_questions[1] == item:
#             per_question['possible_answers'] = item
#         elif split_questions[2] == item:
#             per_question['correct_answer'] = item
# print(per_question)


