from pynput.keyboard import Listener, KeyCode


class Talkbox:
    def __init__(self, soundboard, keybinds):
        self.listener = None
        self.soundboard = soundboard
        self.keybinds = keybinds

    def _pos(self, key):
        keyinput = self._clean_input(key)
        self._toggle(keyinput)

    def _neg(self, key):
        pass
    #TODO: clean up methods
    def start_talkbox(self):
        with Listener(on_press=self._pos,
                      on_release=self._neg) as self.listener:
            self.listener.join()

    def stop_talkbox(self):
        self.listener.stop()

    def _clean_input(self, key):
        if type(key) == KeyCode:
            clean = self.keybinds.search(key.char)

            return clean

    def _toggle(self, key):
        self.soundboard.press(key)
        #TODO: running soundboard in thread
