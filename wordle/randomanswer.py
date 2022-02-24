from wordle.dictionary import jumbled_words
from datetime import datetime as dt
import math

UNIX_reference = 1645678800

def random_answer(daily: bool = True):
    """Picks a random answer every day."""
    if daily == True:
        UNIX = dt.now().timestamp()
        iteration = int(math.floor((UNIX - UNIX_reference)/86400))
        return jumbled_words[iteration]