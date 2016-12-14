# Android-Texts-to-Word-Cloud
Convert text messages from an XML file to a clean string for use in an online word cloud maker


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
