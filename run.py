import datetime
import time
import os
import operator
import threading 
import traceback
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

date = datetime.datetime.now()
sys_ender_email = 'info@wizen.lt'
receiver_email = 'valdemar.tunkevic@gmail.com'


#Print Greetings message with information
print('Stay in touch with hundreds of people')
print('Every person you’ve ever met has the potential to help you.')
print('If you keep in touch and stay on their mind, there’s a good chance an opportunity will come your way. \n But if you don’t keep in touch, that potential is almost gone. \n Out of touch, out of mind.')
print('So you need to make a simple automatic system to keep in touch without \n relying on your memory. Use your database to label everyone in a category like this: \n A list: Very important people. Contact every three weeks. \n B list: Important people. Contact every two months. \n C list: Most people. Contact every six months. \n D list: Demoted people. Contact once a year, to make sure you still have their correct info.')
#Extra texts
'''
To Have Great Relationships, Always Make the First Move.
Always make the first move.
The meaning is simple: if you can help the relationship, then do it. 
Don’t wait for the other person to act (even if you don’t want to).

If you want to have deep, meaningful relationships with your friends, family, and even just the people in your day-to-day life, make the first move — even if it should be them. Be the first to:

- Initiate the conversation
- Send the first text
- Say you miss them
- Say you love them
- Apologize and ask for forgiveness
- Organize a hangout
- Compliment them
- Thank them
- Tell them you appreciate what they did

'''

#Dicionary of lists where date is store
lists = {'a_list': [],'b_list': [], 'c_list': [], 'd_list': []}


def check_friends_name():
    new_friend = input('Only Letters and whitespaces allowed \n')

    while True:
        if all(x.isalpha() or x.isspace() for x in new_friend):
            return new_friend
        new_friend = input('Only Letters and whitespaces allowed \n')  


def is_name_duplicate(name):
   
    while True:
        for sub_list in lists:
            for person in lists[sub_list]:
                if person['name'] == name.lower():
                    return True
        return False        


def check_list():
    possible_lists = ('abcd')
    add_friend_to_list = input('Into which list you want to add friend? A,B,C,D \n')
    
    while True:
        if add_friend_to_list.lower() in possible_lists:
            return add_friend_to_list.lower()
        add_friend_to_list = input('Into which list you want to add friend? A,B,C,D \n')

#Problematic, Capital letters go before Lowercase letters.
def sort_lists_of_dicts():
    for sub_list in lists:
        lists[sub_list].sort(key=operator.itemgetter('name'))
     

def add_friend():
    print('Please enter persons name you want to add')
    last_contacted = date.strftime("%Y/%m/%d")
    
    friend_name = check_friends_name()
    
    #checks if name does not exist, if not, creates new friend and allocates to chosen list. 
    if is_name_duplicate(friend_name) == False:
        list_to_add = check_list()
        
        #appends friend to chosen list
        if list_to_add == 'a':
            print('Friend successfully added to list A')
            lists['a_list'] += [{'name': friend_name, 'last_contacted': last_contacted, 'day_number': 0}]

        elif list_to_add == 'b':
            print('Friend successfully added to list B')
            lists['b_list'] += [{'name': friend_name, 'last_contacted': last_contacted, 'day_number': 0}]

        elif list_to_add == 'c':
            print('Friend successfully added to list C')
            lists['c_list'] += [{'name': friend_name, 'last_contacted': last_contacted, 'day_number': 0}]

        elif list_to_add == 'd':
            print('Friend successfully added to list D')
            lists['d_list'] += [{'name': friend_name, 'last_contacted': last_contacted, 'day_number': 0}]
    #if friend exists with such name, informs and askes to make with new name       
    else:
        print('Such friend already exists')
        add_friend()

def remove_friend():
    print('Enter name of a person you want to remove')
    friend_name = check_friends_name()

    for sub_list in lists:
        for person in lists[sub_list]:
            if person['name'].lower() == friend_name.lower():
                print('Person found' ,person['name'],person['last_contacted'],'& deleted')
                del lists[sub_list][lists[sub_list].index(person)]
                return
    print('Friend not found')


def rename_friend():
    print('Who you want to rename? Enter name')
    friend_name = check_friends_name()
    
    #loops lists to find if friend exists
    for sub_list in lists:
        for y in lists[sub_list]:
            if y['name'].lower() == friend_name.lower():
                print('Friend is found. Enter new name for a friend')
                new_name = check_friends_name()
                lists[sub_list][lists[sub_list].index(y)]['name'] = new_name
                print("New name has been saved", new_name)
                return
    print('Friend not found')
                

def move_to_other_list():
    friend_name = check_friends_name()
        
    for sub_list in lists:
        for y in lists[sub_list]:
            
            if y['name'].lower() == friend_name.lower():
                print('Friend is found!')
                new_list = check_list()
        
                if new_list == 'a':
                    lists['a_list'].append(lists[sub_list][lists[sub_list].index(y)])
                    del lists[sub_list][lists[sub_list].index(y)]
                    print('Friend successfully moved to List A')
                    return
                    
                elif new_list == 'b':
                    lists['b_list'].append(lists[sub_list][lists[sub_list].index(y)])
                    del lists[sub_list][lists[sub_list].index(y)]
                    print('Friend successfully moved to List B')
                    return
                
                elif new_list =='c':
                    lists['c_list'].append(lists[sub_list][lists[sub_list].index(y)])
                    del lists[sub_list][lists[sub_list].index(y)]
                    print('Friend successfully moved to List C')
                    return
                
                elif new_list == 'd':
                    lists['d_list'].append(lists[sub_list][lists[sub_list].index(y)])
                    del lists[sub_list][lists[sub_list].index(y)]
                    print('Friend successfully moved to List D')
                    return
                
    print('Sorry, something went wrong')

#function adding +1 to day_number - will be run once a day
def day_number_add_one():
    for sub_list in lists:
        for y in lists[sub_list]:
            lists[sub_list][lists[sub_list].index(y)]['day_number'] += 1

#function to check who must be contacted today
def whom_contact_today():
    a_days = 21
    b_days = 60
    c_days = 180
    d_days = 365
    
    for sub_list in lists:
        
        if sub_list == 'a_list':
            for y in lists['a_list']:
                if lists['a_list'][lists['a_list'].index(y)]['day_number'] == a_days:
                    send_email(y['name'])
                    lists['a_list'][lists['a_list'].index(y)]['day_number'] = 0
                    lists['a_list'][lists['a_list'].index(y)]['last_contacted'] = date.strftime("%Y/%m/%d")
        
        if sub_list == 'b_list':
            for y in lists['b_list']:
                if lists['b_list'][lists['b_list'].index(y)]['day_number'] == b_days:
                    send_email(y['name'])
                    lists['b_list'][lists['b_list'].index(y)]['day_number'] = 0
                    lists['b_list'][lists['b_list'].index(y)]['last_contacted'] = date.strftime("%Y/%m/%d")
        
        if sub_list == 'c_list':
            for y in lists['c_list']:
                if lists['c_list'][lists['c_list'].index(y)]['day_number'] == c_days:
                    send_email(y['name'])
                    lists['c_list'][lists['c_list'].index(y)]['day_number'] = 0
                    lists['c_list'][lists['c_list'].index(y)]['last_contacted'] = date.strftime("%Y/%m/%d")
        
        if sub_list == 'd_list':
            for y in lists['d_list']:
                if lists['d_list'][lists['d_list'].index(y)]['day_number'] == d_days:
                    send_email(y['name'])
                    lists['d_list'][lists['d_list'].index(y)]['day_number'] = 0
                    lists['d_list'][lists['d_list'].index(y)]['last_contacted'] = date.strftime("%Y/%m/%d")




def every(delay, task):
  next_time = time.time() + delay
  while True:
    time.sleep(max(0, next_time - time.time()))
    try:
      task()
    except Exception:
      traceback.print_exc()
      # in production code you might want to have this instead of course:
      # logger.exception("Problem while executing repetitive task.")
    # skip tasks if we are behind schedule:
    next_time += (time.time() - next_time) // delay * delay + delay


#Every new day - adds 1 to day_number for all friends
threading.Thread(target=lambda: every(20, day_number_add_one)).start()


#Every new day - checks lists to find whom to contact today
threading.Thread(target=lambda: every(60, whom_contact_today)).start()


def send_email(friend_name):
    message = Mail(
        from_email = sys_ender_email,
        to_emails = receiver_email,
        subject='It is time to contact ' + friend_name,
        html_content='Hey there \n It is about time to contact your friend'+friend_name)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)



def extra_commands():
    extra_command = input('Would you like to perform anything else? \n')
    if extra_command == 'yes':
        run_system()
    else:
        print('Good bye')


def run_system():
    command = input('Please enter a command: \n add - to add new friend \n rename - to rename friend \n move - to move friend to new list \n remove - to remove friend \n show - to view current lists \n quit - to quit \n Command: ')
    
    if command.lower() == 'add':
        add_friend()
        run_system()
        
    elif command.lower() == 'rename':
        rename_friend()
        run_system()
            
    elif command.lower() == 'move':
        move_to_other_list()
        run_system()
            
    elif command.lower() == 'remove':
        remove_friend()
        run_system()
    
    elif command.lower() == 'quit':
        print('Good bye')
    
    elif command.lower() == 'show':
        sort_lists_of_dicts()
        print('A List \n')
        for i in lists:
            if i == 'a_list':
                for y in lists['a_list']:
                    print(y['name'],'| Last contacted',y['last_contacted'])
        
        print('\nB List \n')
        for i in lists:
            if i == 'b_list':
                for y in lists['b_list']:
                    print(y['name'],'| Last contacted',y['last_contacted'])
                    
        print('\nC List \n')
        for i in lists:
            if i == 'c_list':
                for y in lists['c_list']:
                    print(y['name'],'| Last contacted',y['last_contacted'])
                    
        print('\nD List \n')
        for i in lists:
            if i == 'd_list':
                for y in lists['d_list']:
                    print(y['name'],'| Last contacted',y['last_contacted'])
        run_system()
              
            
    else:
        run_system()


run_system()


#Further improvement ideas:
    #fix - Sorting
    #Make that schedule module, does not stop other operations to be performed simultanuesly
    #Show when it's expected to contact a friend - Next contact day 
    #Create nice displays - with html/css/js
    #allow users to register - send emails to registered email
    #connect db
    #if list is empty - display message - list is empty