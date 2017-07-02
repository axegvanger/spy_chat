#Import Snoopdetails file
from snoopdetails import snoop, Snoop, ChatMessage, friends


#Import Steganography Library
from steganography.steganography import Steganography


#Import DATETIME
from datetime import datetime


STATUS_MESSAGES = ['My first SNOOPCHAT Status', 'SNOOPCHAT is Awesome App', 'I Enjoyed alot on SNOOPCHAT'] #STATUS MESSAGES LIST

print'Hello, Welcome to SNOOPCHAT '


question = "Do you want to continue as " + snoop.salutation + " " + snoop.name + " (Y/N)? "
existing = raw_input(question)


def add_status():  # Add your status

    updated_status_message = None

    if snoop.current_status_message != None:

        print 'Your current status message is %s \n' % (snoop.current_status_message) # Add Your current status
    else:
        print 'You don\'t have any status message currently \n'

    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))  # select your status from the previous ones


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'Invalid Option Press either y or n.'  # INVALID OPTION

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message



def add_friend():          #Creating Add friend function

    new_friend = Snoop('','',0,0.0)

    new_friend.name = raw_input("Add your Friend's name: ")   #Ask friend's name
    new_friend.salutation = raw_input("Add your friends's salutaion Mr. or Ms.?: ")   #Ask friend's salutation

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Enter friend's Age?")    #Friend's age
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Enter Friend's Rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= snoop.rating:

        friends.append(new_friend) # Append new friend details

        print 'Friend is Added!'     #Friend is being Added
    else:
        print 'Invalid Details. Snoop can not be added with the details you provided'    #Invalid Information of SNOOP-FRIEND

    return len(friends)   #return length of the function named friends



def select_a_friend():    #Creating a function for selecting a friend of your choice
    item = 0

    for friend in friends:   #for loop for searching your friend

        # using placeholders for friend details
        print '%d. %s %s aged %d with rating %.2f is online' % (item +1, friend.salutation, friend.name, friend.age, friend.rating)
        item = item + 1

    friend_choice = raw_input("Select a friend of your choice")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position




def send_message():  # Function for send any text to your friend

    friend_choice = select_a_friend()

    original_image = raw_input("Name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)  #encoding of your image with your secret message

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)  # append your messsage with your selected friend

    print "Now your secret message image is ready"




def read_message():  # function for reading the secret message

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)  #decoding by Steganography

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)

    print "Now your secret message has been saved"




def read_chat_history():  # Chat history function

    read = select_a_friend()

    print '\n6'

    for chat in friends[read].chats:  # using for loop for reading the chats
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read].name, chat.message)




def start_chat(snoop):

    snoop.name = snoop.salutation + " " + snoop.name


    if snoop.age > 12 and snoop.age < 50:


        print "Authentication complete. Welcome " + snoop.name + " Age: " \
              + str(snoop.age) + " and Rating of: " + str(snoop.rating) + " Proud to have you on SnoopChat"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add your status update \n 2. Add a Snoop friend \n 3. Send a secret message to Snoop-friend \n 4. Read a secret message \n 5. Read Chats from a Snoop-user \n 6. Close Snoop Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    snoop.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a snoop'


if existing == "Y":
    start_chat(snoop)
    print 'Continue'
else:

    snoop = Snoop('', '', 0, 0.0)

    snoop.name = raw_input("Welcome to SNOOPCHAT, tell me your snoop name first: ")

    if len(snoop.name) > 0:
        snoop.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        snoop.age = raw_input("What is your age?")
        snoop.age = int(snoop.age)

        snoop.rating = raw_input("What is your snoop rating?")
        snoop.rating = float(snoop.rating)

        start_chat(snoop)
    else:
        print 'Please add a valid snoop name'
