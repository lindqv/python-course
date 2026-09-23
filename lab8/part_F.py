class Notification:
    def send(self):
        return "This is a general message"

class EmailNotification(Notification):
    def send(self):
        return "This is an email notification"

class SMSNotification(Notification):
    def send(self):
        return "This is a SMS notification"

notification = Notification()
email_notification = EmailNotification()
sms_notification = SMSNotification()

print(notification.send()) # This uses send() in the Notification class
print(email_notification.send()) # This uses send() in the EmailNotification class
print(sms_notification.send()) # This uses send() int the SMSNotifcation class