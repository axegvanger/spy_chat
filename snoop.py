#Import termcolor
#import sys
from termcolor import colored, cprint

#Import Snoopdetails files
from snoopdetails import snoop, Snoop, ChatMessage, friends


colored("how r u", 'red')

#Import Steganography Library
from steganography.steganography import Steganography


#Import DATETIME
from datetime import datetime


STATUS_MESSAGES = ['My first SNOOPCHAT Status', 'SNOOPCHAT is an Awesome App', 'I Enjoyed alot on SNOOPCHAT'] #STATUS MESSAGES LIST

words = ['SOS','sos','HELP','help', 'SAVE','save']

cprint('Hello, ---Welcome to SNOOPCHAT!---', 'green')


question = colored("Do you want to continue as ",'blue') + colored(snoop.salutation,'red') + " " + colored(snoop.name,'red') + " (Y/N)? "
existing = raw_input(question)


def add_status():  # Add your status

    updated_status_message = None

    if snoop.current_status_message != None:

        print 'Your current status message is %s \n' % (snoop.current_status_message) # Add Your current status
    else:
        print colored('You don\'t have any status message currently \n','red')

    default = raw_input(colored("Do you want to select from the older status (y/n)? ",'blue'))

    if default.upper() == "N":
        new_status_message = raw_input(colored("What status message do you want to set? ", 'blue'))


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input(colored("\nChoose from the above messages ",'blue')))  # select your status from the previous ones


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:

        print colored('Invalid Option Press either y or n.', 'red') # INVALID OPTION

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)
    else:

        print colored('You current don\'t have a status update','red')

    return updated_status_message



def add_friend():          #Creating Add friend function

    new_friend = Snoop('','',0,0.0)

    new_friend.name = raw_input(colored("Add your Friend's name: ", 'blue'))   #Ask friend's name
    new_friend.salutation = raw_input(colored("Add your friends's salutaion Mr. or Ms.?: ",'blue'))   #Ask friend's salutation

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input(colored("Enter friend's Age?", 'blue'))    #Friend's age
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input(colored("Enter Friend's Rating?", 'blue'))
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= snoop.rating:

        friends.append(new_friend) # Append new friend details

        print colored('Friend is Added!', 'green')    #Friend is being Added
    else:

        print colored('Invalid Details. Snoop can not be added with the details you provided', 'red') #Invalid Information of SNOOP-FRIEND


    return len(friends)   #return length of the function named friends



def select_a_friend():    #Creating a function for selecting a friend of your choice
    item = 0

    for friend in friends:   #for loop for searching your friend

        # using placeholders for friend details
        #print '%d. %s %s aged %d with rating %.2f is online' % (item +1, colored(friend.salutation,'blue'), colored(friend.name,'blue'), colored(friend.age,'blue'), colored(friend.rating,'blue'))
        print colored(friend.salutation,'green'),colored(friend.name,'green'),colored(friend.age,'green'),colored("aged",'green'),colored("with rating",'green'),colored(friend.rating,'green')
        item = item + 1

    friend_choice = raw_input(colored("Select a friend of your choice",'blue'))

    if friend_choice.isdigit():
        friend_choice_position = int(friend_choice) - 1

        return friend_choice_position
    else:
        print "wrong input"
        return select_a_friend()




def send_message():  # Function for send any text to your friend

    friend_choice = select_a_friend()

    original_image = raw_input(colored("Name of the image?", 'blue'))
    output_path = "output.jpg"
    text = raw_input(colored("What do you want to say? ", 'blue'))
    Steganography.encode(original_image, output_path, text)  #encoding of your image with your secret message


    # split the list containing list of words like sos, help etc
    temp = text.split(' ')
    for i in words:
        if i in temp:
            temp[temp.index(i)] = colored('DANGERZONE of Snoopchat')
    text = str.join(' ', temp)
    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)  # append your messsage with your selected friend

    print colored("Now your secret message image is ready",'green')


def read_message():  # function for reading the secret message

    sender = select_a_friend()

    output_path = raw_input(colored("What is the name of your file?",'blue'))

    secret_text = Steganography.decode(output_path)  # Decoding Text from the image
    secret_text = str(secret_text)
    if secret_text == 'None':
        print colored("No secret msg is found",'red')

    else:
        temp = secret_text.split(' ')
        if len(temp)>100:
            del friends[sender]
            print "friend deleted"
            return "pass"
        else:
            for i in words:
                if i in temp:
                    temp[temp.index(i)] = colored('i m in danger', 'red')
            secret_text = str.join(' ', temp)

        new_chat = ChatMessage(secret_text, False)

        friends[sender].chats.append(new_chat)

        print colored("Now your secret message has been saved", 'green')





def read_chat_history():  # Chat history function

    read = select_a_friend()

    print '\n6'

    for chat in friends[read].chats:  # using for loop for reading the chats
        if chat.sent_by_me:
            #print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
            print 'at',colored(chat.time,'cyan'),"you said",chat.message
        else:
            #print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read].name, chat.message)
            print 'at', colored(chat.time,'cyan'), "your friend said", chat.message




def start_chat(snoop):

    snoop.name = snoop.salutation + " " + snoop.name


    if snoop.age > 12 and snoop.age < 50:



        print colored("Authentication complete. Welcome ",'green') + colored(snoop.name, 'red') + " Age: " \
              + str(snoop.age) + " and Rating of: " + str(snoop.rating) + colored(" Proud to have you on SnoopChat", 'green')

        show_menu = True

        while show_menu:
            menu_choices = colored("What do you want to do? \n 1. Add your status update \n 2. Add a Snoop friend \n 3. Send a secret message to Snoop-friend \n 4. Read a secret message \n 5. Read Chats from a Snoop-user \n 6. Close Snoop Application \n", 'blue')
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
                    temp = read_chat_history()
                else:
                    show_menu = False
    else:
        print colored('Sorry you are not of the correct age to be a Snoop-user', 'red')


if existing.upper() == "Y":
    start_chat(snoop)
    print 'Continue'
else:

    snoop = Snoop('','', 0, 0.0)

    snoop.name = raw_input(colored("Welcome to SNOOPCHAT, tell me your snoop name first: ", 'blue'))

    if len(snoop.name) > 0:
        snoop.salutation = raw_input(colored("Should I call you Mr. or Ms.?: ", 'blue'))

        snoop.age = raw_input(colored("What is your age?", 'blue'))
        snoop.age = int(snoop.age)

        snoop.rating = raw_input(colored("What is your snoop rating?", 'blue'))
        snoop.rating = float(snoop.rating)

        start_chat(snoop)
    else:

        print colored('Please add a valid snoop name', 'red')