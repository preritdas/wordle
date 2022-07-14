from .dictionary import jumbled_words
from datetime import datetime as dt
import math

cdef long UNIX_reference = 1645678800
cdef float UNIX
cdef int iteration

cpdef str random_answer(bint daily):
    """Picks a random answer every day."""
    if daily == True:
        UNIX = dt.now().timestamp()
        iteration = math.floor((UNIX - UNIX_reference)/86400)
        return jumbled_words[iteration]