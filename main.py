import trainer
from trainer.errors import * #OutOfRange, TrainerError, BadAnswer
from trainer.questions import make_question
from trainer.game import play

import random

import platform
from rich.console import Console

# import sys
# print(sys.path[0])

# print(OutOfRange(5,0,3).args)

console = Console()

rounds = 5

if __name__ == "__main__":
    try:
        score = play(rounds= rounds, max_mistakes= 3)
    except GameOver:
        console.print("\n[bold] Game Over, Buddy you're not passing💀")
    except KeyboardInterrupt:
        console.print('[bold]Interrupted by User')
    else:
        print(f"[bold]Finished Questionare, Final score: {score}/{rounds}, or {(score/rounds ) * 100}%")
    finally:
        print('Goodbye world.')