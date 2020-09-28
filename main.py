from models.TeamPlayoffYear import build_teams_resumes
from getters_scrappers.seasonsGetter import scrap_seasons
from implemented_stats import teams_that_played_the_most_elimination_games, champs_that_faced_most_elimination_games, \
    teams_that_won_the_most_elimination_games
from getters_scrappers.seriesGetter import parse_scores_from_series_page
from flask import jsonify, abort

stats_to_func_dict = {
    'teams_with_most_elimination_games': teams_that_played_the_most_elimination_games,
    'champs_with_most_elimination_games': champs_that_faced_most_elimination_games,
    'teams_that_won_most_elimination_games': teams_that_won_the_most_elimination_games,
}

# [START functions_get_stat]
def get_stat(request):
    if request.method == 'GET':
        return docs()
    elif request.method == "POST":
        content_type = request.headers['content-type']
        if content_type == 'application/json':
            result = request.get_json(force=True)
        elif content_type == 'application/x-www-form-urlencoded':
            result = request.form
        else:
            return ValueError("content must be json or form encoded")

        try:
            startYear = int(result.get('startYear'))
            endYear = int(result.get('endYear'))
        except Exception as e:
            return {"error", "Your data isn't well formated, please use postman for tests"}

        playoff_resume = get_bbalref_data(startYear, endYear)
        statFunc = stats_to_func_dict.get(result.get('stat'), None)

        if statFunc:
            stat_res = statFunc(playoff_resume)
            return jsonify(stat_res)

    return abort(404)

# [END functions_get_stat]

def docs(hue=None):
    return "doc to be implemented"


def get_bbalref_data(startYear, endYear=None):
    if not endYear:
        endYear = startYear
    all_series = parse_scores_from_series_page(scrap_seasons(startYear, endYear))
    playoff_resume = build_teams_resumes(all_series)
    return playoff_resume
