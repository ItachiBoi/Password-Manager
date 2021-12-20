#imports:-
import os


#Getting the MASTER PASSWORD:-
def master():

    main_password = input('Make a master password for ur acc:- ')
    recheck = input('Pls re-enter the password:- ')
    
    if recheck == main_password:
        with open('master.txt','a') as f:
            a = f.writelines(main_password)
            return a


    else:
        while recheck != main_password:
            input('the password is wrong, pls re-enter:- ')

            if recheck == main_password:
                save_site()
                print('Here u go ahead...')
                break        







# Entering the manager and checking of master passcode:- 
def save_site():
    z = input('Enter the master password:- ')

    with open('master.txt','r') as l:
        c = l.readline()
        
    if z == c:
        print('Correct password! Here u go ahead...')
        True 
        entry()
        

    
    else:
        while True:
            u = input('Wrong password, pls enter the correct password:- ')
            if u == c:
                print('Correct password! Here u go ahead!')
                entry()
                break 
            
                


#Saving of the password and website...
def entry():
    ask = int(input('Do u want to save(enter 1) or Retrieve data(enter 2)? '))
    if ask == 1:
        website = input('Enter the name of the website u r saving the password for:- ')
        password = input('Enter the password:- ')

        with open(f'{website}.txt','a') as g:
            g.write(f'{website} - {password}')
        print('The data has been saved!')

    if ask == 2:
        retrieve()

#Retrieving the password:- 
def retrieve():

    retrieve = input('Enter the website name: ')
    try:
        with open(f'{retrieve}.txt','r') as brrr:
            grrr = brrr.readline()
            print(grrr)

    except:
        print('U havent saved this...')





with open('master.txt','r') as k:
    o = k.readline()
    if len(o) == 0:
        master()
    else:
        save_site()