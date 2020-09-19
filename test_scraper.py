def test_scrap_seasons():
    """
    test the old and new behaviours for getting the series links
    """
    from bs4 import BeautifulSoup
    import requests

    urls = urls_depr = []

    url = f"https://www.basketball-reference.com/playoffs/NBA_2010.html"

    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    from seasonsGetter import get_container_with_series

    urls = urls + get_container_with_series(soup)

    from seasonsGetter import get_container_with_series_deprecated

    urls_depr = urls_depr + get_container_with_series_deprecated(soup)

    assert urls.sort() == urls_depr.sort()
