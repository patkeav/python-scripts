'''
This is a script that performs some basic tasks 
Patrick Keaveny , 2014
'''

'''
Reverses an input string
    @string = the string to be reversed
'''
def _reverse_string( string ):
    str1 = ''
    for s in string:
        str1 = s + str1
    return str1

'''
Creates a substring between two indexes
    @string = the original string
    @first_index = the starting index
    @last_index = the ending index
'''
def _substring( string, first_index, last_index ):
    str1 = string[first_index:last_index]
    return str1

'''
Determines whether a character is in a string
    @string = the original string
    @character = the character to search
'''
def _contains( string, character):
    for ch in string:
        if ch == character:
            return True
        else:
            return False

'''
Swaps the values of two variables
    @var1 = the first variable
    @var2 = the second variable
'''
def _swap_values ( var1, var2 ):
    var3 = var1
    var4 = var2
    var2 = var3
    var1 = var4
    print("var1 = " + var1 + " \nvar2 = " + var2)

'''
Counts the characters in a string
    @string = the original string
'''
def _count_characters ( string ):
    return len(string);
