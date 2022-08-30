import wordle


def test_wordle():
    """
    Test all cases of guess sending - invalid word, valid word, too many letters,
    upper case included, correct answer, multiple words, etc.
    """
    game = wordle.Wordle(word = "hello")
    wordle.send_guess("travis")
    wordle.send_guess("trees")
    wordle.send_guess("asfasdfasdf")
    wordle.send_guess("jAKJasdD")
    wordle.send_guess("two words")
    wordle.send_guess("hello")
    
    game = wordle.Wordle(word = "hello")
    wordle.send_guess("hello")
    
