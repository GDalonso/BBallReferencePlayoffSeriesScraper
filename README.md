# BBallReferencePlayoffSeriesScraper
Scrape all time playoff series data from BasketBall reference to perform analysis

Start reading by main.py

Models contains
    
    - PlayoffGame: Used to represent a game
    - PlayoffSeries: Used to represent a series with various games
    - TeamPlayoffYear: Agregates all the series a team played during an year

Getters_scrappers contains
    
    - ChampsGetter: get all the champs by year
    - seasonsGetter: get the urls for all playoff series during an year
    - seriesGetter: get the data for each series, instatiate games and then series

implemented_stats
    
    - contains all the stats already implemented

deploying with cloud functions

    With your terminal with gcloud sdk setup used
    gcloud functions deploy hello_get --trigger-http --runtime python38    
    
    where
        - functions = google cloud functions
        - hello_get = name of the function in the main.py file i want to deploy
        - trigger-http = trigers the function when get a request
        -- runtime = python version