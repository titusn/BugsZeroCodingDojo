import unittest
from approvaltests.approvals import verify
from subprocess import run
from game import Game, InvalidNumberOfPlayers
import pytest

class GameTest(unittest.TestCase):
    def test_trivia_game(self):
        output = run(["python", "game_runner.py"], capture_output=True).stdout
        verify(output.decode())

        # save the output as 'previous output'



def test_game_can_only_be_played_with_enough_players():
  game = Game(players=['Titus'])
  with pytest.raises(InvalidNumberOfPlayers):
    game.roll(4)


def test_game_can_not_be_played_with_more_than_6_players():
  with pytest.raises(InvalidNumberOfPlayers):
     game = Game(players = ['Titus1','Titus2','Titus3','Titus4','Titus5','Titus6','Titus7'])


def test_game_can_be_played_with_6_players(capsys):
  game = Game(players=['Martijn1', 'Martijn2', 'Martijn3', 'Martijn4', 'Martijn5', 'Martijn6'])
  
  game.roll(4)
  captured = capsys.readouterr()
  assert "They have rolled a 4" in captured.out


if __name__ == "__main__":
    unittest.main()

