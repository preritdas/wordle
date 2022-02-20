from wordle import dictionary

class Wordle:
    """Main Wordle game taking arguments of the answer and whether to check against the dictionary."""
    def __init__(self, word: str, real_words: bool):
        self.word = word.upper()
        self.real_words = real_words

    def run(self):
        """Run the game. Depends on bool real_words from instantiation."""
        if self.real_words == True:
            # For duplicate checking
            self.word_dup = list(self.word)

            if len(self.word) != 5 or self.word.lower() not in dictionary.words:
                raise Exception("The answer has to be a five-letter real word.")

            for i in range(6):  # 6 attempts
                # User attempt
                guess = str(input(f"Attempt {i + 1} >>> ")).upper()

                # Cheating checks
                while (
                    guess.lower() not in dictionary.words
                    or " " in guess
                    or len(guess) > len(self.word)
                ):
                    if " " in guess:
                        print(
                            "You can't have multiple words in your guess. Please run again."
                        )
                    elif len(guess) > len(self.word):
                        print(
                            f"You can't guess a word with more than {len(list(self.word))} letters. Please run again."
                        )
                    elif guess.lower() not in dictionary.words:
                        print("That's not a real word. Try again.")
                    guess = str(input(f"Attempt {i + 1} >>> ")).upper()

                # Response
                response = []
                for j in range(len(guess)):
                    if guess[j] in self.word_dup and guess[j] == self.word[j]:
                        response.append(f"*{guess[j]}*   ")
                        self.word_dup.remove(guess[j]) # Duplicates
                    elif guess[j] in self.word_dup and guess[j] != self.word[j]:
                        response.append(guess[j] + "   ")
                        self.word_dup.remove(guess[j]) # Duplicates
                    elif guess[j] not in self.word_dup:
                        response.append(guess[j].lower() + "   ")

                responseString = ""
                for letter in response:
                    responseString += letter

                print(responseString)

                if guess == self.word:
                    print(f"Congratulations, you passed the wordle in {i + 1} tries.")
                    quit()
        elif self.real_words == False:
            if len(self.word) != 5:
                raise Exception("The answer has to be a five-letter word.")

            for i in range(6):  # 6 attempts
                # User attempt
                guess = str(input(f"Attempt {i + 1} >>> ")).upper()

                # Cheating checks
                while " " in guess or len(guess) > len(self.word):
                    if " " in guess:
                        print(
                            "You can't have multiple words in your guess. Please run again."
                        )
                    elif len(guess) > len(self.word):
                        print(
                            f"You can't guess a word with more than {len(list(self.word))} letters. Please run again."
                        )
                    guess = str(input(f"Attempt {i + 1} >>> ")).upper()

                # Response
                response = []
                for j in range(len(guess)):
                    if guess[j] in self.word and guess[j] == self.word[j]:
                        response.append(f"*{guess[j]}*   ")
                    elif guess[j] in self.word and guess[j] != self.word[j]:
                        response.append(guess[j] + "   ")
                    elif guess[j] not in self.word:
                        response.append(guess[j].lower() + "   ")

                responseString = ""
                for letter in response:
                    responseString += letter

                print(responseString)

                if guess == self.word:
                    print(f"Congratulations, you passed the wordle in {i + 1} tries.")
                    quit()
            print("You failed.")