import random
WordBank = [ 'bottle', 'good', 'tablets', 'chips', 'book', 'chocolate']
word = random.choice(WordBank)
guessedWord = ['_'] * len(word)
attempts = 10

while attempts >0:
    print('\nCurrent word: ' + ' '.join (guessedWord))
    guess = input('Guess a letter: ').lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print("Great guess!")
    else: 
        attempts -= 1
        print('Wrong Guess! Number of attempts left = ' + str(attempts))
    if "_" not in guessedWord:
        print("Congrats you have guessed the word!")
        break
if attempts == 0 and '_' in guessedWord:
        print("\nYou've ran out of attempts! The word was: " + word)

    