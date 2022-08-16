'''
################################################################
################   Author  : MD. KAMRUL ISLAM   ################
################   Date    : 17th August 2022   ################
################   Project : Hangman            ################
################################################################
'''
import hangman_arts as ha
import hangman_words as hw
import random

print(ha.logo)

selectedWord = random.choice(hw.word_list)

print(f"The selected word is: {selectedWord}")

wordLen = len(selectedWord)
lives = 6
temp = ["_"] * wordLen
alreadyGussed = []
while "_" in temp:
    guess = input("Guess a letter : ").lower()

    if guess in alreadyGussed:
      print("You have already guessed the letter. Try a differnt letter!")
    
    alreadyGussed.append(guess)
      
    for letter in range(0, wordLen):
        if(guess == selectedWord[letter]):
            temp[letter] = guess
            
    print(f"{' '.join(temp)}")
    
    if guess not in selectedWord:
        print("The letter you chose is not in the word! Try a differnt letter.")
        lives -= 1
        if(lives == 0):
            print(ha.stages[lives])
            print("You have lost the game!\nTry again!")
            break
    print(ha.stages[lives])
    
if not "_" in temp:
    print("You have won the game!")