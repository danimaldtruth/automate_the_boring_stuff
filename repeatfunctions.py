def repeating(input, num_repeats=15):
    return input * num_repeats
lyrics1 = "I" + repeating(" really", 5) + " like DELICIOUS PIE AND ICE CREAM!!!\n"
verselyrics = repeating(lyrics1)
print(verselyrics)
choruslyrics = repeating("\nIt's so tasty, it's so sweet. I love to eat it after dinner.", 3) + "\nI'm so cranky when I don't get sugar AHHHHH!\n"
print(choruslyrics)
print(verselyrics)
print(choruslyrics)
print(verselyrics)
print("OK, I'm tired, time to take a nap.") 



#A demonstration of repeat functions complete with some goofiness.
