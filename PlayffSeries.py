from constants import WINS_NECESSARY_BY_SERIES_LENGTH, NBA_CHAMPS


class PlayoffSeries:
    def __init__(self, series_name, winner, loser, games=[], best_of_series=7):
        self.series_name = series_name
        self.winner = winner
        self.loser = loser
        self.games = games
        self.best_of_series = best_of_series

    def winner_wins(self):
        from seriesGetter import get_teams_and_total_wins

        return get_teams_and_total_wins(self.games).get(self.winner)

    def loser_wins(self):
        from seriesGetter import get_teams_and_total_wins

        return get_teams_and_total_wins(self.games).get(self.loser)

    def playoff_year(self):
        return self.games[-1].date.year

    def winner_is_champ(self):
        # If some the last playoff game of a series ran in a different year
        #than the championship this will bug
        return True if self.winner is NBA_CHAMPS.get(self.playoff_year()) else False

    def elimination_games(self):
        WINS_NECESSARY_BY_SERIES_LENGTH
        series_moment = {}
