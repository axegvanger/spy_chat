from datetime import datetime   #Import Datetime

class Snoop:              #Class named Snoop consisting of Snoop data

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:          #Class consisting of chat with showing date & time

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me



snoop = Snoop('David', 'Mr.', 24, 4)    #Already existing snoop details

#friends details
friend_one = Snoop('Clara', 'Ms.', 21, 4.7)
friend_two = Snoop('Daniel', 'Mr.', 33, 4.2)
friend_three = Snoop('Lily', 'Ms.', 35, 3.8)
friend_four = Snoop('Kavin', 'Mr.', 40, 4)
friend_five = Snoop('Harry','Mr.', 28, 3.6)


#friends list
friends = [friend_one, friend_two, friend_three, friend_four, friend_five]
