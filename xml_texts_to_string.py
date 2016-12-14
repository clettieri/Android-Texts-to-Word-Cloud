"""
Android Text Messages to Word Cloud

1) Get your text message history in XML format.  Use the free App called
"SMS Backup & Restore" from the Google Play Store.  Back up your text
messages to a local file and transfer that to your PC.  Please note
I am not affliated with this app at all, I just made this script to work
with the XML format it produces.

2) Put this script in the same location as your XML file.  Specify the filename
of your XML file here, in the global variable FILENAME.

3) Call the function output_texts_to_file with the string of the phone number you
want the text messages with and an optional file name of the text file.  The phone
number should be a 10 digit string ("1234567890")

4) Open the text file with your output, copy the text and paste it into a word
cloud maker online.  I used www.wordclouds.com
"""
import xml.etree.ElementTree
import re
from collections import Counter


FILENAME = "sms.xml"


def get_messages_as_clean_string(phone_number):
    '''(string) -> string
    
    Uses global FILENAME and PHONE_NUMBER to parse
    the xml file and get all messages between your number and the
    PHONE_NUMBER variable.  Will remove any punctuation and make all
    letters lower case for easier counting.
    '''
    try:
        assert type(phone_number) == type("")
    except AssertionError:
        print "Phone number must be string format"
        
    text_string = ''
    
    e = xml.etree.ElementTree.parse(FILENAME).getroot()
    
    for atype in e.findall('sms'):
        if atype.get('address') == phone_number:
            text_string += " " + atype.get('body')
            
    #Remove punctuation - Regex
    clean_text = re.sub('\W+',' ', text_string)
    clean_text = clean_text.lower()
    return clean_text
    
def write_to_txt(string, new_file_name):
    '''(string, string) -> writes string to file
    
    Will write a given string to a file with the
    given filename.
    '''
    text_file = open(new_file_name+".txt", "w")
    text_file.write(string)
    text_file.close()

def print_word_counts(string):
    '''(string) -> outputs word counts

    Will print the counts for each word found in the string.
    '''
    list_of_words = string.split(" ")
    count = Counter(list_of_words)
    print count
        
def output_texts_to_file(phone_number, file_name="My Texts"):
    '''(string, optional string) -> will write a file
    
    This will run the entire script essentially.  Takes phone number
    you want the message history with, and will write the texts
    as a clean string to a file.
    '''
    write_to_txt(get_messages_as_clean_string(phone_number), file_name)

""" MAIN """
#Example Call
output_texts_to_file('1234567890', 'My Texts with 1234567890')