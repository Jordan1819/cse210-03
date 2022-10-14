from game.guesser import Guesser
from game.jumper import Jumper
from game.terminal_service import TerminalService
#First we want to import all of the classes we need - Jordan

class Director:
    def __init__(self):
        #Assign classes to variables/ attributes - Jordan
        self._guesser = Guesser()
        self._jumper = Jumper()
        self._terminal_service = TerminalService()
        pass
