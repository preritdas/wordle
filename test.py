import wordle

game = wordle.Wordle(word = 'grape', real_words = True)

response = game.send_guess(guess = 'adieu')
print(response)

response = game.send_guess(guess = 'adieu')
print(response)

response = game.send_guess(guess = 'adieu')
print(response)

response = game.send_guess(guess = 'adieu')
print(response)

response = game.send_guess(guess = 'adieu')
print(response)

response = game.send_guess(guess = 'adieu')
print(response)

response = game.send_guess(guess = 'adieu')
print(response)

# as there are seven sent attempts, the final one returns...
#... "Out of guesses." as expected.