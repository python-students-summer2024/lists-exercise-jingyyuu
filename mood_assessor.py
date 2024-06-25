import datetime
import os

def read_diary():
    data_directory = "data"
    diary_file_path = os.path.join(data_directory, "mood_diary.txt")
    if not os.path.exists(diary_file_path):
        return []
    with open(diary_file_path, 'r') as myDiary:
        return [line.strip().split(" ") for line in myDiary.readlines()]

def getMood():
    valid_moods = ['happy', 'relaxed', 'apathetic', 'sad', 'angry']
    while True:
        current_mood = input("Please enter your current mood: ").strip().lower()
        if current_mood in valid_moods:
            return current_mood
        else:
            print("Invalid input, please enter again!")

def getNumberFromMood(current_mood):
    mood_to_number = {
        'happy': 2,
        'relaxed': 1,
        'apathetic': 0,
        'sad': -1,
        'angry': -2
    }
    return mood_to_number.get(current_mood, 0)

def getMoodFromNumber(num):
    number_to_mood = {
        2: "happy",
        1: "relaxed",
        0: "apathetic",
        -1: "sad",
        -2: "angry"
    }
    return number_to_mood.get(num, "unknown")

def write_diary(date_today, mood_today):
    data_directory = "data"
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
    diary_file_path = os.path.join(data_directory, "mood_diary.txt")
    with open(diary_file_path, 'a') as myDiary:
        myDiary.write(date_today + " " + mood_today + "\n")

def diagnose_mood(diary_entries):
    if len(diary_entries) >= 7:
        last_7_entries = diary_entries[-7:]
        moods = [int(entry[1]) for entry in last_7_entries]
        average_mood = round(sum(moods) / len(moods))

        mood_count = [int(entry[1]) for entry in last_7_entries]

        if mood_count.count(2) >= 5:
            diagnosis = "manic"
        elif mood_count.count(-1) >= 4:
            diagnosis = "depressive"
        elif mood_count.count(0) >= 6:
            diagnosis = "schizoid"
        else:
            diagnosis = getMoodFromNumber(average_mood)

        print("Your diagnosis: " + diagnosis + "!")
    else:
        print("Not enough data for diagnosis.")

def assess_mood():
    date_today = str(datetime.date.today())
    diary_entries = read_diary()

    if diary_entries and diary_entries[-1][0] == date_today:
        print("Sorry, you have already entered your mood today.")
        return

    current_mood = getMood()
    mood_today = str(getNumberFromMood(current_mood))
    write_diary(date_today, mood_today)
    diary_entries.append([date_today, mood_today])
    diagnose_mood(diary_entries)
