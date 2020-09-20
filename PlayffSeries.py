from constants import WINS_NECESSARY_BY_SERIES_LENGTH, NBA_CHAMPS
from datetime import datetime


class PlayoffSeries:
    def __init__(self, series_name, winner, loser, games=[], best_of_series=7):
        self.series_name = series_name
        self.winner = winner
        self.loser = loser
        self.games = games
        # series that arent over were breaking this
        self.best_of_series = (
            best_of_series if self.playoff_year() != datetime.now().year else 7
        )

    def winner_wins(self):
        from seriesGetter import get_teams_and_total_wins

        return get_teams_and_total_wins(self.games).get(self.winner)

    def loser_wins(self):
        from seriesGetter import get_teams_and_total_wins

        return get_teams_and_total_wins(self.games).get(self.loser)

    def playoff_year(self):
        return self.games[-1].date.year

    def winner_is_champ(self):
        # True if the winner of the series get to be the nba champ
        # If some the last playoff game of a series ran in a different year
        # than the championship this will bug
        return True if self.winner is NBA_CHAMPS.get(self.playoff_year()) else False

    def elimination_games(self):
        # WINS_NECESSARY_BY_SERIES_LENGTH
        winner_elimination_games_so_far = 0
        loser_elimination_games_so_far = 0

        winner_games_won_so_far = 0
        loser_games_won_so_far = 0
        for game in self.games:
            (
                winner_elimination_games_so_far,
                loser_elimination_games_so_far,
            ) = process_elimination_game(
                self.best_of_series,
                winner_games_won_so_far,
                loser_games_won_so_far,
                winner_elimination_games_so_far,
                loser_elimination_games_so_far,
            )

            if game.winner == self.winner:
                winner_games_won_so_far = winner_games_won_so_far + 1
            if game.winner == self.loser:
                loser_games_won_so_far = loser_games_won_so_far + 1

        return winner_elimination_games_so_far, loser_elimination_games_so_far

    def winner_elimination_games(self):
        return self.elimination_games()[0]

    def loser_elimination_games(self):
        return self.elimination_games()[1]

    def team_elimination_games(self, team_name):
        if team_name != self.winner and team_name != self.loser:
            return
        return (
            self.loser_elimination_games()
            if team_name is self.loser
            else self.winner_elimination_games()
        )

    def ongoing_series(self):
        return (
            True
            if int(WINS_NECESSARY_BY_SERIES_LENGTH.get(str(self.best_of_series)))
            > self.winner_wins()
            else False
        )

    def __sizeof__(self):
        return self.playoff_year()

    def __gt__(self, other):
        return self.__sizeof__() > other.__sizeof__()


def process_elimination_game(
    series_length,
    winner_games_won_so_far,
    loser_games_won_so_far,
    winner_elimination_games_so_far,
    loser_elimination_games_so_far,
):
    if (
        winner_games_won_so_far
        is WINS_NECESSARY_BY_SERIES_LENGTH.get(str(series_length)) - 1
    ):
        loser_elimination_games_so_far = loser_elimination_games_so_far + 1
    if (
        loser_games_won_so_far
        is WINS_NECESSARY_BY_SERIES_LENGTH.get(str(series_length)) - 1
    ):
        winner_elimination_games_so_far = winner_elimination_games_so_far + 1

    return winner_elimination_games_so_far, loser_elimination_games_so_far
