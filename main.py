import re
from pprint import pprint
import csv

#lastname,firstname,surname,organization,position,phone,email

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)


#Общий формат телефонов
pattern = re.compile(r"(\+7|8)?\s*\(?(\d{3})\)?[\-]?\s?(\d{3})\-?(\d{2})\-?(\d{2})\s?\(?([д][о][б])?([\.])?\s?(\d{4})?\)?")
subst = "+7(\\2)\\3-\\4-\\5 \\6\\7\\8"

#Разбитие строк и замена номера
def str_split(contact_list: list):
    new_list = list()
    for item in contact_list:
        full_str = ' '.join(item[:3]).split(' ')
        result = [full_str[0], full_str[1], full_str[2], item[3], item[4], re.sub(pattern, subst, item[5]), item[6]]
        new_list.append(result)
    return lists(new_list)

#Обработка списка
def lists(contacts: list):
    for contact in contacts:
        first_name = contact[0]
        last_name = contact[1]
        for new_contact in contacts:
            new_first_name = new_contact[0]
            new_last_name = new_contact[1]
            if first_name == new_first_name and last_name == new_last_name:
                if contact[2] == "": contact[2] = new_contact[2]
                if contact[3] == "": contact[3] = new_contact[3]
                if contact[4] == "": contact[4] = new_contact[4]
                if contact[5] == "": contact[5] = new_contact[5]
                if contact[6] == "": contact[6] = new_contact[6]
    result_list = list()
    for i in contacts:
        if i not in result_list:
            result_list.append(i)
    return result_list

# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')

    # Вместо contacts_list подставьте свой список:
    datawriter.writerows(str_split(contacts_list))