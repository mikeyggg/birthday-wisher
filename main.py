from random import randint
import pandas
import  smtplib
import datetime as dt




today = dt.date.today()
today_tuple = (today.month,today.day)

birthdays = pandas.read_csv('birthdays.csv')
birthday_dict = {(row.month,row.day) : row for index,row in birthdays.iterrows() }

email = "PLACE YOUR EMAIL HERE"
password = "PLACE YOUR PASSWORD HERE"

if today_tuple in birthday_dict:

    name = birthday_dict[today_tuple]["name"]
    to_email = birthday_dict[today_tuple]["email"]

    with open(f'letter_templates/letter_{randint(1,3)}.txt',"r") as card:
        text = card.read()
        text = text.replace("[NAME]", name)


    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email,password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=to_email,
                            msg=f'Subject: Happy Birthday!\n\n{text}'
                              )


