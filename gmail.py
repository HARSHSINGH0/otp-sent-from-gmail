import smtplib
import random
otp=random.randrange(1000,9999)

content="Here is your otp "#{}".format(otp)
print(content)
mail=smtplib.SMTP('smtp.gmail.com')
mail.ehlo()
mail.starttls()
recipient='hs475052@gmail.com'
sender='phoneaddicts007@gmail.com'
try:
    mail.login("phoneaddicts007@gmail.com","phoneaddicts")
except Exception:
    print("wrong password\n see below error's")
header="To:"+recipient+'\n'+'From:' +sender+'\n'+'Subject:OTP {}\n'.format(otp)
content=header+content

mail.sendmail(sender,recipient,content)
print("succesfully sent ")
mail.close()
check=int(input("Enter the OTP:"))
if check==otp:
	print("you are in!!")
else:
	print("sorry wrong otp please try again")
