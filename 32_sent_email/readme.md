


# Sent Email, birthday letter

## Introduction

This project use smtplib library to sent emails, however I found an issue with yahoo server, gmail seems working fine,
sendemail() is an old function that yahoo doesnt accept it, but it accepts a modern structure: MIMEMultipart,
and can be used with send_message() function.

The first step is to generate an aplication password from you email provider, is not your current email passowrd,
search how to do it with your email provider.

On this project I read birthdays.csv file where you need to add your friends/family name, email, birth informacion: year, month, day;
the program check today's date and extract data from the file and ramdonly chooses between 3 templates to sent happy birthday letter.

birthdays.csv  ->  You will need to update it, I leave some details just to show you the format, current information is invented

main.py  ->  You need update your email and application passowrd



## Dependencies

| File      | Description |
| ----------- | ----------- |
| main.py       | main program file |
| brithdays.csv | loaad data |
| letter_1.txt | template 1 |
| letter_2.txt | template 2 |
| letter_3.txt | template 3 |
