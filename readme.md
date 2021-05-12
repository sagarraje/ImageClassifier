![alt text](https://github.com/sagarraje/ImageClassifier/blob/main/certification.png?raw=true)

Meets Specifications
Dear Student,

Congratulations!!!!:clap::clap::clap::clap:
You’ve successfully passed all the specifications in this submission and I must admit that the structure of this project implementation is good. Going through the work, I could appreciate the time and effort put into this submission as it meets all the principal objectives. The results obtained from your models clearly proves how excellent your implementation was. :+1:


HAPPY NEW YEAR!!!!
Additional Materials
Learning Python: From Zero to Hero
30 Python Best Practices, Tips, And Tricks
Learn Python from Top 50 Articles for the Past Year (v.2019)
Python & Object-Oriented Programming
Classify Images Using Convolutional Neural Networks & Python

Timing Code
Student calls the time functions before the start of main code and after the main logic has been finished.

Well done measuring execution time. This is the first step in the process of code optimization. Keep it up!

Comments
Python's time module has a handy function called sleep(). Essentially, as the name implies, it pauses your Python program. time.sleep() is the equivalent to the Bash shell's sleep command. Almost all programming languages have this feature, and is used in many use-cases.

Tips
Here are some documents on the topic.

Time a Python Function
Python time measure function
Time access and conversions
Time Functions in Python
Command Line arguments
adds command line argument for '--dir'
uses default ='pet_images/'

Good work! the output of the python check_images.py --dir pet_images/ is superb.:+1:

Extra Resources
The purpose of command line arguments is to provide a way for your programs to be more flexible by allowing external inputs (command line arguments)
to be input into a program. The key is that these external arguments can change as to allow more flexibility in the program.
Please check some links provided below to know more:
The Easy Guide to Python Command Line Arguments
Parser for command-line options, arguments and sub-commands
How to Write Perfect Python Command-line Interfaces
adds command line argument for '--arch'
default='vgg'

Nice to see that the --arch argument has been used in your work with default='vgg' as required.:+1:

adds command line argument for '--dogfile'
default='dognames.txt'

python check_images.py --dogfile dognames.txt gives a good result. Keep working hard!

Pet Image Labels
Makes sure files starting with '.' are ignored.
Checks for '.' using a conditional statement.

Good work ignoring filenames starting with '.'.

Extra Resources
Working With Files in Python
Filenames and file paths in Python

Dictionary key and label are in the correct format and retrieves 40 key-value pairs.
e.g:- {'Poodle_07956.jpg': ['poodle'], 'fox_squirrel_01.jpg': ['fox squirrel'] ... }

Well done!!!

Extra Resources
Python | Ways to create a dictionary of Lists
Dictionaries in Python
'in_arg.dir' is passed as an argument inside check_images.py while calling the get_pet_labels function.

Nice implementation of the get_pet_labels() function. And, the argument passed in as the parameter of this function is reasonable.

Classifying Images
Appends images_dir to each value before making the function call.

classifier(images_dir+users_key, model)

Great work here!:clap:

Convert the output to lower case and strip any whitespaces

The lower() and strip() functions do the required work.

Comment
The lower() et strip() functions are among the string methods. Here is a document that presents other string methods with some good examples.

String Methods Part 1
Note that you have used the required functions, but the above document is only provided for more information on string methods.

Extra Resources
Python String Formatting Best Practices
Python String Methods

Appends 1 to correct label, and 0 to falsely classified values

Your work appends 1 to correct label, and 0 to falsely classified values. Great!

Classifying Labels as Dogs
Check the displayed output and see if all matches are appropriately displayed.

All matches are appropriately displayed in the display output. Good job!

Check the displayed output and see if all non matches are appropriately displayed

All non-matches are appropriately displayed in the display output.:+1:

Results
All three models score as expected.

Well done with all models' scores.

![alt text](https://github.com/sagarraje/ImageClassifier/blob/main/code.png?raw=true)


