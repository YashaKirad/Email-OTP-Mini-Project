import random
import smtplib

server=smtplib.SMTP('smtp.gmail.com',587)
#adding TLS security 
server.starttls()
#get your app password of gmail ----as directed in the video
password='ynstcblzldrxbvaf'
server.login('yashakirad@gmail.com',password)
receiver_email = input("Enter receiver's email: ")
#generate OTP using random.randint() function
otp=''.join([str(random.randint(0,9)) for i in range(4)])
msg='Hello, Your OTP is '+str(otp)


server.sendmail('yashakirad@gmail.com',receiver_email,msg)
server.quit()

