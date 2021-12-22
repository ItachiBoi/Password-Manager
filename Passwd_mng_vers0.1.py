import json


# ------------------------------------------> THE ENTRY PART <----------------------------------------

# Enter the master password and making acc:- 
def json_stuff():
    global master
    global acc
    global master_acc
    print('We are making an acc for u...')
    acc = input('Enter the acc name:- ')
    master = input('Enter the master passwd:- ')

    master_acc = {  "data":
    {"master_passwd": master} }


    json_string = json.dumps(master_acc, indent = 4)

    with open(f"{acc}.json",'a') as f:
        f.write(json_string)
    recheck()




#recheck the password:- 
def recheck():
    global recheck_master
    recheck_master = input('Enter the master password again:- ')

    if recheck_master == master:
        print('Correct! Here u go ahead...')
        options()

    else:
        while recheck != master:
            recheck_master2 = input(' ')

            if recheck_master2 == master:
                print('Here u go ahead')
                options()
                break




def fool(): # asks the master password for a change 

    try:
        ask_acc = input('Enter ur acc name:- ')
        lmfao = input('Enter the password')

        with open(f"{ask_acc}.json",'r+') as oop:
            wtf = json.load(oop)
            bruh = (wtf["data"]["master_passwd"])
            oop.close()


        if bruh == lmfao:
            print('So now u can change the password')
            lmfao2 = input('Enter the changed password:- ')


            (wtf["data"]["master_passwd"]) = lmfao2
            json.dump(wtf, open(f"{ask_acc}.json", "w"))
            options()
            
            
        else:
            while bruh != lmfao:
                lmfao3 = input('Wrong password, ur a fake bitch, pls fuck off, k have some formalities so PLS ENTER THE CORRECT PASSWORD')
                if lmfao3 == bruh:
                    print('So now u can change the password')
                    lmfao4 = input('Enter the changed password:- ')

                    wtf["master_passwd"] = lmfao4
                    
                    json.dump(wtf, open(f"{ask_acc}.json", "w"))
                    options()
                    break
                
    except FileNotFoundError :
        print('Pls make an acc first...')
        json_stuff()


            


def password_and_sitename(): # adds the website and password
    global ofc_acc
    global pillow_data
    global pillow
    try:
        ofc_acc = input('Enter ur acc:- ')
        master_bruh = input('Enter the master password:- ')

        pillow = open(f'{ofc_acc}.json')
        pillow_data = json.load(pillow)
        tv = (pillow_data["data"]["master_passwd"])

        if tv == master_bruh:
            print('k here u go ahead....')
            password_and_sitename_main()
        else:
            while tv!= master_bruh:
                tv2 = input('Wrong password, ur a fake bitch, pls fuck off, k have some formalities so PLS ENTER THE CORRECT PASSWORD ')
                if tv2 == tv:
                    print('Ok, here u go ahead...')
                    password_and_sitename_main()
                    break


    except FileNotFoundError:
        print('U have not made an account yet, pls make one first bitch, how tf can u change the password stupid little brat...')
        json_stuff()




def password_and_sitename_main():
    website = input('Enter the name of the website:- ')
    the_main = input('Enter the password for that website, dont think if it will be safe or not(we can do anything btw, just telling):- ')

    with open(f"{ofc_acc}.json",'r+') as google:
        google_data = json.load(google)
        google_data["data"].update({website:the_main})
        
        google.seek(0)

        json.dump(google_data, google, indent = 4)
        print('It has been added to ur acc, Thank u :)')
        options()




# --------------------------------------------> THE RETRIEVING PART and some more things <---------------------------------------






def paper(): # retrieve sys
    try:
        bruh_udk_a_shit = input('Enter ur username:- ')
        wasowiski = input('Enter the master password:- ')


        x = open(f"{bruh_udk_a_shit}.json")
        kekwut = json.load(x)
        kek = (kekwut["data"]["master_passwd"])
        

        if kek == wasowiski:
            print("lemme tell ur stupid(jk jk), nvm, so the password's right, here u go ahead")

            r_website = input('Enter the website name:- ')        
            password_only = (kekwut["data"][r_website])
            print(f"the password of {r_website} is {password_only}")
            options()

        else:
            while kek != wasowiski:
                highlighter = input('Wrong password, pls enter the right one:- ')
                if highlighter == kek:
                    print("lemme tell ur stupid(jk jk), nvm, so the password's right, here u go ahead")
                    r_website1 = input('Enter the website name:- ')
                    password_only_wdym = (kekwut["data"][r_website1])
                    print(f"the passwrd of {r_website1} is {password_only_wdym}")
                    options()
                    

    except FileNotFoundError:
        print('U have not made an account yet, pls make one first bitch, how tf can u change the password stupid little brat...')
        json_stuff()

 



def ask_bruh(): # just a part of changing the password
    global pencil
    global bottle
    try:
        bottle = input('Enter the acc name:- ')
        bottle_grey = input('Enter the master password: ')

        pen = open(f"{bottle}.json")
        pencil = json.load(pen)

        notebook = (pencil["data"]["master_passwd"])
        if notebook == bottle_grey:
            print('Right, here u go ahead')
            actual_thing()
        
        else:
            while notebook!=bottle_grey:
                bottle_grey = input('U stupid fucking bitch pls enter the right one! ')
                if notebook == bottle_grey:
                    print('Right password! Here u go ahead')
                    actual_thing()
                    break

    except FileNotFoundError:
        print('U have not made an account yet, pls make one first bitch, how tf can u change the password stupid little brat...')
        json_stuff()
  


           
def actual_thing(): #--> it updates the password
    history = input('Enter the website name:- ')
    change = input('Enter the changed password, dont think if it will be safe or not(btw we can do anything, just telling...):- ')
    (pencil["data"][history]) = change
    
    json.dump(pencil, open(f"{bottle}.json", "w"))

    print(f'The password of {history} is successfully changed to {change}')
    json.dumps(pencil)
    options()



def options(): #opens up all the functions 
    cocacola = int(input('''
    Enter 1 for changing ur master password
    Enter 2 for saving ur website and password
    Enter 3 for retrieving ur passwords
    Enter 4 for updating ur passwords
    '''))
    

    if cocacola == 1:
        fool()

    if cocacola == 2:
        password_and_sitename()

    if cocacola == 3:
        paper()
    
    if cocacola == 4:
        ask_bruh()


options()