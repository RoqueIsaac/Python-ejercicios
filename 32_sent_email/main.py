
import datetime as dt
import random
import pandas as pd

dats=dt.datetime.now()
today = (dats.month, dats.day)

cumples = pd.read_csv("birthdays.csv")

new_dict2 = {(data_row["month"],data_row["day"]):data_row for (index, data_row) in cumples.iterrows()}

#email libraries
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

if today in new_dict2:
    num = random.randint(1,3)
    #open and choose 1 template
    with open("./letter_templates/letter_{}.txt".format(num),"r") as file:

        x = file.read()
        x = x.replace("[NAME]",new_dict2[today]["name"])

        with smtplib.SMTP('smtp.mail.yahoo.com', 587) as connection:

            my_email = "xxxxxxxx@yahoo.com"     #update your email
            password = "xxxxxxxxxxxx"           #update your api pswd

            #create multipart message
            msg = MIMEMultipart()
            msg['From'] = my_email
            msg['To'] = new_dict2[today]["email"]
            msg['Subject'] = "Happy Birthday"
            msg['Cc'] = my_email

            #add text message(template)
            msg.attach(MIMEText(x, 'plain'))

            #start secure connection
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.send_message(msg)

            #other option is using sendmail(), but yahoo doesnt accept it
            # connection.sendmail(from_addr=my_email, to_addrs="xxxxxxx@hotmail.com", msg="Subject: hello\n\n this is the boddy")





