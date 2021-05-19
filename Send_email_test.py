import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com',587)

smtp_object.ehlo()
smtp_object.starttls()

# For hidden passwords
import getpass

email = input("Enter your email: ")
password = 'xxxxxxxxxx'  #check your notes



smtp_object.login(email,password)


from_address = 'rogerryansalvador@gmail.com'
to_address = 'rogerryansalvador@gmail.com'
subject = input("Enter the subject line: ")
message = input("Type out the message you want to send: ")
msg = "Subject: " + subject + '\n' + message
smtp_object.sendmail(from_address,to_address,msg)

smtp_object.quit()