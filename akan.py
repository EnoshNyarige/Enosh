# coding=utf-8
# The Akan naming algo
import datetime

date = raw_input("Please enter your date of birth in the following format: YYYY-MM-DD: ")
gender = raw_input("Please enter your gender in the following format: M or F ")

date = datetime.datetime.strptime(date, '%Y-%m-%d').strftime('%Y%m%d')


def date_to_date(date):
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:])
    y = year - ((14 - month) // 12)
    x = y + (y//4) - (y // 100) + (y // 400)
    m = month + 12 * ((14 - month) // 12) - 2
    d = (day + x + 31 * m // 12)%7
    return d


def akan_name(day, gender):
    # Decide the name
    if gender == "M":
        m_names = {0: "Kwasí", 1: "Kwadwó", 2: "Kwabená", 3: "Kwakú", 4: "Yaw", 5: "Kofí", 6: "Kwámè"}
        return "Your Akan name is " + str(m_names.get(day))
    elif gender == "F":
        f_name = {0: "Adwoa", 1: "Abenaa", 2: "Akúá", 3: "Yaa", 4: "Afua", 5: "Ám̀ma", 6: "Akosua"}
        return "Your Akan name is " + str(f_name.get(day))


print (akan_name(date_to_date(date), gender))