from seasonsGetter import scrap_seasons
from seriesGetter import parse_scores_from_series_page


if __name__ == "__main__":
    # parse_scores_from_series_page(scrap_seasons(2018, 2019))
    parse_scores_from_series_page(scrap_seasons(2010, 2019))
