from typing import List

from models.TeamPlayoffYear import TeamPlayoffYear

def teams_that_played_the_most_elimination_games(playoff_resume: List[TeamPlayoffYear]):

    # Sort all the teams with the most elimination games
    a = {}
    for team_seasons in playoff_resume:
        a[
            f"{team_seasons.year} {team_seasons.team}"
        ] = team_seasons.get_quantity_of_elimination_games()
    teams_with_most_elimination_games = sorted(
        a.items(), key=lambda x: x[1], reverse=True
    )
    return teams_with_most_elimination_games


def champs_that_faced_most_elimination_games(playoff_resume: List[TeamPlayoffYear]):
    # Sort all the champs and how many elimination games they won
    a = {}
    for team_seasons in playoff_resume:
        a[
            f"{team_seasons.year} {team_seasons.team}"
        ] = team_seasons.get_quantity_of_elimination_games_by_champ()

    champs_with_most_elimination_games = sorted(
        a.items(), key=lambda x: x[1], reverse=True
    )

    def filter_not_champs(item):
        return item[1] is not False

    champs_with_most_elimination_games = list(
        filter(filter_not_champs, champs_with_most_elimination_games)
    )
    return champs_with_most_elimination_games


def teams_that_won_the_most_elimination_games(playoff_resume: List[TeamPlayoffYear]):
    # sort the teams that won most elimination games
    a = {}
    for team_seasons in playoff_resume:
        a[
            f"{team_seasons.year} {team_seasons.team}"
        ] = team_seasons.get_quantity_of_won_elimination_games()
    teams_that_won_most_elimination_games = sorted(
        a.items(), key=lambda x: x[1], reverse=True
    )
    return teams_that_won_most_elimination_games
