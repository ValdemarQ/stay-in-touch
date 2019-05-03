import datetime

#Global variables
date = datetime.datetime.now()


#Print Greetings message with information

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


#Add_friend function
def add_friend_to_list():
    #date when friend added, as reference to when contact next 
    last_contacted = date.strftime("%a")
    day_number = date.strftime("%j")
    

    new_friend = input('Please enter  friends name you want to add to list')
    #check_friends_name()
    
    list_to_add = input('Into which list would you like to add this friend? A,B,C,D?')
    #to lowercase
    #check which list a,b,c,d
    #add new_friend to that list
    #else, error and ask to repeat the proccess and only A,B,C,D
    a_list.append({'name': new_friend,'list':list_to_add, 'last_contacted': last_contacted, 'day_number': day_number})

#check friends name, only lettters and whitespaces allowed
def check_friends_name():
    new_friend = input('Please enter friends name you want to add. Only Letters and whitespaces allowed')
    
    while True:
        if all(x.isalpha() or x.isspace() for x in new_friend):
            return new_friend
        new_friend = input('Please enter friends name you want to add. Only Letters and whitespaces allowed')   

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



