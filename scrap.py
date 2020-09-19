from champsGetter import retieve_nba_champs_since_merger
from seasonsGetter import scrap_seasons
from seriesGetter import parse_scores_from_series_page


if __name__ == "__main__":
    # parse_scores_from_series_page(scrap_seasons(2018, 2019))
    parse_scores_from_series_page(scrap_seasons(2019, 2019))
    # retieve_nba_champs_since_merger()
    assert True
