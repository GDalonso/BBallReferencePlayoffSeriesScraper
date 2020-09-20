from PlayoffsYear import build_teams_resumes
from champsGetter import retieve_nba_champs_since_merger
from seasonsGetter import scrap_seasons
from seriesGetter import parse_scores_from_series_page
import os

os.environ["HUE"] = "1"

if __name__ == "__main__":
    # parse_scores_from_series_page(scrap_seasons(2018, 2019))
    all_series = parse_scores_from_series_page(scrap_seasons(1977, 1977))
    playoff_resume = build_teams_resumes(all_series)

    # Sort all the teams with the most elimination games
    a = {}
    for team_yearly_resume in playoff_resume:
        a[
            f"{team_yearly_resume.year} {team_yearly_resume.team}"
        ] = team_yearly_resume.get_quantity_of_elimination_games()
    most_teams_with_elimination_games = sorted(
        a.items(), key=lambda x: x[1], reverse=True
    )

    team_yearly_resume.get_quantity_of_elimination_games_by_champ()
    team_yearly_resume.get_quantity_of_elimination_games_by_champ()
    team_yearly_resume.get_quantity_of_won_elimination_games()


assert True
