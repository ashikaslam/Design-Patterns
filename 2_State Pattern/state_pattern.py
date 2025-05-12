from abc import ABC, abstractmethod

# State Interface
class State(ABC):
    @abstractmethod
    def click_play(self, player):
        pass

# Concrete States
class PlayingState(State):
    def click_play(self, player):
        print("Pausing the music.")
        player.state = PausedState()

class PausedState(State):
    def click_play(self, player):
        print("Resuming the music.")
        player.state = PlayingState()

# Context
class MusicPlayer:
    def __init__(self):
        self.state = PausedState()  # Default state

    def click_play(self):
        self.state.click_play(self)

# Example Usage
if __name__ == "__main__":
    player = MusicPlayer()

    player.click_play()  # Output: Resuming the music.
    player.click_play()  # Output: Pausing the music.
    player.click_play()  # Output: Resuming the music.
