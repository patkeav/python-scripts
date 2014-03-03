def _reverse_string( string ):
    str1 = ''
    for s in string:
        str1 = s + str1
    return str1

def _substring( string, first_index, last_index ):
    str1 = string[first_index:last_index]
    return str1

def _contains( string, character):
    for ch in string:
        if ch == character:
            return True
        else:
            return False

def _swap_values ( var1, var2 ):
    var3 = var1
    var4 = var2
    var2 = var3
    var1 = var4
    print("var1 = " + var1 + " \nvar2 = " + var2)

def _count_characters ( string ):
    return len(string);
