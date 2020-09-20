from champsGetter import retieve_nba_champs_since_merger

SERIES_LENGTH_BY_WINNER_WINS = {"1": 1, "2": 3, "3": 5, "4": 7}
WINS_NECESSARY_BY_SERIES_LENGTH = {"1": 1, "3": 2, "5": 3, "7": 4}

# that's not a const LMAO
NBA_CHAMPS = retieve_nba_champs_since_merger()
keys_playoffs_depr = [
    "East Conf 1st Round",
    "West Conf 1st Round",
    "East Conf Semis",
    "West Conf Semis",
    "East Conf Finals",
    "West Conf Finals",
    "Finals",
]

keys_playoffs = [
    "Eastern Conference First Round",
    "Western Conference First Round",
    "Eastern Conference Semifinals",
    "Western Conference Semifinals",
    "Eastern Conference Finals",
    "Western Conference Finals",
    "Finals",
]

ALL_TEAMS_NAMES = [
    "ATLANTA HAWKS",
    "BOSTON CELTICS",
    "BROOKLYN NETS",
    "CHARLOTTE HORNETS",
    "CHICAGO BULLS",
    "CLEVELAND CAVALIERS",
    "DALLAS MAVERICKS",
    "DENVER NUGGETS",
    "DETROIT PISTONS",
    "GOLDEN STATE WARRIORS",
    "HOUSTON ROCKETS",
    "INDIANA PACERS",
    "LOS ANGELES CLIPPERS",
    "LOS ANGELES LAKERS",
    "MEMPHIS GRIZZLIES",
    "MIAMI HEAT",
    "MILWAUKEE BUCKS",
    "MINNESOTA TIMBERWOLVES",
    "NEW ORLEANS PELICANS",
    "NEW YORK KNICKS",
    "OKLAHOMA CITY THUNDER",
    "ORLANDO MAGIC",
    "PHILADELPHIA 76ERS",
    "PHOENIX SUNS",
    "PORTLAND TRAIL BLAZERS",
    "SACRAMENTO KINGS",
    "SAN ANTONIO SPURS",
    "TORONTO RAPTORS",
    "UTAH JAZZ",
    "WASHINGTON WIZARDS",
    # Names that don't exist anymore (names from 1977 on)
    "BUFFALO BRAVES",
    "CHARLOTTE BOBCATS",
    "KANSAS CITY KINGS",
    "NEW JERSEY NETS",
    "NEW ORLEANS HORNETS",
    "NEW ORLEANS JAZZ",
    "NEW ORLEANS/OKLAHOMA CITY HORNETS",
    "SAN DIEGO CLIPPERS",
    "SEATTLE SUPERSONICS",
    "WASHINGTON BULLETS",
    "VANCOUVER GRIZZLIES",
]
