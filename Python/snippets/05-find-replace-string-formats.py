msg='Sometimes all you can do is keep living until you feel alive'


#####----- Find something within a string
print(msg.find('you')) # use .find
# Result is "14" which is the first "you"

#####----- Replace something within a string (immuteable)
print(msg.replace('you', 'u'))
# Result is "Sometimes all u can do is keep living until u feel alive"


#####----- Create a new variable to contain the change
msg1=(msg.replace('feel', 'f33l'))
print(msg1)
# Prints: "Sometimes all you can do is keep living until you f33l alive"


#####----- Check a parameter and return a variable
print('dog' not in msg) 
# "Not in" returns true becuase "dog" is not in the message
print('feelings' in msg)
# "In" returns false because "feelings" is not in the message


#####----- 
name='DONNA'
color= 'RED'
# You can format as the line below, but it isn't the easiest to read
msg2 = '[' + name + '] loves the colour ' + color.lower() + '!'
# f is for formatting, and the following is more readable than the previousline but they do the same thing.
msg3 = f'[{name.title()}] loves the colour {color.lower()}!'
print(msg2, msg3)