# print("Esc + R convert cell to RAW - Plain text and Esc + Y will convert cell back to code")
# print("This is my VS code python")
# print("This is raw")

# usama_bio = [
#     "Name: Muhammad Usama",
#     "F.Name: Muhammad Sabir",
#     "Occupation: Student",
#     "Course: Cloud Data Engineering",
#     "Center: Saylani Mass IT Program",
#     "Roll Number: 456987",
#     "I am a student odf saylani mass it training program. I am currently learning CDE at saylani. My instruction name is Qasim Hasan"
# ]
# # print(usama_bio)

# num = int(input("Enter your number: "))

# if num%5 == 0:
#     print("Hello")
# else:
#      print("Bye")

# length_1 = int(input("Enter the length: "))
# breadth_1 = int(input("Enter the breadth: "))

# if length_1 == breadth_1:
#  print("It is a square")
# else:
#  print("It is a rectangle")
# user_intake1 = int(input("Enter your first number: "))
# user_intake2 = int(input("Enter your second number: "))

# if user_intake1 > user_intake2:
#  print("First number is greater than second number", user_intake1)
# else:
#  print("Second number is greater than first number", user_intake2)


# print("Our product price is 100")
# price = 100
# discount = 10
# discount_on = 1000
# user_input = int(input("Please enter the total quantity of your purchase: "))
# total_cost = user_input*price
# discounted_price = total_cost - total_cost/discount

# if total_cost >= discount_on:
#     print("Your total cost after discount is: ", int(discounted_price))
# else:
#     print("You are not eligible for discount")

# age1 = int(input("Enter your age 1: "))
# age2 = int(input("Enter your age 1: "))
# age3 = int(input("Enter your age 1: "))

# if age1 >= age2 and age1 >= age3:
#  oldest_age = age1
# elif age2 >= age1 and age2 >= age3:
#  oldest_age = age2
# else:
#  oldest_age = age3

# if age1 <= age2 and age1 <= age3:
#   youngest_age = age1
# elif age2 <= age1 and age2 <= age3:
#   youngest_age = age2
# else:
#   youngest_age = age3

# print(f"oldest age is {oldest_age}")
# print(f"youngest age is {youngest_age}")


# user_units = int(input("Enter your units25"))

# if user_units >=0 and user_units <= 100:
#     print("Your bill is: Free")
# elif user_units >= 101 and user_units <= 200:
#     print(f"Your bill is: {int(user_units *5)}")
# else:
#     print(f"Your bill is: {int(user_units * 10)}")


# attended_classes = int(input("Enter your number of attended classes: "))
# held_classes = int(input("Enter your number of held classes: "))
# medical_leave = input("Are you on medical leaves (Yes or No): ")
# total_classes = (attended_classes / held_classes) * 100


# if total_classes >= 75:
#  print("You are allowed to sit in examn!")
# elif medical_leave == "Yes":
#  print("You are allowed to sit in examn!")
# else:
#  print("You are not allowed to sit in exam!")




# total_marks = 100
# std_num = int(input("Please enter your marks to see your grade: "))

# if std_num >= 25 and std_num <= 45:
#  print("Your Grade is E")
# elif std_num >= 45 and std_num <= 50:
#  print("Your Grade is D")
# elif std_num >= 50 and std_num <= 60:
#  print("Your Grade is C")
# elif std_num >= 60 and std_num <= 80:
#  print("Your Grade is B")
# elif std_num >= 80:
#  print("Your Grade is A")

# else:
#  print("You are Fail")

# user_input = int(input("Enter your five digit number: "))

# if user_input%10:
#  print(f"Your last digit is: {user_input%10}")
# else:
#  print("ERROR")


# user_age = int(input("Enter your Age: "))
# user_gender = input("Enter your Gender (male or female): ")
# user_marital_status = input("Enter your Marital Status (yes or no): ")

# if user_gender == "female":
#  print("You will work in Urban Area only!")
# elif user_gender == "male" and user_age >= 20 and user_age <= 40:
#  print("You can work in Anywhere!")
# elif user_gender == "male" and user_age >= 40 and user_age <= 60:
#  print("You will work in Urban Area only!")
# else:
#  print("ERROR")



# user_salary = int(input("Enter your Gross Salary: "))
# user_service = int(input("Enter your Years of Service: "))
# bonus = user_salary * 0.05
# if user_service > 5:
#  print(f"Your Net Bonus is: {bonus}")
# else:
#  print("You are not eligible for Bonus")