msg='This is all about strings and slicing in Python. Here\'s an Escaped character'

print(msg)
# Some built-in string functions for text formatting:
print(msg.upper())
print(msg.lower())
print(msg.capitalize())
print(msg.title())

# Some built-in string functinos for more information:
newmsg='Shadowfax the horse'
print(newmsg)
print(len(newmsg)) # Print the length of the string
print(newmsg.count('horse')) # (case sensitive) looks for and counts paramater - in this case the string 'horse'
print(newmsg.count('o')) #how many 'o's ? 

# Slicing strings
print(newmsg[5]) # Gives the letter at position 6 as Python is a zero-based language. 0 would be the first letter.
print(newmsg[-1]) # Gives the last letter in the string.
print(newmsg[2:]) # Give me everything after the second position. Eg, "adowfax the horse"
print(newmsg[:2]) # Give me everything up until the second position Eg, "Sh"
print(newmsg[4:10]) # Or, print a range

## Scrimba challenge:
## From 'welcome to Python 101: Strings', print:
# 'welcome to Python 101: Strings'
# 'Relyt Ot Gnir Emoclew 1'

messages='welcome to Python 101: Strings'

together = messages[18] + " " + messages[0:7] + " " + messages[-5:-1] + " " + messages[8:10] + " " + messages[13] + messages[12] + messages[2] + messages[6] + messages[-5]
print(together.title())
print(together[::-1].title())

#1 Welcome Ring To Tyler