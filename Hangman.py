import random
from collections import Counter

someWords='apple mango strawberry orange apple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'
# this split function splits the above string into separate words and stores them in a list someWords
someWords=someWords.split(' ')
# print(someWords)
word=random.choice(someWords)
print(word)
# word gets any word from list someWords randomly
if __name__=='__main__':
# if True:
    print('Guess the word! HINT: word is a name of a fruit')
    for i in word:
        print(i)
        print("_",end=" ")
    print()

    playing=True
    letterGuessed=""
    chances=len(word)+2
    correct=0
    flag=0
    try:
        while(chances!=0)and flag==0:
            print()
            chances-=1

            try:
                guess=str(input("Enter a letter to guess: "))
            except:
                print("Enter only a letter!")
                continue
            if not guess.isalpha():
                print("Enter only a letter!")
                continue
            elif len(guess)>1:
                print("Enter only a SINGLE LETTER")
                continue
            elif guess in letterGuessed:
                print("You have already guessed that letter")
                continue
                
            if guess in word:
                k=word.count(guess)
                for _ in range(k):
                    letterGuessed+=guess
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed)!=Counter(word)):
                    print(char, end=" ")
                    correct+=1
                elif Counter(letterGuessed)==Counter(word):
                    print( )
        if chances <=0  and (Counter(letterGuessed)!=Counter(word)):
            print()
            print("You lost! Try again")
            print("The word was {}".format(word))
    except KeyboardInterrupt:
        print()
        print("Bye! Try again")
        exit()
