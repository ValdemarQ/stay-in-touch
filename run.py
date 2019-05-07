import datetime

#Global variables
date = datetime.datetime.now()


#Print Greetings message with information
print('Stay in touch with hundreds of people')
print('Every person you’ve ever met has the potential to help you.')
print('If you keep in touch and stay on their mind, there’s a good chance an opportunity will come your way. \n But if you don’t keep in touch, that potential is almost gone. \n Out of touch, out of mind.')
print('So you need to make a simple automatic system to keep in touch without \n relying on your memory. Use your database to label everyone in a category like this: \n A list: Very important people. Contact every three weeks. \n B list: Important people. Contact every two months. \n C list: Most people. Contact every six months. \n D list: Demoted people. Contact once a year, to make sure you still have their correct info.')

#New lists as single dictionary
lists = {'a_list': [],'b_list': [], 'c_list': [], 'd_list': []}



#lists of friends
a_list = []
b_list = []
c_list = []
d_list = []

#Sort lists of friends into alphabetical order.


class Friend:
    def __init__(self,name,list_to,contact_date, just_date):
        self.name = name
        self.list_to = list_to
        self.contact_date = contact_date
        self.just_date = just_date


def check_friends_name():
    new_friend = input('Please enter friends name you want to add. Only Letters and whitespaces allowed')

    while True:
        if all(x.isalpha() or x.isspace() for x in new_friend):
            return new_friend
        new_friend = input('Please enter friends name you want to add. Only Letters and whitespaces allowed')  

def check_list():
    possible_lists = ('abcd')
    add_friend_to_list = input('Into which list you want to add friend? A,B,C,D')
    
    while True:
        if add_friend_to_list.lower() in possible_lists:
            return add_friend_to_list.lower()
        add_friend_to_list = input('Into which list you want to add friend? A,B,C,D')
     


#Create new friend instnace and add to list
def add_friend():
    last_contacted = date.strftime("%Y/%m/%d")
    day_number = date.strftime("%j")
    
    friend_name = check_friends_name()
    
    list_to_add = check_list()
    
    #appends friend to chosen list
    if list_to_add == 'a':
        print('Friend successfully added to list A')
        return a_list.append({'name': friend_name, 'last_contacted': last_contacted, 'day_number': day_number})
    elif list_to_add == 'b':
        print('Friend successfully added to list B')
        return b_list.append({'name': friend_name, 'last_contacted': last_contacted, 'day_number': day_number})
        
    elif list_to_add == 'c':
        print('Friend successfully added to list C')
        return c_list.append({'name': friend_name, 'last_contacted': last_contacted, 'day_number': day_number})
        
    elif list_to_add == 'd':
        print('Friend successfully added to list D')
        return d_list.append({'name': friend_name, 'last_contacted': last_contacted, 'day_number': day_number})


#Remove_friend function
def remove_friend():
    #which friend to remove?
    #find friend if found remove + message removed
    #if friend not found + message no friend found


#Edit_friends name
def edit_friend():
    #which friend to edit?
    #Rename friend if found
    #if friend not found, error

#Move friend from one list to another
def move_friend_to_other_list():
    #which friend
        #if friend found
            #to which list?
                #if list found
                    #move friend + success message
                #else:
                    #list not found + error message
        #else:
            #friend not found + error message


#Friend has been contacted - to reset meter

#System check - checks lists for which friends to contact

#Systems - Send reminder to contact friend - #Email via sendgrid etc.



