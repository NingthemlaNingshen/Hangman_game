import random
from image_for_hangman import hangman_image 
from secret_word_for_hangman import secret_words

def get_the_random_word():
    secret_word=random.choice(secret_words).lower() ##random word will be chossen and convert it into lower case
    return secret_word

def start_the_game():
    print("Welcome to hangman Game!")
    Gamer_name=input("enter your name: ")
    if Gamer_name.isalpha()==True:
        print(Gamer_name,"Welcome to the world of Hangman game! .\n Hope you will enjoy the game and learn new words at same time.")
    else:
        print("enter your name using letters only!")
        Gamer_name=input("enter a valid name using letters only: ")

def replay():
    print("Do you want to play again? Yes/No")
    user_choice=input("enter your choice: ")
    if user_choice=="Yes":
        let_the_Game_begin()
    else:
        print("See you next time")

def let_the_Game_begin():
    start_the_game()
    word=get_the_random_word()
    guessed_letter=[]    ##storing the right guesses
    guessed_word=[]      ##storing the wrong guesses
    failure_count=0
    tries=6
    print("The word contains",len(word),"letters.")
    while tries>0:
        word_completion=""
        for letter in word:
            if letter in guessed_letter:
                word_completion+= letter
            else:
                word_completion+= "_"
        if  word_completion==word:
            print(word_completion.capitalize())
            print("Congrats!! You guess the word correctly!You win")
            break
        print("Guess the word",word_completion)
        print("You have",tries,"chances left")
        guess=input("Guess a letter in  the word  or enter the full word:-").lower()
        if len(guess)==1 and guess.isalpha():
            if guess in guessed_letter:
                print("you have already guess the letter before.")
            elif guess not in word:
                print("Sorry! that letter is not in the word.")
                failure_count = failure_count+1
                tries = tries-1
                guessed_word.append(guess)
                print(hangman_image[failure_count])
            elif guess in word:
                print("Good job",guess,"is in the word!")
                guessed_letter.append(guess)
        elif len(guess)==len(word):
            if guess in guessed_word:
                    print("You already guessed the word",guess)
            elif guess!=word:
                print(guess,"is not in the word.")
                failure_count = failure_count +1
                tries = tries-1
                guessed_word.append(guess)
                print(hangman_image[failure_count])
        else:
            print("The length of your guess is not the same as the length of the correct word.")
            failure_count = failure_count +1
            tries = tries-1
            guessed_word.append(guess)
            print(hangman_image[failure_count])
    if tries==0:
        print("Sorry!.You ran out of tries.The word was",word.capitalize())
    replay()
let_the_Game_begin()
        


    