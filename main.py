import pandas
import datetime as dt
import random
import smtplib

my_email = 'ahmed2562006abd'
my_password = 'rtpbixhxjkvaocmc'

TEMPLATES=('letter_1.txt','letter_2.txt','letter_3.txt')
data = pandas.read_csv ('birthdays.csv')
now = dt.datetime.now()
today_day = now.day
today_month = now.month
today_year = now.year
people_to_hello=[row for index,row in data.iterrows() if row['day']==today_day and row['month']==today_month]
template=random.choice(TEMPLATES)
if len(people_to_hello) > 0:
    for person in people_to_hello:
        new_year=int(today_year)-int(person['year'])
        with open (template) as file:
            message = file.read().replace('[NAME]',person['name']).replace('number',f'{new_year}')
        with smtplib.SMTP('smtp.gmail.com',587) as con:
            con.starttls()
            con.login(my_email,my_password)
            con.sendmail(from_addr=my_email,to_addrs=person['email'],msg=f'Subject:Happy birthday {person['name']} !\n\n{message}')
        print('Done')
