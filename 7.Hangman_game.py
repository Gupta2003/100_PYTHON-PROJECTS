import random
import string

word_list = ["ashish","akshat","sudha","sanjeev"]

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/   ''')

      
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
print(stages[6])
#we select a random word from the list of words named word list  
choosen_word = random.choice(word_list)
print(choosen_word)

#here we make a empty list of spaces to denote letters 
display = []
lenght = len(choosen_word)
for i in range(0,lenght):
    display.append("_")

print(display)

# actual logic of the code 
end_of_game = False
lives = 6
while end_of_game is False:
    guessed  = input("Please enter a letter from a to z : \n").lower()
    print("You guess the letter :",guessed)
    if guessed in display:
        print("you already guessed that letter ")
    elif guessed in choosen_word:
        print("yes the letter",guessed,"is present in word")
        print("Remaining lives are :",lives)
        for i in range(0,lenght):
            if(choosen_word[i] == guessed):
                display[i] = guessed
        print(f"{' '.join(display)}")
    else:
        print("No the letter",guessed,"is not present in word")
        lives-=1
        print("Remaining lives are :",lives)
        print(stages[lives])
        if(lives == 0):
            print("OOPS! you loose the game ")
            end_of_game = True
    

    if "_" not in display:
        end_of_game = True
        print("You win.")

  


