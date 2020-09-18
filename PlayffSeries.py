class PlayoffSeries():
    # https://www.basketball-reference.com/playoffs/NBA_2019.html
    # https://www.basketball-reference.com/playoffs/2019-nba-eastern-conference-first-round-pistons-vs-bucks.html
    """
    get the div class="game_summaries"
        for fiv in it
            get table
                tr winner
                    td regex name
                    td class righ (points)
                tr loser
                    td regex name
                    td class righ (points)

    """

    self.series_name:str
    self.winner: TeamSeries #ref to TeamSeries
    self.loser: TeamSeries #ref to TeamSeries
