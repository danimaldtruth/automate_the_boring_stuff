# moving from mu-editor back into py-charm professional with vim plugin
# just checking a few things with pycharm functionality here
##print('Hello World')
#print(7 + 7)
# on to the lesson and chapter 2
# booleans lesson
# testing this in console first
#spam = True
#42 == 42
#42 == 99
#2 != 3
# ok, i'm understanding pycharm a little better, let's move on to writing a script, if example
# print('Please enter your name')
# name = input()
# if name =='Danny':
#    print('Hi, Danny')
# code prints 'Hi, Danny' if Danny name is entered, nothing if anything else is entered or nothing.
# adding else
#print('Please enter your name')
#name = input()
#if name =='Danny':
#    print('Hi, Danny')
#else:
#    print('Hello, stranger')
#if and elif example, coming back to this tomorrow.
# back on jan 2nd, 2022.
#experimenting with yank yy copy paste and new line o and new line shift o in vim
#going to create a new vim file to master copy paste select after this
print('What is your name?')
name = input()
if name == 'Alice':
    print('Hello Alice.')
elif name != 'Alice':
    print("You are not Alice. I only care about Alice's age.")
    quit()
print('What is your age as an integer?')
age = int(input())
if age < 12:
    print('You are a youngin')
elif age >= 101:
    print('Unlike you, Alice is not an undead immortal vampire.')
elif age >= 100:
    print('You are not Alice, grannie.')
elif age >= 12 <= 100:
    print('Okay, you are probably an okay age to be a human.')

#okay i think this is done. next time ill write this line as a commit.