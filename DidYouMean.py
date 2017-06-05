"""  DidYouMean.py
Author: Adjoa Darien
Last Modified: June 5, 2017
Description: Determines whether the word the user entered exists in the dictionary
being used --WordCount.txt. If the word does not exist as entered it will generate
alternative spellings of the word by deleting, transposing, substituting or
inserting letters and look for the generated spelling that exists in the dictionary
and appears most frequently.

Python 2.x
"""

def dictionary(filename):
    """
    Converts the WordCount.txt file into a dictionary.
    :param filename: a file containing words (keys) and their frequencies (values)
    :param oxford: an empty dictionary
    :param lines: an array of key-value pairs read from WordCount.txt
    :param legos: a word (key) and its frequency (value)
    :return: a dictionary containing word-frequency key-value pairs
    """
    # Convert WordCount.txt into an array called lines.
    # Split each key-value pair in the lines array.
    # Store words as keys and, frequencies as values.
    
    oxford = {}
    f = open(filename, "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        legos = line.split()
        oxford[legos[0]]= legos[1]

    return oxford   


def errorCheck():
    """
    Prompts the user to enter a word that will trigger the program to start or stop.
    Formats the entry so all letters are lowercase and, so it contains no blank spaces. 
    Verifies that the user has entered only letters.
    :param userIn: user entry
    :return: valid user entry
    """
    userIn = raw_input("Enter a word or QUIT to exit: ",)
    userIn = userIn.lower().strip()

    while (userIn != "quit"):
        while(userIn.isalpha() == False):
            print "That word was not valid."
            userIn = raw_input("Enter a word or QUIT to exit: ",)
            userIn = userIn.lower().strip()
        return userIn
    return userIn

def delete(userIn, oxford, oxfordAlt):
    """
    Generates alternative spellings of the user's entry by deleting each letter in turn.
    Each alternative spelling found in the dictionary of real words is added, with its
    frequency, to a dictionary of valid alternative spellings.
    :param userIn: valid user entry
    :param oxford: dictionary of real words
    :param oxfordAlt: dictionary of valid alternative spellings
    :param letter: an item in the list of letters which make up the user's entry
    :param entryList: the list form of the user's entry
    :param entryString: the string form of a list with a deleted letter
    """
    # Convert user's entry into a list and, remove each letter in turn.
        # Convert each resulting list into a string.
        # If it is a real word, add to oxfordAlt.
        
    for letter in range(len(userIn)):
        entryList = list(userIn)
        entryList.pop(letter)
        entryString = ""
        
        for letter in range(len(entryList)):
            entryString += entryList[letter]
        entryString.strip()
        
        if (entryString in oxford) == True:
            val = oxford[entryString]
            oxfordAlt[entryString]= val         


def transpose(userIn, oxford, oxfordAlt):
    """
    Generates alternative spellings of the user's entry by transposing its characters.
    :param userIn: valid user entry
    :param oxford: dictionary of real words
    :param oxfordAlt: dictionary of valid alternative spellings
    :param entryList: the list form of the user's entry
    :param find: the list form of the user's entry with characters transposed
    :param findMe: the string form of :param find:
    """
    # Convert user's entry into a list and, transpose each letter in turn.
        # Convert each resulting list into a string.
        # If it is a real word, add to oxfordAlt.
        # Return entryList to original user entry form. 

    entryList = list(userIn)
    for i in range(len(entryList)-1):
        find = swap(entryList , i)
        findMe = ""

        for letter in range(len(find)):
            findMe +=find[letter]
        findMe.strip()

        if (findMe in oxford) == True:
            val = oxford[findMe]
            oxfordAlt[findMe]= val

        entryList = swap(entryList , i)


def swap(swapThis, count):
    """
    Transposes neighbouring characters in a list.
    :param temp: an character holder
    :param swapThis: an array of characters
    :param count: character index
    :return: list with transposed characters
    """
    temp = swapThis[count]
    swapThis[count] = swapThis[count +1]
    swapThis[count +1] = temp

    return swapThis


def sub(userIn, oxford, oxfordAlt):
    """
    Generates alternative spellings of the user's entry by substituting each letter
    in it with every letter in the alphabet.
    :param userIn: valid user entry
    :param oxford: dictionary of real words
    :param oxfordAlt: dictionary of valid alternative spellings
    :param entryList: the list form of the user's entry
    :param letter: an item in the list of letters which make up the user's entry
    :param i: a (lowercase) letter in the alphabet
    :param entryString: the string form of a list with a substituted letter
    """
    # Convert user's entry into a list.
    # Substitute each letter with one from the alphabet in turn.
        # Convert each resulting list into a string.
        # If it is a real word, add to oxfordAlt.
        
    entryList = list(userIn)
    for letter in range(len(entryList)):
        for i in range(97,123):
            entryList[letter] = chr(i)
            entryString = ""

            for item in range(len(entryList)):
                entryString +=entryList[item]
            entryString.strip()
            
            if(entryString in oxford) == True:
                val = oxford[entryString]
                oxfordAlt[entryString] = val

            entryList = list(userIn)


def insert(userIn, oxford, oxfordAlt):
    """
    Generates alternative spellings of the user's entry by inserting each letter
    of the alphabet in place of each letter in the user's entry a letter of the entry at a time."
    :param userIn: valid user entry
    :param oxford: dictionary of real words
    :param oxfordAlt: dictionary of valid alternative spellings
    :param entryList: the list form of the user's entry
    :param entryString: the string form of a list with a substituted letter
    """
    # Convert user's entry into a list.
    # Insert (add) each letter from the alphabet next to each letter in turn.
        # Convert each resulting list into a string.
        # If it is a real word, add to oxfordAlt.
  
    entryList = list(userIn)
    for letter in range(len(entryList)+1):
        for i in range(97,123):
            entryList.insert(letter, chr(i))
            entryString = ""
            
            for item in range(len(entryList)):
                entryString +=entryList[item]
            entryString.strip()

            if (entryString in oxford) == True:
                val = oxford[entryString]
                oxfordAlt[entryString]= val
                
            entryList = list(userIn)

            
def main():
    """
    Runs the DidYouMean program until the user enters QUIT.
    First, convert WordCount.txt into a dictionary. Prompt the user to enter a word.
    Verify that the user has entered a word containing only letters with errorCheck().
    Once verified, create a blank dictionary to store valid alternative spellings
    generated by the following functions: delete(), transpose(), sub() and, insert().
    Sort the words in the dictionary of alternative spellings by frequency from
    largest to smallest. If the word is so badly mispelled that no viable
    alternatives were found, report that word was not found.
    Return the alternative spelling with the highest frequency
    """
    print "Welcome"
    print "This program will tell you whether the word " \
          "you've entered is in our dictionary."
    Oxford = dictionary("WordCount.txt")
    entry = errorCheck()
    
    while (entry != "quit"):       
        if (entry in Oxford) == True:
            print "Entry found."
            entry = errorCheck()
        else:
            OxfordAlt = {}
            
            delete(entry, Oxford, OxfordAlt)
            transpose(entry, Oxford, OxfordAlt)
            sub(entry, Oxford, OxfordAlt)
            insert(entry, Oxford, OxfordAlt)

            sorted(OxfordAlt.values())

            if (OxfordAlt == {}) == True:
                print "No matches found."
                entry = errorCheck()
            else:
                first = OxfordAlt.popitem()
                print "Did you mean: ", first[0],"?"
                entry = errorCheck()

    print "Thank you for using Adjoa's word correction program."

        
main()
