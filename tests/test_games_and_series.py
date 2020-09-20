from models.TeamPlayoffYear import build_teams_resumes, TeamPlayoffYear
from tests.mocks import mock_playoffGame, mock_series, mock_team_year_resume


def test_playoffGame():
    game = mock_playoffGame()
    # Has no behaviours to test

def test_playoffSeries():
    pseries = mock_series()

    assert pseries.winner_wins() == 4
    assert pseries.loser_wins() == 1
    assert pseries.winner_is_champ() is False
    assert pseries.loser_elimination_games() == 1
    assert pseries.winner_elimination_games() == 0
    assert pseries.ongoing_series() is False
    assert pseries.team_elimination_games

def test_TeamPlayoffYear():
    team_playoff_year=mock_team_year_resume()

    assert team_playoff_year.get_quantity_of_elimination_games() == 0
    assert team_playoff_year.team_is_champ() is False
    assert team_playoff_year.get_quantity_of_elimination_games_by_champ() is False
    assert team_playoff_year.get_quantity_of_won_elimination_games()==0


def test_build_resumes():
    all_year_series = [mock_series() for i in range(2)]
    team_by_year=build_teams_resumes(all_year_series)
    assert isinstance(team_by_year[0], TeamPlayoffYear)