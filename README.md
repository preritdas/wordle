# Wordle

View on [GitHub](https://github.com/preritdas/wordle) and [PyPI](https://pypi.org/project/wordle-python/).

Wordle is super fun and popular game. Unfortunately, it's new and nonstandard, meaning the backend technology is not prevalent and recreatable online. There are a couple web-based customizable Wordle tools, which work very well, but they're front-end only (you can't clone, copy, modify, or edit the back-end to deploy it to a website or run your own game). That said, the logic behind Wordle is quite simple which is why it's now a Python library, enabling all the functions of an open-sourced game.

Currently, the module is logic based and runs in a shell. I'd love it if this project was forked into a GUI-based application, possibly using `pygame`, allowing users to take this a step further and deploy a version with a user-interface. As it stands, the best way I can think of to deploy Wordle to the web is by using an embedded Python console like [Trinket](https://trinket.io/features/python3) and putting it in 'run-only' mode so users can't see the source code (where the answer is). See an example of this in real deployment [here](https://wordle.preritdas.com).

In any case, usage of this module is wickedly simple.

```python
import wordle

game = wordle.Wordle(word = 'HELLO', realWords = False)
game.run()

# Or even more simply:
wordle.Wordle(word = 'hello', realWords = True).run() # runs in one line. 
```

Instantiate a `game` object using `game = wordle.Wordle()`. The two positional requirements of the `Wordle` class are `word` and `realWords`. `word` is the answer to the game. If the object is instantiated with `realWords = True`, `word` must be a real, five-letter word or an exception will be raised, and you'll have to change your instantiation to reflect a real word. `realWords` is a boolean. If it's `True`, the package will check user's (in-game) guesses against a comprehensive inbuilt database of thousands of five-letter words. If it's `False`, any guess (real or not) will be accepted. In summary, `realWords` applies both to the answer in the code's instantiation _and_ in the user's in-game guesses.

In the game of Wordle, part of the challenge is that guesses must be real words. This prevents users from guessing `"aeiou"` as their first attempt, for example. That's it's relevant and important for you to tell the `game` object whether it should check for real words or not.

_Note_: In version 1.5.10, the issue disallowing a lower-case `word` has been patched. `word = 'hello'` and `word = 'HELLO'` are both acceptable in the game initialization.