import random
from hangman_words import word_list
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

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
print(logo)
a=random.choice(word_list)



c=[]

for j in a:
    c.append("_")
h=c.copy()
print(h)

end_of_game=False
lives=6
while not end_of_game:

    b=input("Enter the letter:").lower()

    for i in range(len(a)):
        letter=a[i]
        if(a[i]==b):
            h[i]=letter
    if b not in a:
        print(f"You guessed {b}, that's not in the word. You lose a life.")
        lives=lives-1
        if(lives==0):
            end_of_game=True
            print("You lose!")
    print(h)
    if "_" not in h:
        end_of_game == True
        print("You win")
    
   
    print(stages[lives])
    




