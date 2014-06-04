import json
"""
    Desearilaze data from json file and write them in a readable way
    Put "???" if there are some problems with fields for hand checking
"""
questions_dict = dict()
with open("/Users/danmir/Google Диск/Матмех (gd)/Python/history.txt", "r", encoding="UTF-8") as f:
    questions_dict = json.load(f)

with open("/Users/danmir/Google Диск/Матмех (gd)/Python/history_111.txt", "w", encoding="UTF-8") as f1:
    count = 1
    for key in sorted(questions_dict.keys()):
        try:
            f1.write(str(count) + key + "\n" + "Ответ: " + questions_dict[key]["right"] + "\n" + "Варианты ответов: " + repr(questions_dict[key]["ans"]) + "\n" + "Подсказка: " + questions_dict[key]["hint"] + "\n" + "\n")
        except:
            f1.write(str(count) + key + "\n" + "Ответ: " + "???" + "\n" + "Варианты ответов: " + repr(questions_dict[key]["ans"]) + "\n" + "Подсказка: " + "???" + "\n" + "\n")
        count += 1
