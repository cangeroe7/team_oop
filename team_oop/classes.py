class Game:
    def __init__(self, games):
        self.games = games
        self.player1 = ""
        self.player2 =  ""
        self.player1Level = 0
        self.player2Level = 0

    def get_player_names(self):
        while self.player1 != "":
            self.player1 = input("Player 1 what is your name: ")

        while self.player2 != "" or self.player2 != self.player1:
            self.player2 = input("Player 2 what is your name: ")

    def end_screen(self, winner):
        if winner == 1:
            print(f"congrats {self.player1}, you won!")
        if winner == 2:
            print(f"congrats {self.player2}, you won!")
        if winner == 3:
            print(f"congrats {self.player1}, and {self.player2}, it is a tie!")            
        

    def play_game(self):
        while True:
            self.player1Level += self.games[self.player1Level]()
            self.player2Level += self.games[self.player2Level]()
            if self.player1Level == 7 and self.player2Level == 7:
                self.end_screen(3)
                return
            if self.player1Level == 7:
                self.end_screen(1)
            if self.player2Level == 7:
                self.end_screen(2)
