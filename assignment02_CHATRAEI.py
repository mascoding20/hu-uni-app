#Create a simple to_do list using a list . Make sure the code contains the following 
#actions as listed below (this can be sequential i.e. in steps so no need to overthink it): 

to_do_list = [ "add a task to the to_do list with append ()","add a task to the to_do list with an input()","print the number of tasks in the to_do list"]

# 1.add a task to the to_do list with append ()
to_do_list.append("remove the first task of the to_do list ")

# 2.add a task to the to_do list with an input()
new_task = input("please enter a new task : ")
to_do_list.append(new_task)

# 3.print the number of tasks in the to_do list
Number_of_tasks = len(to_do_list)
print("Number_of_tasks = " , Number_of_tasks) 

# 4.remove the first task of the to_do list 
to_do_list.pop(0)

# 5.remove a specific task of the to_do list 
to_do_list.remove("add a task to the to_do list with an input()")


# 6.tell the user that if he/she has less than 4 tasks on the to_do list she has time to do more tasks 
Number_of_tasks = len(to_do_list)
if (Number_of_tasks < 4 ):
    print("You have time to do more tasks. ")

# 7.tell the user that if he/she has more or equal than 6 items she has no room to do more tasks 
if (Number_of_tasks >= 6 ):
    print("You have no more room to do more tasks ! ")