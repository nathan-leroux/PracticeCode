from Config import (Keybind,
                    KeybindHandler,
                    Sound,
                    SoundHandler,
                    Soundboard,
                    SoundboardHandler)
from Talkbox import Talkbox


class Interface:
    def __init__(self):
        self.keybindH = KeybindHandler()
        self.soundboardH = SoundboardHandler()
        self.soundH = SoundHandler()

        self.menu = None

    def get_keybinds(self):
        templist = ['u', 'i', 'o']
        binds = self.keybindH.create_keybind()
        self.keybindH.bind_keybind(binds, templist)
        return binds

    def get_soundboard(self):
        templist = [Sound('Phantomcigar.wav')]
        board = self.soundboardH.create_soundboard()
        self.soundboardH.bind_soundboard(board, templist)
        return board
    #TODO: perminent keybinds and soundboard
    #TODO: menu board
    def get_menu_board(self):
        pass

    def start_menu(self):
        pass

    def start_talkbox(self):
        kb = self.get_keybinds()
        sb = self.get_soundboard()
        print(sb, kb)
        tb = Talkbox(sb, kb)
        tb.start_talkbox()


if __name__ == '__main__':
    interface = Interface()
    interface.start_talkbox()
