# 👉 Run "./connect" (or "connect.cmd" on Windows) in the terminal to get started
class Bot:
    def __init__(self, config):
      self.config = config
        print("Hello World!", config)
        pass

    def move(self, fen):
        # The current game state in Forsyth-Edwards notation
        # https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
        print(fen)

        # Return moves using algebraic notation
        # https://en.wikipedia.org/wiki/Algebraic_notation_(chess)
        return "e4" if self.config.player == "white" else "e5"

    def end(self, fen):
        print("Good game!")
