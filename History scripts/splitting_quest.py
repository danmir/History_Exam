import sh
import os
"""
    Splitting all questions to own files sorted in folders that are sorted by the first letter
    Text in all questions splited to new lines on every 57 char to make it fit into small pictures
"""
with open("/Users/danmir/Google Диск/Матмех (gd)/Python/Новая папка/exper.txt", "r") as f:  # Path to the questions
    for i in range(606):  # 606 total
        quest = f.readline()
        ans = f.readline()
        all_ans = f.readline()
        hint = f.readline()
        empty_line = f.readline()

        all_text = quest + "\n" + ans + "\n" + all_ans + "\n" + hint
        for j in range(len(all_text)):
            if not (j % 57):
                all_text = all_text[:j] + "\n" + all_text[j:]

        directory = "/Users/danmir/All_quest/{}".format(quest[0])
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(directory)

        with open("/Users/danmir/All_quest/{}/_{}_quest.txt".format(quest[0], i), "w") as w:
            w.write(all_text)

        # print(quest)
        # print(ans)
        # print(all_ans)
        # print(hint)
        # print(empty_line)
