import random #imports the random libary

guesses_taken = 0 #assign 0 to guesses_taken variable

print('Hello! What is your name?') #prints out "Hello! What is your name?"
myName = input() #asks for myNames input value

number = random.randint(1, 20) #return with a random value between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') #prints out "Well" and the myNames value and "I am thinking of a number between 1 and 20."

while guesses_taken < 6: #loop as long as the guesses_taken variable smaller then 6
    print('Take a guess.') #prints out "Take a guess"
    guess = input() #asks for the guess input value
    guess = int(guess) #convert guess to string

    guesses_taken += 1 #guesses taken will be one more with every loop

    if guess < number: #if guess is greater than number
        print('Your guess is too low.') #prints out "Your guess is too low"

    if guess > number: #if guess is smaller than number 
        print('Your guess is too high.') #prints out "Your guess is too high"

    if guess == number: #if guess is equal to number
        break #breaks from the while loop

if guess == number: #if guess is equal to number
    guesses_taken = str(guesses_taken) #convert guess to a string
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!') #print out "Good job, " adds myName "! You guessed my number in " adds guesses_taken " guesses!"

if guess != number: #guess value isn't the number
    number = str(number) #convert the number to a string
    print('Nope. The number I was thinking of was ' + number) #print out "Nope. The number I was thinking of was " adds number
