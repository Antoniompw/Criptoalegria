import numpy as np

# Returns the alphabet of the file
def alphabet(filename):
    char_set = []
    with open(filename) as f:
        char = f.read(1)
        while(char):
            if not(ord(char) in char_set):
                char_set.append(ord(char))
            char = f.read(1)
    char_set.sort()
    return char_set

# Encripts a file and then retrieves the key
def enigma(filename):
    import random as rd
    # Constante utilizada frequêntemente
    KEY_LENGTH = len(alphabet(filename))
    # Init one cilinder
    cilinder1 = alphabet(filename)
    rd.shuffle(cilinder1)
    # IDEM
    cilinder2 = alphabet(filename)
    rd.shuffle(cilinder2)
    # IDEM
    cilinder3 = alphabet(filename)
    rd.shuffle(cilinder3)
    map_function = {}
    counter = 0
    for i in alphabet(filename):
        map_function[i] = counter
        counter = counter + 1

    f = open(filename)
    buffer = f.read()
    buffer = list(buffer)
    char_index = 0
    offset1 = 0
    offset2 = 0
    offset3 = 0
    while(char_index != len(buffer)):
        current_char = ord(buffer[char_index])
        # First phase
        respective_index = map_function[current_char]
        new_char = cilinder1[(respective_index + offset1)%KEY_LENGTH]
        # Second phase
        respective_index = map_function[new_char]
        new_char = cilinder2[(respective_index + offset2)%KEY_LENGTH]
        # Third phase
        respective_index = map_function[new_char]
        new_char = cilinder3[(respective_index + offset3)%KEY_LENGTH]
        buffer[char_index] = chr(new_char)
        char_index = char_index + 1
        offset1 = offset1 + 1
        if offset1 == KEY_LENGTH:
            offset1 = 0
            offset2 = offset2 + 1
            if offset2 == KEY_LENGTH:
                offset3 = offset3 + 1
                if offset3 == KEY_LENGTH:
                    offset1 = 0
                    offset2 = 0
                    offset3 = 0
    return buffer, cilinder1, cilinder2, cilinder3

def search(l, key):
    counter = 0
    for item in l:
        if item == key:
            return counter 
        counter = counter + 1
    return -1

def deencript(filename, cilinder1, cilinder2, cilinder3):
    # Constante utilizada frequêntemente
    KEY_LENGTH = len(cilinder1)
    numeric_set = cilinder1.copy()
    numeric_set.sort()
    f = open(filename)
    buffer = f.read()
    buffer = list(buffer)
    char_index = 0
    offset1 = 0
    offset2 = 0
    offset3 = 0
    while(char_index != len(buffer)-1):
        char_index = char_index + 1
        offset1 = offset1 + 1
        if offset1 == KEY_LENGTH:
            offset1 = 0
            offset2 = offset2 + 1
            if offset2 == KEY_LENGTH:
                offset3 = offset3 + 1
                if offset3 == KEY_LENGTH:
                    offset1 = 0
                    offset2 = 0
                    offset3 = 0

    map_function = {}
    counter = 0
    for i in alphabet(filename):
        map_function[i] = counter
        counter = counter + 1
    
    char_index = len(buffer) - 1
    while(True):
        current_char = ord(buffer[char_index])
        index = search(cilinder3, current_char) 
        if index >= offset3:
            index = index - offset3
        else:
            index = index - offset3
            index = index + KEY_LENGTH 
        current_char = numeric_set[index]
        index = search(cilinder2, current_char)
        if index >= offset2:
            index = index - offset2
        else:
            index = index - offset2
            index = index + KEY_LENGTH 
        current_char = numeric_set[index]
        index = search(cilinder1, current_char)
        if index >= offset1:
            index = index - offset1
        else:
            index = index - offset1
            index = index + KEY_LENGTH 

        current_char = numeric_set[index]
        buffer[char_index] = chr(current_char)
        char_index = char_index - 1
        offset1 = offset1 - 1
        if offset1 < 0:
            offset1 = KEY_LENGTH - 1
            offset2 = offset2 - 1
            if offset2 < 0:
                offset2 = KEY_LENGTH - 1
                offset3 = offset3 - 1
                if offset3 < 0:
                    offset1 = KEY_LENGTH - 1
                    offset2 = KEY_LENGTH - 1
                    offset3 = KEY_LENGTH - 1
                    break
    return buffer

filename = "test.txt"
buffer, cilinder1, cilinder2, cilinder3 = enigma(filename)
with open("encripted.txt", "w+") as f:
    for char in buffer:
        f.write(char)
filename = "encripted.txt"
buffer = deencript(filename, cilinder1, cilinder2, cilinder3)
with open("deencripted.txt", "w+") as f:
    for char in buffer:
        f.write(char)