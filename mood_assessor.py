
import datetime
import os

def assess_mood():
    #get today's date
    date_today = str(datetime.date.today())
#read diary to check if an input already exists for today
    def read_diary():
        data_directory = "data"
        diary_file_path = os.path.join(data_directory, "mood_diary.txt")
        myDiary = open(diary_file_path,'r')
        return [line.strip().split(" ") for line in myDiary.readlines()]

    diary_entries = read_diary()

    #get valid input
    
    def getMood():

        valid_input = False

        while not valid_input :
            current_mood = str(input("Please enter your current mood:"))

            if current_mood == 'happy' or 'relaxed' or 'apathetic' or 'sad' or 'angry':
                valid_input = True
            else: 
                print("Invalid input, please enter again!")
            return current_mood
    
    # save input as integer
    def getNumberFromMood(current_mood): 
        if current_mood == 'happy':
            return 2
        elif current_mood == 'relaxed':
            return 1
        elif current_mood == 'apathetic':
            return 0
        elif current_mood == 'sad':
            return -1
        else:
            return -2
    
    # convert integer back into mood string:
    def getMoodFromNumber(num):
        if num == 2:
            return "happy"
        elif num == 1:
            return "relaxed"
        elif num == 0:
            return "apathetic"
        elif num == -1:
            return "sad"
        else:
            return "angry"
    # write diary

    def write_diary(date_today,mood_today):
        data_directory = "data"
        diary_file_path = os.path.join(data_directory, "mood_diary.txt")
        myDiary = open(diary_file_path,'w')
        myDiary.write(date_today+" "+mood_today+"\n")

    #diagnose 

    def diagnose_mood(diary_entries):
        if len(diary_entries) >= 7:
            last_7_entries = diary_entries[-7:]
            moods = [int(entry[1]) for entry in last_7_entries]
            average_mood = round(sum(moods) / len(moods))
            
            mood_count = [entry[1] for entry in last_7_entries]

            #happy for 5 or more days, sad for 4 or more days, apathetic for 6 or more days
            if mood_count.count(2) >=5:
                diagnosis = "manic"
            elif mood_count.count(-1) >=4:
                diagnosis = "depressive"
            elif mood_count.count(0)>= 6:
                diagnosis = "schizoid"
            else:
                diagnosis = getMoodFromNumber(average_mood)
        
            print("Your diagnosis:"+ diagnosis+"!")
        
    # main function 
    if diary_entries and diary_entries[-1][0] == str(date_today):
        print("Sorry, you have already entered your mood today.")
        exit()
    else: 
        current_mood= getMood()
        mood_today = str(getNumberFromMood(current_mood))
        write_diary(date_today, mood_today)
        diagnose_mood(diary_entries)



    

    
   






    
    
    