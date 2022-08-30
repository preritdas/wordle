![tests](https://github.com/preritdas/wordle/actions/workflows/pytest.yml/badge.svg)
![pypi deployment](https://github.com/preritdas/wordle/actions/workflows/python-publish.yml/badge.svg)
[![PyPI version](https://badge.fury.io/py/wordle-python.svg)](https://badge.fury.io/py/wordle-python)

# Wordle

View on [GitHub](https://github.com/preritdas/wordle) and [PyPI](https://pypi.org/project/wordle-python/).

----
## Updates

### Version 2.2.0: Individual Guessing!

This package can now be properly used to power the backend of a Wordle game. Initially, the `.run()` method had to be used to play the game. It would open a console, request guesses as inputs, and print out responses. That's not a viable solution to power the backend of a package user's application or game. 

See a demo!

[![asciicast](https://asciinema.org/a/U0PSdB4lw87B7CFddB9cQb7ju.svg)](https://asciinema.org/a/U0PSdB4lw87B7CFddB9cQb7ju)

The `Wordle` class has two new submethods: `.send_guess()` and `.reset_guesses()`. 

Instantiate an object with the answer and game options (dictionary, etc.). Then, send individual guesses and the method will return a response.

```python
import wordle

# Instantiate a game object
game = wordle.Wordle(word = 'grape', real_words = True)

# Send your object a guess
response = game.send_guess('adieu')
# response = a d i e u

# Send an invalid guess
response = game.send_guess('yabadabadoo')
# response = "You can't guess a word with more than 5 letters."
# Note: invalid guesses don't count towards the guess log.

# Send a 7th guess (only 6 allowed with log_guess = True)
response = game.send_guess('seven')
# response = "Out of guesses."
```

More information on how to use this new feature is below.

### Version 2.0.0

A new function to get a random answer based on the day. You can deploy this Wordle and have it give you a random answer automatically every day! Instead of manually changing the answer, the program (can) automatically change its answer every day.

Use `wordle.random_answer(daily = True)` (Update: `daily` argument is now optional with default value `True`). You can instantiate a game using this parameter:

```python
import wordle

wordle.Wordle(word = wordle.random_answer(), real_words = True).run()
```

Or, you can access the random word directly in instantiation (**new and preferred**):

```python
import wordle

wordle.Wordle(random_daily = True, real_words = True).run()
```

All arguments are now optional. By default, `word = 'hello'`, `real_words = True`, and `random_daily = False`. If you set `random_daily = True`, `word` is overwritten with a daily word. If you provide a `word` _and_ set `random_daily = True`, the `word` you chose will be overwritten. So, try to use _either_ `word` _or_ `random_daily`. 

If this game is run in the same day, the answer `word` will be the same. Tomorrow, however, it will change. I did this using UNIX. The dictionary is shuffled and an iterator is calculated using multiples of 86400 (seconds in a day). The program then gets a word from the randomized `dictionary.jumbled_words` list based on the iterator. 

The behavior is that the program will have the same answer intraday but will automatically run with a new unique answer the next day. By standardizing this using UNIX time I avoided the need for a central database of "used" words. To reset it all, `dictionary.jumbled_words` has to be recalculated using `random.sample(dictionary.words, len(dictionary.words))`. 

This is a much better way to deploy to the cloud as the game is **completely self-sufficient**!

### Version 1.9.0

Completely redesigned the `Wordle` class as it was totally inefficient. It used to take the parameter `self.real_words`, given on object instantiation, and then run in two separate ways. The logic worked in this way:

```python
class Wordle:
    def run(self):
        if self.real_words == True:
            run_with_logic_that_words_must_be_checked()
        elif self.real_words == False:
            run_with_logic_that_words_must_not_be_checked()
```

This was very inefficient because fixes and upgrades had to be made to both aspects of the `Wordle.run()` function. Initially it was necessary because the logic for checking against the dictionary was unique, but now, I'm hosting a dictionary of thousands of five-letter words [here](https://wordle.preritdas.com/words.txt). So, I rewrote the class to have this structure:

```python
class Wordle:
    def run(self):
        run_with_interspersed_realWords_conditions()
```

Which works much better. I introduced a `failed_dictionary_test` boolean which resets every time a new attempt is entered but allows the program to alert non-real words only if `self.real_words == True AND guess.lower() not in dictionary.words`. It's clean, faster, and more efficient!

### Version 1.8.0

An issue was brought up on GitHub. If the answer was `"games"` for example, and you guessed `"trees"`, the program would capitalize _both_ of the letters `"e"` in your guess. It would behave in this way:

```
# Answer = 'games'

Attempt 1 >>> trees
t   r   E   E   *S*
```

I corrected the error with a functional `list(self.word)` that resets itself every attempt. Now the program behaves properly, in the way we'd expect:

```
# Answer = 'games'

Attempt 1 >>> trees
t   r   E   e   *S*
```
----
## Documentation

Wordle is super fun and popular game. Unfortunately, it's new and nonstandard, meaning the backend technology is not prevalent and recreatable online. There are a couple web-based customizable Wordle tools, which work very well, but they're front-end only (you can't clone, copy, modify, or edit the back-end to deploy it to a website or run your own game). That said, the logic behind Wordle is quite simple which is why it's now a Python library, enabling all the functions of an open-sourced game.

Currently, the module is logic based and runs in a shell (as of v2.2.0, the new individual guess methods enable Wordle to be deployed practically anywhere). I'd love it if this project was forked into a GUI-based application, possibly using `pygame`, allowing users to take this a step further and deploy a version with a user-interface. As it stands, the best way I can think of to deploy Wordle to the web is by using an embedded Python console like [Trinket](https://trinket.io/features/python3) and putting it in 'run-only' mode so users can't see the source code (where the answer is). See an example of this in real deployment [here](https://wordle.preritdas.com).

In any case, usage of this module is wickedly simple.

```python
import wordle

game = wordle.Wordle(word = 'HELLO', real_words = False)
game.run()

# Or even more simply:
wordle.Wordle(word = 'hello', real_words = True).run() # runs in one line. 
```

Instantiate a `game` object using `game = wordle.Wordle()`. The two positional requirements of the `Wordle` class are `word` and `real_words`. `word` is the answer to the game. If the object is instantiated with `real_words = True`, `word` must be a real, five-letter word or an exception will be raised, and you'll have to change your instantiation to reflect a real word. `real_words` is a boolean. If it's `True`, the package will check user's (in-game) guesses against a comprehensive inbuilt database of thousands of five-letter words. If it's `False`, any guess (real or not) will be accepted. In summary, `real_words` applies both to the answer in the code's instantiation _and_ in the user's in-game guesses.

In the game of Wordle, part of the challenge is that guesses must be real words. This prevents users from guessing `"aeiou"` as their first attempt, for example. That's it's relevant and important for you to tell the `game` object whether it should check for real words or not.

_Note_: In version 1.5.10, the issue disallowing a lower-case `word` has been patched. `word = 'hello'` and `word = 'HELLO'` are both acceptable in the game initialization.

To view the docstring (explainer) of a particular function, use `wordle.Wordle.run.__doc__` where `run` can be repalced with any other function. For example, running `print(wordle.Wordle.run.__doc__)` will return: `Run the game. Depends on bool real_words from instantiation.` Depending on your IDE, hovering over a function in the editor will show the function's docstring (works in VS Code).

```python
import wordle

if __name__ == "__main__":
    print(wordle.Wordle.__doc__)
    print(wordle.Wordle.run.__doc__)
```

### Individual Guessing

This new feature was introduced in the Version 2.2.0 update at the top of the read-me. Here's some more usage information.

Here's some example usage. 

Instantiate an object with the answer and game options (dictionary, etc.). Then, send individual guesses and the method will return a response.

```python
import wordle

# Instantiate a game object
game = wordle.Wordle(word = 'grape', real_words = True)

# Send your object a guess
response = game.send_guess('adieu')
# response = a d i e u

# Send an invalid guess
response = game.send_guess('yabadabadoo')
# response = "You can't guess a word with more than 5 letters."
# Note: invalid guesses don't count towards the guess log.

# Send a 7th guess (only 6 allowed with log_guess = True)
response = game.send_guess('seven')
# response = "Out of guesses."
```

The `.send_guess()` method has two parameters, one of which is optional. `guess` is a string and is necessary. `log_guess` is a boolean and is `True` by default. Log guessing is simply the program's way of tracking how many times a _valid_ guess has been sent to the object. It will only allow 6 valid guesses to be sent to it before it starts returning `"Out of guesses."` automatically. To send a guess and return a response without adding to the guesses log, use `log_guess = False`.