from datetime import datetime


class PlayoffSeries:
    # https://www.basketball-reference.com/playoffs/NBA_2019.html
    # https://www.basketball-reference.com/playoffs/2019-nba-eastern-conference-first-round-pistons-vs-bucks.html
    # get the div class="game_summaries"
    #     for fiv in it
    #         get table
    #             tr winner
    #                 td regex name
    #                 td class righ (points)
    #             tr loser
    #                 td regex name
    #                 td class righ (points)

    def __init__(self, series_name, winner, loser, games=[]):
        self.series_name = series_name
        self.winner = winner
        self.loser = loser
        self.games = games


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
