class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives
        
    def guess(self, n):
        guessed = False
        while not guessed:
            while self.lives > 0:
                if n != self.number:
                    self.lives -= 1
                    return False
                else:
                    guessed = True
                    return True
            raise ValueError('Expect error: "Omae wa mo shindeiru"')
