from datetime import datetime


class PlayoffGame:
    def __init__(
        self,
        winner: str,
        loser: str,
        score_winner: int,
        score_loser: int,
        date: datetime,
        game_number: int,
    ):
        self.winner = winner
        self.loser = loser

        self.score_winner = score_winner
        self.score_loser = score_loser

        self.date = date
        self.game_number = game_number
