
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3

while guess != secret_word and guess_count < guess_limit:
    guess = input(" what is  secret word? \n")
    if guess == secret_word:
        print(" Good job!! you guessed it correctly ;) \n")
        break
    print("Try again")
    guess_count += 1
else:
    print("Sorry, you run out of tries")