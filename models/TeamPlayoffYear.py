from datetime import datetime

from constants import NBA_CHAMPS


class TeamPlayoffYear:
    def __init__(self, team, year, series):
        self.team = team
        self.year = year
        self.series = series
        pass

    def get_quantity_of_elimination_games(self):
        return sum([series.team_elimination_games(self.team) for series in self.series])

    def team_is_champ(self):
        return True if NBA_CHAMPS.get(self.year) == self.team else False

    def get_quantity_of_elimination_games_by_champ(self):
        "get the quantity of wins by a champ team, False if team isn't the champ"
        if not self.team_is_champ():
            return False
        return self.get_quantity_of_elimination_games()

    def get_quantity_of_won_elimination_games(self):
        if self.team_is_champ() or any(
            [series.ongoing_series() for series in self.series]
        ):
            return self.get_quantity_of_elimination_games()
        return self.get_quantity_of_elimination_games() - 1 if self.get_quantity_of_elimination_games() > 0 else 0


def build_teams_resumes(all_playoff_series):
    # Initializes the dict with all the users on the period
    yearly_dict = {str(series.playoff_year()): [] for series in all_playoff_series}

    # Separate all series by year
    for series in all_playoff_series:
        yearly_dict[str(series.playoff_year())] = yearly_dict[
            str(series.playoff_year())
        ] + [series]

    # separate all series of the year by team
    team_yearly_report = {}
    for year in yearly_dict:
        # Get all teams that were in those playoffs
        all_teams = set()
        for series in yearly_dict.get(year):
            all_teams.add(series.winner)
            all_teams.add(series.loser)
        team_yearly_report[year] = {team: [] for team in all_teams}

        # Separate each series by teams
        for series in yearly_dict.get(year):
            team_yearly_report[year][series.winner].append(series)
            team_yearly_report[year][series.loser].append(series)

    # Create the objs with the series
    teams_yearly_objs = set()
    for year in team_yearly_report:
        for team in team_yearly_report.get(year):
            teams_yearly_objs.add(
                TeamPlayoffYear(
                    team=team, year=year, series=team_yearly_report.get(year).get(team)
                )
            )

    return list(teams_yearly_objs)
