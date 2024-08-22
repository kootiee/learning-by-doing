# highscore_in_file, highscorer_in_file = '0', 'be the first!'
# with open('score.txt', 'a+') as score_file: #6 
#     check_highscore = score_file.read() #7
#     if not check_highscore: #8
#         score_file.write('0')
#         print('yes')
#         print(check_highscore)
#     else:
#         highscore_in_file = score_file.readline()  #9
#         highscorer_in_file = score_file.readline()
#         print(highscore_in_file,'-', highscorer_in_file, 'In the file this is the highscore')

# f = open("demofile3.txt", "w")
# f.write("Woops! I have deleted the content!\nlive")
# f.close()

# #open and read the file after the overwriting:
# f = open("demofile3.txt", "r")
# print(f.read())

with open('score.txt', 'a+') as score_file: #mode
    check_highscore = score_file.readline()
    print(check_highscore, '<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    if player_score > int(check_highscore):
        score_file.seek(0) #11
        score_file.write(str(player_score))
        score_file.write(player_name)
        score_file.truncate() #