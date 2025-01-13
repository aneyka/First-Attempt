'''
project_1.py: First project for Engeto Online Python Akademie

 author: Marta Martinkova
 email: marta@ufa.cas.cz
'''


# import of the string module
import string
 
# The texts to be analyzed stored in the list TEXTS #
#####################################################

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#################################################
# selection of the registered users; signing in #
#################################################

# The list of registered users is stored in a dictionary:
# the dictionary is created using dictionary comprehension
# from two tuples of same length;
# the tuples are called names and passwords.

# tuples
names = ('bob', 'ann', 'mike', 'liz')
passwords = ('123', 'pass123', 'password123', 'pass123')

# checking wheather the tuples have length
# creating the dictionary called users using dictionary comprehension

if len(names) == len(passwords):
    users = {names[i] : passwords[i] for i, _ in enumerate(names)}


# Promting the user for name and password

# the name is obtained from the user by function input()
# the name is a string
#
# methods of strings used for name:
#
# .strip() not necessary, to avoid accidental spaces etc.
#
# .lower() also not necessary, for a string to be normalized 
# to lowercase.
# Users generally don't care about case sensitivity in the names.
# Names are ussually stored in lower case.
#
# the method of strings used for password:
# .strip() also not necessary, to avoid accidental spaces etc.
# a password is case sensitive so no .lower()


name = input('Enter your name: ').strip().lower()
password = input('Enter your password: ').strip()

print('_' * 69)
 

# Selecting registered users by using if else:
# if: the user is registered, i.e. name and corresponding password found
# in the dictionary users,
#  the program continues + greeting
# alternatively, not here, .title() method to capitalize back 
# the first letter of the name
#
# else: program stops using function exit() + warning

if users.get(name) == password:
    print('Welcome to the text analysis program,', name)
else:
    print('Error: Name or password not found; terminating the program.')
    exit()

print('We have 3 texts to be analyzed.')
print('_' * 69)

########################################
# selection of the text to be analyzed #
########################################

choice = input('''Enter a number 
               btw. 1 and 3 to select the text: ''').strip()

# Validating the input and proceeding:
#  Input has to be a number 1, 2 or 3
#  Program has to validate wheather the input is a number 
#  Not clear wheather the the two conditions should be dealt with
#  separately. Dealing with them together:
#  .isdigit() checks wheather the data type is a number
#  int() convert 

if choice.isdigit() and 1<=int(choice) <= 3:
    selected_text = TEXTS[int(choice) - 1]
else:
    print('Invalid input. Please enter a number between 1 and 3.')
    exit()

print('_' * 69)

#############################################
# Text analysis: 6 statistics and a barplot #
#############################################

# The texts to be analyzed stored in the TEXTS in the begining

# spliting the text into words

words = selected_text.split()

# 6 different text statistics:

# 1] counting words in the selected text
num_words = len(words)

# 2] counting titlecase words
num_titlecase = sum( 1 for word in words 
                    if word.strip(string.punctuation).istitle())

# 3] counting uppercase words
num_uppercase = sum(1 for word in words 
                    if word.strip(string.punctuation).isupper() 
                    and word.strip(string.punctuation).isalpha())

# Debugging: where is the second word :
# uppercase_words = [word for word in words if word.strip(string.punctuation).isupper()]
#print(uppercase_words)
# 4] counting lowercase words
num_lowercase = sum(1 for word in words
                    if word.strip(string.punctuation).islower())
                    

# 5] counting numeric strings
num_numeric = sum(1 for word in words if word.isdigit())


# 6] summing all the numbers
sum_numbers = sum(int(word) for word in words if word.isdigit())


# printing of selected statistics
# 1] 
print(f'There are {num_words} words in the selected text.')
# 2]
print(f'There are {num_titlecase} titlecase words.')
# 3]
print(f'There are {num_uppercase} uppercase words.')
# 4]
print(f'There are {num_lowercase} lowercase words.')
# 5]
print(f'There are {num_numeric} numeric strings.')
# 6]
print(f'The sum of all the numbers is {sum_numbers}')

# Barplot of words lengths

# calculating the word lengths                                     
lengths = [len(word) for word in words if word]

# counting the frequency of each length
frequency = {}
for length in lengths:
   frequency[length] = frequency.get(length, 0) + 1


# Printing the barplot
print('_' * 69)
print('LEN|  OCCURENCES   |NR.')
print('_' * 69)



for length, count in sorted(frequency.items()):
    print(f'{length:3}| {'*' * count:13} |{count}') 



# Note: f-string from Python 3.6 in
# https://www.geeksforgeeks.org/
# formatted-string-literals-f-strings-python/




