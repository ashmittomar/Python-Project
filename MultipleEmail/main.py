import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('mail','password') #Add your email and password
subject = "Test"
body = "Hello world!"
message = "subject:{}\n\n{}".format(subject,body)

listadd = ['mail'] #You can add email of your choice

ob.sendmail('mail')  #Sender's mail 
print("Mail sent")
ob.quit()