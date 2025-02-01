#14
#Implement method overriding for a `Notification` class where 
# `send()` is overridden in `EmailNotification` and `SMSNotification`.

class Notification:
    def send(self):
        print("Sent notification from Notification class")
class EmailNotification(Notification):
    def send(self):
        print("Email notification sent")
class SMSNotification(Notification):
    def send(self):
        print("SMS notification send")
email = EmailNotification()
email.send()
sms = SMSNotification()
sms.send()
