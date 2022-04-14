import smtplib

# define send_mail funtion that will take three parameter.
def send_mail(email,password,message):
    server = smtplib.SMTP("smtp.gmail.com", 587)  #trying to establihsed connection to gmail server and the port number of gmail server is 587.
    server.starttls() # for tell server we want to communicate with TLS encryption
    server.login(email, password)
    server.sendmail(email,email,message)

email = ""  
password = ""
message = "hey Elisha how are you doing!!"
send_mail(email, password, message)
