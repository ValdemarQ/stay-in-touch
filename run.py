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

#Sort lists of friends into alphabetical order before displaying.

#what to do with class?
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
    
    friend_name = check_friends_name()
    
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


#Remove_friend function
def remove_friend():
    friend_name = check_friends_name()

    for i in lists:
        for person in lists[i]:
            if person['name'].lower() == friend_name.lower():
                print('Person found' ,person['name'],person['last_contacted'],'& deleted')
                del lists[i][lists[i].index(person)]
                return
    print('Friend not found')

#rename friend
def rename_friend():
    #whom to rename?
    print('Who you want to rename? Enter name')
    friend_name = check_friends_name()
    
    #loops lists to find if exists
    for i in lists:
        for y in lists[i]:
            if y['name'].lower() == friend_name.lower():
                print('Friend is found. Enter new name for a friend')
                new_name = check_friends_name()
                lists[i][lists[i].index(y)]['name'] = new_name
                return
    print('Friend not found')
                

#Move friend from one list to another
def move_to_other_list():
    friend_name = check_friends_name()
        
    for i in lists:
        for y in lists[i]:
            
            if y['name'].lower() == friend_name.lower():
                print('Friend is found!')
                new_list = check_list()
        
                if new_list == 'a':
                    lists['a_list'].append(lists[i][lists[i].index(y)])
                    del lists[i][lists[i].index(y)]
                    print('Friend successfully moved to List A')
                    return
                    
                elif new_list == 'b':
                    lists['b_list'].append(lists[i][lists[i].index(y)])
                    del lists[i][lists[i].index(y)]
                    print('Friend successfully moved to List B')
                    return
                
                elif new_list =='c':
                    lists['c_list'].append(lists[i][lists[i].index(y)])
                    del lists[i][lists[i].index(y)]
                    print('Friend successfully moved to List C')
                    return
                
                elif new_list == 'd':
                    lists['d_list'].append(lists[i][lists[i].index(y)])
                    del lists[i][lists[i].index(y)]
                    print('Friend successfully moved to List D')
                    return
                
    print('Sorry, something went wrong')



#Friend has been contacted - to reset meter

#System check - checks lists for which friends to contact

#Systems - Send reminder to contact friend - #Email via sendgrid etc.

#Check for duplicaates if friend exists - so no duplicate items.

