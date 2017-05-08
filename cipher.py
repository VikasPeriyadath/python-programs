
text = raw_input("Enter Text : ")
def getTranslatedMessage():
     translated = ''

     for char in text:
         if char.isalpha():
             num = ord(char)
             num += -3

             if char.isupper():
                 if num < ord('A'):
                     num += 26
             elif char.islower():
                 if num < ord('a'):
                     num += 26                

             translated += chr(num)
         else:
             translated += char
     print "Your translated Text is : ",translated


getTranslatedMessage()