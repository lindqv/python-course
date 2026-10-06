class EmailNotification:
    def send():
        return "Email notification!"

class SMSNotification:
    def send():
        return "SMS notification!"

class PushNotification:
    def send():
        return "Push notification!"

notifications = [EmailNotification, SMSNotification, PushNotification]

for notification in notifications:
    print(notification.send())

# The loop does not need to know the exact class of each object, 
# what is needed is for each object to have a send() method.