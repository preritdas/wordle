from wordle import dictionary, randomanswer


class Wordle:
    """Main Wordle game taking optional arguments of the answer and whether to check against the dictionary.
        random_daily changes answer every day (see github/preritdas/wordle)."""
    def __init__(
        self, word: str = 'hello', 
        enforce_len: bool = True, 
        real_words: bool = True, 
        random_daily: bool = False
    ):
        self.word = word.upper()
        self.real_words = real_words
        self.enforce_len = enforce_len
        if random_daily == True:
            self.word = randomanswer.random_answer(daily=True).upper()

        # Individual guesses
        self.individual_guesses = []

    def run(self):
        """Run the game. Depends on bool real_words from instantiation."""

        # Answer viability test
        if self.enforce_len and len(self.word) != 5:
            raise Exception("The answer has to be a five-letter word.")
        if self.real_words == True and self.word.lower() not in dictionary.words:
            raise Exception(
                "The answer has to be a real word as you indicated you want dictionary checking."
                )

        # Begin iterating for attempts (6)
        for i in range(6):  # 6 attempts
            # For duplicate checking
            self.word_dup = list(self.word)

            failed_dictionary_test = False # by default

            # User attempt
            guess = str(input(f"Attempt {i + 1} >>> ")).upper()

            # Cheating checks

            # real_words = True
            if self.real_words == True and guess.lower() not in dictionary.words:
                failed_dictionary_test = True

            while (
                failed_dictionary_test == True
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
                elif failed_dictionary_test == True: # Not a real word
                    print("That's not a real word. Try again.")
                guess = str(input(f"Attempt {i + 1} >>> ")).upper()

                # Correct failed dictionary test if real word is guessed
                if self.real_words and guess.lower() in dictionary.words:
                    failed_dictionary_test = False

            # prepare response list
            response = []
            for _ in range(len(self.word_dup)):
                response.append('')

            # first correctness check
            for j in range(len(guess)):
                if guess[j] in self.word_dup and guess[j] == self.word[j]:
                    response[j] = f"*{guess[j]}*   "
                    self.word_dup.remove(guess[j])  # Duplicates

            # next present and absent check
            for j in range(len(guess)):
                # already response skip
                if response[j] != "":
                    continue
                # it's present(yellow)
                if guess[j] in self.word_dup:
                    response[j] = guess[j] + "   "
                    self.word_dup.remove(guess[j])  # Duplicates
                # other absent
                else:
                    response[j] = guess[j].lower() + "   "

            responseString = ""
            for letter in response:
                responseString += letter

            print(responseString)

            if guess == self.word:
                if (i + 1) == 1: # Passed in one try
                    print(f"Congratulations, you passed the wordle in {i + 1} try.")
                elif (i + 1) > 1:
                    print(f"Congratulations, you passed the wordle in {i + 1} tries.")
                else:
                    raise Exception("Fatal iteration error for largest for loop.")
                quit()
        print("You failed.")
        quit()

    # Individual guesses
    def send_guess(self, guess: str, log_guess: bool = True):
        """
        Send individual guesses. Returns a tuple where item one is the \
            string response, and item two is a boolean of whether or not the \
            puzzle was solved.. 
        Follows dictionary checking if that's enabled on object instantiation.
        If a guess is invalid (too many letters, etc.) the returned response \
            is simply an error message. No guess is logged.
        Use log_guess = False to send a guess without it counting towards \
            the 6 guess total.
        """
        # For duplicate checking
        self.word_dup = list(self.word)
        failed_dictionary_test = False # by default
        guess = guess.upper() # for the logic

        # Cheating checks

        # real_words = True
        if self.real_words == True and guess.lower() not in dictionary.words:
            failed_dictionary_test = True

        if " " in guess:
            return "You can't have multiple words in your guess."
        elif self.enforce_len and len(guess) > len(self.word):
            return f"You can't guess a word with more than {len(list(self.word))} letters."
        elif failed_dictionary_test == True: # Not a real word
            return "That's not a real word."

        # Correct failed dictionary test if real word is guessed
        if self.real_words and guess.lower() in dictionary.words:
            failed_dictionary_test = False

        # prepare response list
        response = ['' for _ in range(len(guess))]

        # first correctness check
        for j in range(len(guess)):
            # out of range issue
            try:
                if guess[j] == self.word[j]:
                    response[j] = f"*{guess[j]}*   "
                    self.word_dup.remove(guess[j])
                    continue
            except IndexError:
                pass

        # next present and absent check
        for j in range(len(guess)):
            # already response skip
            if response[j] != "":
                continue
            # it's present(yellow)
            if guess[j] in self.word_dup:
                response[j] = guess[j] + "   "
                self.word_dup.remove(guess[j])  # Duplicates
            # other absent
            else:
                response[j] = guess[j].lower() + "   "

        responseString = ""
        for letter in response:
            responseString += letter

        if guess == self.word:
            guessed_correctly = True
        else:
            guessed_correctly = False

        # Guess Logging
        if log_guess:
            if len(self.individual_guesses) < 6:
                self.individual_guesses.append(guess)
            else:
                return "Out of guesses."

        # Return the response
        if guessed_correctly:
            return responseString, True
        else:
            return responseString, False

    # Reset individual guesses
    def reset_guesses(self):
        """Removes all guesses from guess logging to allow 6 more attempts."""
        self.individual_guesses = []
