# 1. calculate how much one Oreo cookie is concerning : calories , sodium , carbohydrate , fat  
serving_size = 3 
calories = 160 
sodium = 190 
carbohydrate = 25 
fat = 7 
calories_per_cookie = calories / serving_size
print ("calories_per_cookie = ", calories_per_cookie ,"kcal")
sodium_per_cookie = sodium / serving_size 
print("sodium_per_cookie = ", sodium_per_cookie ,"mg")
carbohydrate_per_cookie = carbohydrate / serving_size
print("carbohydrate_per_cookie = " , carbohydrate_per_cookie ,"g" )
fat_per_cookie = fat / serving_size
print("fat_per_cookie = " , fat_per_cookie,"g")


# 2. create a user input that asks how much cookies you ate 
num_cookies = int(input ("please insert how many cookies you ate  ? "))

# 3. calculate how much calories , etc . you consumed 
total_calories = num_cookies * calories_per_cookie
print(" total_calories =  " , total_calories , "kcal")

total_sodium = num_cookies * sodium_per_cookie
print(' total_sodium = ', total_sodium,"mg")

total_carbohydrate = num_cookies *  carbohydrate_per_cookie
print(" total_carbohydrate = " , total_carbohydrate , "g")

total_fat = num_cookies * fat_per_cookie
print(" total_fat = " , total_fat , "g")


# 4.warn the user if he/she surpasses 2000kcal he/she should stop eating these darn delicious cookies 
if total_calories > 2000 :
    print ("WARNING : stop eating cookies .")


# 5. use variables!
