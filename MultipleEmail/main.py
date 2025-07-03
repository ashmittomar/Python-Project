import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('ashmittomar5@gmail.com','noobtopro') #Add your email and password
subject = "Test"
body = "Hello world!"
message = "subject:{}\n\n{}".format(subject,body)

listadd = ['ashmitt668@gmail.com'] #You can add email of your choice

ob.sendmail('ashmittomar5@gmail.com')  #Sender's mail 
print("Mail sent")
ob.quit()