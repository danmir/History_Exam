from bs4 import BeautifulSoup
import requests
import json
import re

"""
    Grabber and parser for history questions from i-exa.ru
    Save them to file and to json format
"""

def get_all_pages():
    all_pages = []
    for i in range(1, 14):
        all_pages.append(
            "http://i-exa.ru/category/otechestvennaya-istoriya/page/{}".format(i))
    return all_pages


def get_pages():
    all_pages = get_all_pages()
    all_links = []
    for page in all_pages:
        main_page = requests.get(page)
        main_page_data = main_page.text
        main_soup = BeautifulSoup(main_page_data)
        # print(main_soup.prettify())

        for link in main_soup.find_all("a"):
            link_text = link.get("href")
            if link_text[link_text.__len__() - 1] == "l":
                all_links.append(link_text)

    return all_links


def get_question():
    all_questions = get_pages()
    questions_dict = dict()
    num = 0
    for page in all_questions:
        print("Num of question {}".format(num))
        num += 1
        r = requests.get(page)
        data = r.text
        soup = BeautifulSoup(data)

        # print(soup.prettify())
        # print(soup.table)
        t = soup.table
        for child in t.find_all("tr"):
            if child.img:
                right_answer = child.font.string
                # print(right_answer)

        count = 0
        for elem in soup.find_all('font'):
            if not count:
                curr_quest = elem.string
                if curr_quest is None or curr_quest.__len__() < 6:
                    #curr_quest = input("Текущий вопрос ?")
                    curr_quest = "check_it{}".format(count)
                questions_dict[curr_quest] = dict()
                questions_dict[curr_quest]["ans"] = list()
                print(curr_quest)
            if elem.string == right_answer:
                print(elem.string, "<-")
                questions_dict[curr_quest]["right"] = elem.string
                if questions_dict[curr_quest]["right"] is None:
                    #questions_dict[curr_quest]["right"] = input("Правильный ответ ?")
                    questions_dict[curr_quest]["right"] = "check_it{}".format(count)
                questions_dict[curr_quest]["ans"].append(elem.string)
            else:
                if count == 5:
                    questions_dict[curr_quest]["hint"] = elem.string
                    if questions_dict[curr_quest]["hint"] is None:
                        #questions_dict[curr_quest]["hint"] = input("Подсказка ?")
                        questions_dict[curr_quest]["hint"] = "check_it{}".format(count)
                    print("Hint {}".format(elem.string))
                elif count != 0:
                    questions_dict[curr_quest]["ans"].append(elem.string)
                    print(elem.string)
            count += 1

        print("\n")
    return questions_dict


def main():
    questions_dict = get_question()
    with open("/Users/danmir/Google Диск/Матмех (gd)/Python/history_1.txt", "w", encoding="UTF-8") as f:
        json.dump(questions_dict, f)
        #f.write(json.dumps(questions_dict))

    with open("/Users/danmir/Google Диск/Матмех (gd)/Python/history_r_1.txt", "w", encoding="UTF-8") as f1:
        count = 1
        for key in sorted(questions_dict.keys()):
            try:
                f1.write(str(count) + key + "\n" + "Ответ: " + questions_dict[key]["right"] + "\n" + "Варианты ответов: " + repr(questions_dict[key]["ans"]) + "\n" + "Подсказка: " + questions_dict[key]["hint"] + "\n" + "\n")
            except KeyError:
                f1.write(str(count) + key + "\n" + "Ответ: " + "check_it{}".format(count) + "\n" + "Варианты ответов: " + repr(questions_dict[key]["ans"]) + "\n" + "Подсказка: " + "check_it{}".format(count) + "\n" + "\n")
            count += 1

if __name__ == "__main__":
    main()
