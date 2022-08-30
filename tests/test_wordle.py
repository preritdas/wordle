import wordle


def test_wordle():
    """
    Test all cases of guess sending - invalid word, valid word, too many letters,
    upper case included, correct answer, multiple words, etc.
    """
    game = wordle.Wordle(word = "hello")
    game.send_guess("travis")
    game.send_guess("trees")
    game.send_guess("asfasdfasdf")
    game.send_guess("jAKJasdD")
    game.send_guess("two words")
    game.send_guess("hello")
    
    game = wordle.Wordle(word = "hello")
    game.send_guess("hello")
    
