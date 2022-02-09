# Wordle

View on [GitHub](https://github.com/preritdas/wordle) and [PyPI](https://pypi.org/project/wordle-python/).

Wordle is super fun and popular game. Unfortunately, it's a little nonstandard, but the logic behind it is quite simple which is why it's now a Python library.

```python
import wordle

game = wordle.Wordle(word = 'HELLO', realWords = False)
game.run()
```

Instantiate a `game` object using `game = wordle.Wordle()`. The two positional requirements of the `Wordle` class are `word` and `realWords`. `word` is the answer to the game. It must be a real, five-letter word. If it isn't, the package will raise an error and you'll have to change your instantiation to reflect a real word. `realWords` is a boolean. If it's `True`, the package will check user guesses against a comprehensive inbuilt database of thousands of five-letter words. If it's `False`, any guess (real or not) will be accepted. 

In the game of Wordle, part of the challenge is that guesses must be real words. This prevents users from guessing `"aeiou"` as their first attempt, for example. That's why you must tell the `game` object whether it should check for real words or not.