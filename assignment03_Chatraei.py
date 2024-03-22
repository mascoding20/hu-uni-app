#Create a static dictionary with a number of users  and with the following values :
# 1.First name  # 2.Last name   # 3.Email address  # 4.Password
users = {
    "user_1": {"First_name":"masoud" , "Last_name": "chatraei","Email_address":"masoud_ch@gmail.com", "password":"Mas1@ch"},
    "user_2": {"First_name":"harry" , "Last_name": "potter","Email_address":"harry.potter@hogwarts.com", "password":"voldeMort1!"},
    "user_3": {"First_name":"tom" , "Last_name":"jerry" ,"Email_address":"catmouse@mgm.com", "password":"Tojer2"},
    "user_4": {"First_name": "dobby", "Last_name": "elf","Email_address":"elf.d@elfs.com", "password":"socks"}
 }

#Ask the user for :
# 5.Email address 
# 6.Password 

input_email = input("Please enter your email address : ")
input_password = input("Please enter your password :")

#Loop (for()) through the dictionary and if (if()) the user is found print the following :
# 7.Hello, first name last name you have successfully logged in 
# 8.Notify the user if the password and email address are wrong 
# 9.Additional challenge : if you want the program to keep asking for a username and password when the combination is wrong , you will need a while() loop 


for key,val in users.items(): 
   if input_email == val["Email_address"] and input_password == val["password"]:
      print(f"Hello",val["First_name"],val["Last_name"],"you have successfully logged in .")
      break
   else :
       print("Invalid email or password ")
logged_in = False
while True :

    
    input_email = input("Please enter your email address : ")
    input_password = input("Please enter your password :")
    
    for key,val in users.items(): 
        
        if input_email == val["Email_address"] and input_password == val["password"]:
            
            

            print(val["Email_address"],input_email,val["password"],input_password)
            print("ok")
            logged_in = True
            break

    if logged_in == True:
        break
   

