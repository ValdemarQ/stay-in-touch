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

#Add_friend function
def add_friend_to_list():
    new_friend = input('Please enter  friends name you want to add to list')
    #check atleast 3 chars
    #check for only alpha and spaces,no numbers
    
    list_to_add = input('Into which list would you like to add this friend? A,B,C,D?')
    #to lowercase
    #check which list a,b,c,d
    #add new_friend to that list
    #else, error and ask to repeat the proccess and only A,B,C,D
    
    #date when friend added, as reference to when contact next 
    date_when_added = date.strftime("%j")

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


#Systems - Send reminder to contact friend - #Email via sendgrid etc.



