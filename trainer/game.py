import trainer
from trainer.questions import make_question
from trainer.questions import LOW, HIGH
from trainer.errors import BadAnswer, OutOfRange, GameOver, TrainerError

import platform
from rich.console import Console

console = Console()

def read_answer(text, low =LOW, high = HIGH):
    try:
        text = int(text)

        if not(low <= text <= high):
            raise OutOfRange(text, low, high)

        return text
        
    except ValueError:
        raise BadAnswer(f"\"{text}\" is not an Interger.")



def play(rounds: int = 5, max_mistakes: int = 3):
    score = 0
    mistakes = 0
    for i in range(1, rounds + 1 ):
        text, answer = make_question()

        print(f'\n{i}. what does the following output? {text} =', end=" ")

        
        try:
            guess = read_answer(input())

        except BadAnswer as e:
            print('It doesnt count:', e)
            mistakes += 1 

        except OutOfRange as e:
            print(e)
            mistakes += 1 

        else:

            if guess == answer:
                score += 1 
                console.print("[green] Correct! [/]")

            else:
                mistakes += 1
                console.print(f"[red]Wrong, Correct answer is {answer} [/]")
        finally:
            console.print(f" \n Current Stats, [green]Score:{score}[/], [red]Mistakes:{mistakes}[/]")

        if mistakes >= max_mistakes:
            raise GameOver(mistakes)

    return score
