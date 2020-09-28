from datetime import datetime
from random import choices as random_choices, randint
from string import ascii_uppercase, digits

from models.PlayoffSeries import PlayoffSeries
from models.PlayoffGame import PlayoffGame
from models.TeamPlayoffYear import TeamPlayoffYear


def mock_playoffGame():

    # Gera uma string com letras e numeros de tamanho 10
    winner = "".join(random_choices(ascii_uppercase + digits, k=10))
    loser = "".join(random_choices(ascii_uppercase + digits, k=10))
    score_winner = randint(100, 999)
    score_loser = randint(1, 99)
    date = datetime.now()
    game_number = randint(1, 7)
    return PlayoffGame(winner, loser, score_winner, score_loser, date, game_number)


def mock_series():
    games = []
    for i in range(1, 6):
        games.append(mock_playoffGame())

    def fix_names(game, winner, loser):
        game.winner = winner
        game.loser = loser
        return game

    # Set the name of all the teams equal for all games
    list(
        map(
            fix_names,
            games,
            [games[0].winner] * len(games),
            [games[0].loser] * len(games),
        )
    )
    # Invert the winner of the first game
    list(map(fix_names, games, [games[0].loser], [games[0].winner]))

    series_name = "".join(random_choices(ascii_uppercase + digits, k=10))
    return PlayoffSeries(
        series_name,
        winner=games[-1].winner,
        loser=games[-1].loser,
        games=games,
        best_of_series=7,
    )


def mock_team_year_resume():
    series = mock_series()
    return TeamPlayoffYear(series.winner, series.playoff_year(), [series])
