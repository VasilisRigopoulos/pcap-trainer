class TrainerError(Exception):
    pass

class BadAnswer(TrainerError):
    pass

class GameOver(TrainerError):
    pass

class OutOfRange(TrainerError):
    def __init__(self, value, low, high):
        super().__init__(f"{value} is outside of valid answer range [{low},{high}]")

        self.value = value
        self.low = low
        self.high = high
