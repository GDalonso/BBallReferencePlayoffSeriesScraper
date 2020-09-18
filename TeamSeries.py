class TeamSeries:
    self.team: str
    self.winner: bool
    self.games: list  #  {'game1':{"win"=True, "eliminationGame"=False}}
    # self.eliminationGames = self.countEliminations(self.games)

    def countEliminations(games=self.games):
        eliminationGames = 0
        for game in games:
            if game.get("eliminationGame", False):
                eliminationGames = eliminationGames + 1
