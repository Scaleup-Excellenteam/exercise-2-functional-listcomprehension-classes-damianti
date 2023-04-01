# exercise-2-functional-listcomprehension-classes-damianti

## Getting Started

To get started, clone this repository or download the exercises as a ZIP file. Then, open each exercise file in your favorite Python IDE or text editor. <br>
The name of each file starts with a number and after that a point. Python module names must follow certain naming conventions, and they cannot start with a number or contain dots. 
That's why you won't be able to import a module. 
# Exercises
## 1)  6.2.two_thousand_run
### Description: 
This file contains a function to measure the execution time of other functions.

### Usage

You can use the timer function to measure the execution time of any function. Simply pass the function to be measured as the first argument, followed by any arguments or keyword arguments that the function requires.

Here's an example:

    #the import is only able if you change the name of the file and use the new module name
    import 6.2.two_thousand_run as measure_time
    
    def my_function(arg1, arg2):
        # some code here
        pass

    #measure the execution time of my_function
    time_spent = measure_time.timer(my_function, arg1, arg2)
    print(f'Time taken: {time_spent:.10f} seconds')
    # measure the execution time of the print function
    time_spent = measure_time.timer(print, "Hello")
    print(f'Time taken: {time_spent:.10f} seconds')

## 2)  6.3.long_cat_is_cat
### Description:

This module has a function called count_words. It receives a text and returns a dictionary where the keys are every 
word (only the ones with latin letters) and the values are the number of letters that that word has. <br>
The count_words function removes all non-alphabetic characters and non-space characters from the input string using the
isalpha() and isspace() string methods. It then splits the cleaned string into words using the split() method and 
creates a dictionary comprehension that maps each word to its length using the len() function.

### Usage

You can use the count_words to count the length of the words of a given text. Simply pass the text to be measured 
as the first argument, followed by any arguments or keyword arguments that the function requires.

Here's an example:
    
    import 6.3.long_cat_is_cat as word_counter
    
    txt = 'you are awesome'
    print (word_counter.count_words(txt))
   
## 3)  6.4.remember_remember
### Description:
This module contains a function called decrypt_message. It uses the Python Imaging Library (PIL) to open the image at 
the given file path. It then retrieves the dimensions of the image using the size attribute of the Image object.

Using a list comprehension, the function finds the row number of the black pixel in each column of the image. It does
this by iterating over the columns of the image and finding the first row that contains a black pixel (represented by 
the value 1 in the image's binary representation). The getpixel method is used to access the pixel value at a given 
position.

The function then converts the row numbers to characters using the chr() function and concatenates them into a single
string. This string is the decrypted message extracted from the image.

### Usage

Note that this function assumes that the image contains a binary representation of the message, where black pixels
represent 1s and white pixels represent 0s.

The main block of the code demonstrates an example usage of the decrypt_message function by decrypting a message 
from an image file located at "resources/code.png". The resulting message is printed to the console.

## 4)  6.5.group_by
### Description:
The module contains a function called group_by. It iterates over each item in the iterable and applies the function 
func to it to determine its key. The function creates a new key-value pair in the dictionary result using the key
obtained from the function application. If the key is already in the dictionary, the item is appended to the existing
list value. If the key is not already in the dictionary, an empty list is created as the value for that key, and the
item is added to the list.

The resulting dictionary result maps each unique result of the function func to a list of items in the iterable that 
have that result.

### Usage
The main block of the code demonstrates an example usage of the group_by function. 
The function is called with the function len and a list of strings as arguments. The resulting dictionary groups the 
strings in the list according to their length, mapping each length to a list of strings that have that length. 
The resulting dictionary is printed to the console.

Overall, this code demonstrates a simple approach to grouping items in an iterable based on a key obtained by applying 
a function to each item in the iterable using a dictionary comprehension in Python.

## 5)  7.2.turtle_sent
### Description:
The PostOffice class allows users to send messages to each other, and includes methods for reading and searching inboxes.
In this exercise, I had to add two methods of the class: read_inbox and search_inbox. In order to do that, small changes
have been done in the function send_messages: it now receives the header of the mail. And inside it creates an dictionary
named message_details, where i added keys 'is_read', 'recipient' and 'header' in order to do the other methods.

### Usage
The main block of the code demonstrates an example usage of the PostOffice class.

### Type Checking Decorator Factory
In this exercise, you will create a decorator factory called type_check that takes one argument, a type, and returns a
decorator. This decorator checks if the first argument of the decorated function has the correct type. If the type is 
incorrect, it raises a custom TypeCheckError.

The solution should use the functools.wraps decorator to preserve the metadata of the decorated function.

Here's an example usage of the type_check decorator factory:

    @type_check(int)
    def times2(num):
        return num * 2
In this example, the times2 function should only accept integers as its first argument. If the argument is not an integer, a TypeCheckError should be raised.

#### Files:

- type_check_decorator_factory.py: The solution file containing the implementation of the type_check decorator factory, the TypeCheckError class, and the example times2 function.
