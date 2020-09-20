from models.TeamPlayoffYear import build_teams_resumes
from getters_scrappers.seasonsGetter import scrap_seasons
from implemented_stats import teams_that_played_the_most_elimination_games, champs_that_faced_most_elimination_games, \
    teams_that_won_the_most_elimination_games
from getters_scrappers.seriesGetter import parse_scores_from_series_page

if __name__ == "__main__":


    all_series = parse_scores_from_series_page(scrap_seasons(1977, 1977))
    playoff_resume = build_teams_resumes(all_series)

    teams_with_most_elimination_games=teams_that_played_the_most_elimination_games(playoff_resume)

    champs_with_most_elimination_games=champs_that_faced_most_elimination_games(playoff_resume)

    teams_that_won_most_elimination_games=teams_that_won_the_most_elimination_games(playoff_resume)

assert True
