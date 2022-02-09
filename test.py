import wordle

game = wordle.Wordle(word = 'HELLO', realWords = False)
game.run()

# Or
import wordle as w
w.Wordle(word = 'hello', realWords = True).run()
