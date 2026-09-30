#The following script / study material was gathered from ChatGPT by uploading the class lecture slides, and asking for a list of 'command → what it does' operations. Verify in your own code before useage. 
#==================================


PYTHON COMMAND / SYNTAX DEFINITIONS — SLIDES 1–99


=== BASIC OUTPUT / VARIABLES ===

print() — Displays/output information to the console.

print("text") — Prints text.

print(variable) — Prints the value stored in a variable.

print(a, b, c) — Prints multiple items at once.

\n — New-line character; moves output to the next line.

\t — Tab character; inserts horizontal spacing.

str(value) — Converts a value into a string.

%d — Placeholder used to format an integer into a string.

% — When used in string formatting, inserts a value into a placeholder.

x = value — Assigns a value to a variable.

x, y = 1, 2 — Assigns multiple variables at once.

x, y = y, x — Swaps the values of x and y.


=== FUNCTIONS / UDFs ===

def function_name(): — Defines/creates a User Defined Function (UDF).

def function_name(argument): — Defines a function that accepts an argument.

def function_name(arg1, arg2): — Defines a function with multiple arguments.

function_name() — Calls/runs a function.

function_name(value) — Calls a function and passes it an argument.

function_name(value1, value2) — Calls a function with multiple arguments.

return value — Sends a result back from a function and ends that function.

return value1, value2 — Returns multiple values from a function.

a, b = function_name() — Stores multiple returned values into separate variables.

def main(): — Defines a main/driver function used to organize the program.

main() — Calls/runs the main function.


=== USER INPUT / DATA TYPES ===

input("Message") — Prompts the user for input and returns the input as a string.

eval(value) — Evaluates a string as Python code/expression; powerful but unsafe for untrusted input.

type(value) — Returns the data type of a value.

int(value) — Converts a value to an integer.

float(value) — Converts a value to a floating-point/decimal number.

str(value) — Converts a value to a string.

bool(value) — Converts a value to True or False.

True — Boolean true value.

False — Boolean false value.


=== BASIC OPERATORS ===

+ — Addition; also concatenates lists or strings.

- — Subtraction.

* — Multiplication; can also repeat strings, lists, or tuples.

/ — Division.

% — Modulus/remainder operator.

+= — Adds a value to a variable and stores the new result.
Example: x += 1 is the same as x = x + 1.

-= — Subtracts and stores the result.

== — Checks whether two values are equal.

!= — Checks whether two values are NOT equal.

> — Greater than.

< — Less than.

>= — Greater than or equal to.

<= — Less than or equal to.


=== FOR LOOPS / RANGE ===

for i in sequence: — Repeats code once for each item in a sequence.

for i in range(n): — Repeats from 0 through n-1.

range(stop) — Generates values from 0 up to, but not including, stop.

range(start, stop) — Generates values from start up to, but not including, stop.

range(start, stop, step) — Generates values using a specified increment/decrement.

range(1, 10, 2) — Counts upward by 2.

range(10, 0, -1) — Counts backward by 1.

print(value, end=" ") — Changes what print() places after its output instead of a new line.

print(a, b, sep="_") — Changes the separator between multiple printed values.

print(a, b, sep="_", end="") — Controls both the separator and ending character.


=== LISTS ===

[] — Creates a list.

my_list = [1, 2, 3] — Creates a list containing several values.

[] — By itself creates an empty list.

list1 + list2 — Combines/concatenates two lists.

list1 * 3 — Repeats the contents of a list three times.

list[index] — Accesses one item in a list.

list[0] — Accesses the first item.

list[-1] — Accesses the last item.

list[-2] — Accesses the second-to-last item.

list[start:stop] — Returns a slice from start through stop-1.

list[:stop] — Slices from the beginning through stop-1.

list[start:] — Slices from start through the end.

list[:] — Refers to/copies the entire sequence.

list[start:stop:step] — Slices a list while skipping according to step.

list[0:9:2] — Takes every second item from indexes 0 through 8.

list[index] = value — Changes an item in a mutable list.

list[start:stop] = [...] — Replaces a section of a list.

list[:] = [] — Removes all elements from the existing list.


=== LIST FUNCTIONS / METHODS ===

list.append(x) — Adds one item to the end of a list.

list.extend(other_list) — Adds all items from another iterable to the end.

list.insert(index, x) — Inserts an item at a specified index.

list.remove(x) — Removes the first occurrence of a specified value.

list.pop() — Removes and returns the last item.

list.pop(index) — Removes and returns an item at a specified index.

list.clear() — Removes every item from a list.

list.index(x) — Returns the index of the first occurrence of x.

list.count(x) — Counts how many times x appears.

list.sort() — Sorts the list in place.

list.reverse() — Reverses the list in place.

list.copy() — Creates a shallow copy of a list.

len(list) — Returns the number of elements in the list.

min(list) — Returns the minimum/smallest item.

max(list) — Returns the maximum/largest item.

  #==========================================
  #                  CONTINUED    
  #==========================================

=== STRINGS ===

"text" — Creates a string.

'text' — Also creates a string.

string1 + string2 — Concatenates strings.

string * 3 — Repeats a string.

string[index] — Accesses a character at an index.

string += "text" — Adds text to the end by creating a new string value.

len(string) — Returns the number of characters in a string.

min(string) — Returns the character with the lowest ordering value.

max(string) — Returns the character with the highest ordering value.

for character in string: — Loops through a string one character at a time.

Strings are immutable — Individual characters cannot be directly changed with string[index] = value.


=== STRING METHODS ===

string.capitalize() — Capitalizes the first character and lowercases the rest.

string.upper() — Converts all letters to uppercase.

string.lower() — Converts all letters to lowercase.

string.strip() — Removes whitespace from both ends.

string.rstrip() — Removes whitespace from the right/end.

string.find(sub) — Returns the first index where a substring occurs; returns -1 if not found.

string.rfind(sub) — Searches from the right/back for a substring.

string.replace(old, new) — Replaces occurrences of old text with new text.

string.split() — Splits a string into a list of substrings.

separator.join(iterable) — Joins multiple strings using the specified separator.

string.count(sub) — Counts occurrences of a substring.

string.startswith(prefix) — Returns True if the string begins with prefix.

string.endswith(suffix) — Returns True if the string ends with suffix.

string.isnumeric() — Returns True if the characters are numeric.

string.isdigit() — Returns True if the characters are digits.

string.isalpha() — Returns True if all characters are alphabetic letters.

string.isspace() — Returns True if all characters are whitespace.

"{}".format(value) — Inserts values into placeholders in a formatted string.

"{0} {1}".format(a, b) — Inserts values based on numbered placeholders.

f"{variable}" — F-string; inserts a variable directly into a formatted string.

=== DELETE ===

del variable — Deletes a variable/object reference.

del list[index] — Deletes one list element.

del list[start:stop] — Deletes a section of a list.

del list[:] — Deletes all elements from a list.


=== CONDITIONAL STATEMENTS ===

if condition: — Runs code only if the condition is True.

elif condition: — Checks another condition if the previous if/elif was False.

else: — Runs when none of the previous conditions were True.

if value: — Tests the truthiness of a value.

0 — Treated as False in a Boolean context.

Non-zero number — Treated as True in a Boolean context.


=== LOGICAL OPERATORS ===

and — True only when both conditions are True.

or — True when at least one condition is True.

in — Checks whether an item exists inside a sequence.

not in — Checks whether an item does NOT exist inside a sequence.

x in list — Checks whether x is inside a list.

"text" in string — Checks whether text occurs inside a string.


=== WHILE LOOPS ===

while condition: — Repeats code as long as the condition remains True.

while True: — Creates an indefinite/infinite loop until something stops it.

break — Immediately exits the current loop.

continue — Skips the rest of the current iteration and begins the next iteration.

Nested loop — A loop placed inside another loop.


=== TUPLES ===

() — Used to create a tuple.

tuple1 = (1, 2, 3) — Creates a tuple.

tuple[index] — Accesses an element in a tuple.

tuple[start:stop] — Slices a tuple.

tuple1 + tuple2 — Creates a new tuple by combining two tuples.

tuple * 2 — Creates a new tuple with repeated contents.

len(tuple) — Returns the number of elements.

max(tuple) — Returns the largest element.

min(tuple) — Returns the smallest element.

tuple.count(x) — Counts occurrences of x.

tuple.index(x) — Returns the index of the first occurrence of x.

x in tuple — Checks whether x is present.

x not in tuple — Checks whether x is absent.

Tuples are immutable — Existing tuple elements cannot be changed, added, or removed.


=== CONVERSION BETWEEN SEQUENCE TYPES ===

list(value) — Converts an iterable into a list.

list(tuple) — Converts a tuple into a list.

list(range(...)) — Converts a range into a list.

list("Hello") — Converts a string into a list of characters.

tuple(value) — Converts an iterable into a tuple.

tuple(list) — Converts a list into a tuple.

tuple(range(...)) — Converts a range into a tuple.

tuple("Hello") — Converts a string into a tuple of characters.

#=========================


=== FUNCTION ARGUMENT OPTIONS ===

function(name="James", age=25) — Uses keyword/named arguments.

function(age=25, name="James") — Keyword arguments can be supplied out of positional order.

def function(name, age=25): — Defines a default value for an argument.

age=25 — Means age automatically equals 25 if the caller does not provide another value.

Required arguments must come before default arguments.

def function(required, optional=25): — Valid.

def function(optional=25, required): — Invalid.


=== MODULES / IMPORTING ===

import module — Imports an entire Python module.

import sys — Imports Python's sys module.

sys.path — Contains directories Python searches for modules.

sys.path.append("folder") — Adds another folder to Python's module search path.

import Circle — Imports the custom Circle.py module.

Circle.function() — Calls a function contained inside the Circle module.

from Circle import function — Imports one specific function from Circle.

from Circle import function1, function2 — Imports multiple specific functions.

from Circle import function as alias — Imports a function and gives it a shorter alias.

import Circle as alias — Imports an entire module under another name.

as — Creates an alias/nickname for an imported module or function.


=== LIBRARIES / MODULES MENTIONED ON SLIDE 99 ===

NumPy — Numerical computing, arrays, matrices, and mathematical operations.

Pandas — Data analysis and table/time-series manipulation.

Matplotlib — Plotting and data visualization.

SciPy — Scientific and engineering computation tools.

scikit-learn — Machine-learning and data-analysis tools.

TensorFlow / Keras — Machine-learning and deep-learning frameworks.

SymPy — Symbolic mathematics and algebra.

OpenCV — Computer-vision and image/video processing.

Pillow — Image manipulation and processing.

socket — Network communication.

pySerial — Serial-port communication with hardware/devices.

ROS libraries — Python tools/APIs used with the Robot Operating System.
