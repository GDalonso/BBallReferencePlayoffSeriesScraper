from champsGetter import retieve_nba_champs_since_merger
from constants import ALL_TEAMS_NAMES
from seasonsGetter import scrap_seasons
from seriesGetter import parse_scores_from_series_page
import os

os.environ["HUE"] = "1"

if __name__ == "__main__":
    # parse_scores_from_series_page(scrap_seasons(2018, 2019))
    all_series = parse_scores_from_series_page(scrap_seasons(1977, 2019))
    yearly_dict = {str(series.playoff_year()): [] for series in all_series}
    for series in all_series:
        yearly_dict[str(series.playoff_year())] = yearly_dict[
            str(series.playoff_year())
        ] + [series]
    team_yearly_report = {}
    for key in yearly_dict:
        for team_name in ALL_TEAMS_NAMES:
            team_yearly_report[f"{key} {team_name}"] = 0
        for series in yearly_dict[key]:
            team_yearly_report[f"{series.playoff_year()} {series.winner.upper()}"] = (
                team_yearly_report[f"{series.playoff_year()} {series.winner.upper()}"]
                + series.winner_elimination_games()
            )
            team_yearly_report[f"{series.playoff_year()} {series.loser.upper()}"] = (
                team_yearly_report[f"{series.playoff_year()} {series.loser.upper()}"]
                + series.loser_elimination_games()
            )
    # def filter_zeroes(key, value):
    #     return True if value > 0 else False
    # list(filter(filter_zeroes, team_yearly_report.items()))

    sort_orders = sorted(team_yearly_report.items(), key=lambda x: x[1], reverse=True)

    # clutchest_teams = {}
    # for index in range(0, len(all_series)):
    #     clutchest_teams[str(index)] = {}

    assert True
