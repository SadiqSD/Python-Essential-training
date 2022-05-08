# we want to invent something that can count how many words are there
# in what you type

# text = "a s f e g f f g"
#
# dic  = {}
# for word in text.split():
#     if word in dic:
#         dic[word] += 1
#     else:
#         dic[word] = 1
#
# print(dic)
# y = ("Time", 2, "Name", [2.4, "6"])
# x = ("Time", 2, "Name", [2.4, "6"])
# print(id(y[0]))
# print(id(x[0]))


#a textarea that allows you to type a specific words. and the words are counted


text = """
my name is is my sadiq murtasla isa isa musa my name is sadiq isa musa
"""




#erros in python
#generators and decorators
#class

# class users_info:
#     def __int__(self):
#         self.name
#         self.surname
#         self.hobby
#
#
# user1 = users_info()
# user1.name = "sadiq"
# user1.surname = "murtala"
# user1.hobby = "codding"


#files


# for and while loops

# for i in range(1,10):
#     print("")
#The for loop follows the loop of numbers untile done it loop through items like nmbers and so on

#while loop, break
# l = 0
# while l < 6:
#     print(l, "you're my lover")
#     if l == 2:
#         break
#     l += 1



#erros

#object





#oop
#REASONS FOR OOP IN THE FIRST PLACE
# Python does not require to use objexts or classes
#complex programs are hard to keep organized
#objec-oriented programming organizes and structures code
#
#
#ourse pycharm for python developers or visual studio code


#Rivision of every single thing you did in python and HTML

#we have to learn about random fah


# secret_number = 10
# number_count = 0
# number_limit = 5
#
# while number_count < number_limit:
#     guess = int(input("guess the number "))
#     number_count += 1
#     if guess != secret_number:
#         print("you mother fucker you're wrong")
#         print(f"bro you nuber of guess is {number_count} ")
#     else:
#         print("yeah! let's go motherfucker you're fucking right")
#         break
#
# identifying odd and even numbers



#ask a user for passwrd and store it in a file called secret file
# calculated and even number out of numbers



# secret_nuber = 9
# guess_limit = 3
# guess_count = 0
#
# while guess_count < guess_limit:
#     friend_guess = int(input("can pls guess the number in my hands? "))
#     guess_count += 1
#     if friend_guess != secret_nuber:
#         print("sorry you guessed wrong")
#     else:
#         print("yey! you guessed right!! ")
#         break
# print("thanks for completing the game")
#
#




# def sadiq(name):
#     print(f"my name is {name}")
#
# sadiq("sadiq")
# user_input = input("Write some short story of yours ")
# dict = {}
# text_info = user_input
# for word in text_info.split():
#     if word in dict:
#         dict[word] += 1
#     else:
#         dict[word] = 1
# print(dict)



#you can also put waht the user said in a file

# def word_counter():
#     dict = {}
#     user_input = input("wirte a short story of yours ")
#     for words in user_input.split():
#         if words in dict:
#             dict[words] += 1
#         else:
#             dict[words] = 1
#                         #printing the function
#     file = open("README.md","x")
#     file.write("\nThe name tht was giving to me was sadiq murtala")
#     file.close()
# word_counter()
### operators
#comparison operator e.g <= >= > < == != e.t.c
### Arithmetic operations e.g // % * / + -
### logical operators e.g and or not
### identity operator e.g the test of two var e.g x is y, x is not y
### membership operator if a ver is a member of a collection e.g x in y, x not in y
### Bitwise operators

## me and dady songs
# legend never die
# ours @ legend never sleep, in the midle of the night



# Arithmetic operators
# x = 10
# y = 3
# z = x % y
# print(f"the result is {z}")

#compnarison
#boolean operators

# text = """
# a d t s a at h t s d v b a a s
# """
#
# dict = {}
#
# for word in text.split():
#     if word in dict:
#         dict[word] += 1
#     else:
#         dict[word] = 1
# print(dict)
# finally worked


# conditonal statement must learn





# def word_counter():
#     dict = {}
#     user_input = input("wirte a short story of yours ")
#     for words in user_input.split():
#         if words in dict:
#             dict[words] += 1
#         else:
#             dict[words] = 1
#      print(dict)
# items = {'turkey':1,'hen':2,'hat':2,'orange':3}
# for food in items:
#     if food == 'turkey': continue
#     print(food)
########



# These is the correct code
# class Books:
#     def __init__(self, title):
#         self.title = title
#
# b1 = Books("Just getting stated")
# print(b1.title)



# PLS be awere of the infected code
# class Books:
#     def __int__(self, title):
#         self.title = title
#
# b1 = Books("the new world")
# print(b1.title)




# This life is all about security and having to know what to do in the next
#time is to live or to exist

#classes are just like functions baby

class Person:
    def __init__(self,name,surname,id,eyecolor):
        self.name = name
        self.surname = surname
        self.id = id
        self.eyecolor = eyecolor


Emp1 = Person("sadiq", "Murtala", "Emp1", "Brown")


#Legit game of Guessing
#**********************************************************
# Learning python sranderd library
#logical operators
# is_rainning = False
# is_sunny = True
#
# if is_rainning and is_sunny:
#     print("we might see some rainbow")
#
# if is_sunny or is_rainning:
#     print("it might be sunny or rainny")
#
# if not is_rainning:
#     print("is not rainnt outside")
#comparison operators
# mouse = 1
# kitten = 10
# tiger = 80

# if mouse < kitten and mouse < tiger:
#     print("woow mr mouse you're way to small to be in a compatition rightnow")
# print(False > True)
# #claculating len()
# first_name = "sadiq"
# # print(len(firs_name))
# first_name.__len__()


#the list function in range(rand and list)
# p_list = [1,44,51,9,1,82,18,19]
# for i in range(0, len(p_list)):
#     print(p_list[i])
# number = range(30)
# print(list(number))

#
 #************************************** min and max
 #min: determines the minumum number amoung numbers
#Rouding, absollute(abs) valie and exponets
#round, will aproximate it to the nearset number
# myGPA = 11.7
# print("My GPA:",round(myGPA))
# apple = -1.2
#*********************************abs: will alway's return a positive number

# dist = -13
# print(abs(dist))
# tree_root = -2.5
# print(abs(round(tree_root)))
#*******************************pow function: for exponecial
# print(3**2)
# print(pow(3,2))
#********************************sorted function




#facebook problems
#******************    1
# text = "OpenEDG Python Institute"
# for letter in text:
#     if letter == "s":
#         break #but why break after looping throu letters?
#     print(letter)
#******************    2
# def full_name(first_last):
#     return first_last.split()
# name = full_name("Sarah snow")
# print(name)  # no reply yet
#the pop()method

# b = ("dog", "cat", "monkey")
# print(b)
#
# list = [99,2,3,5,4,6,7,6,33,9]
# print(list.pop())
# print(list)
#
# number = int(input("Enter a number: "))
#the ultimate one liner code.
#print("number is positive ")if number > 0 else  print("number is negetive ")if number < 0 else print("number is zero")



#push to git tomorrow


#password cheaker and generator

#you prompt the user about special characters
#if the special characters are not in the password print password is weak
#make sure the password reach some certain lenth before it can be a password

# user_password = int(input("Enter your password: "))
password = 2799497
for number in password:
    print("number: ",number)


#want to do files
#the random library
#jupyter notebook


#PUBLIC NOTE "int" object is not iterable

