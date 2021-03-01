import pyaudio
import wave


class Keybind:
    def __init__(self):
        self.keybinds = {}

    def __str__(self):
        string = ''
        for x in self.keybinds.keys():
            string += f'{x} : {self.keybinds[x]}\n'
        return string

    def search(self, key):
        data = self.keybinds.get(key, None)
        return data


class KeybindHandler:
    def create_keybind(self):
        object = Keybind()
        return object

    def bind_keybind(self, object, binds):
        x = 1
        for slot in binds:
            object.keybinds[slot] = 'slot'+str(x)
            x += 1


class Soundboard:
    def __init__(self):
        self.sounds = {'slot1': None,
                       'slot2': None,
                       'slot3': None,
                       'slot4': None,
                       'slot5': None,
                       'slot6': None,
                       'slot7': None,
                       'slot8': None}

    def __str__(self):
        string = ''
        for x in self.sounds.keys():
            string += f'{x} : {self.sounds[x]}\n'
        return string

    def press(self, slot):
        if slot is not None:
            if self.sounds[slot] is not None:
                self.sounds[slot].play_sound()


class SoundboardHandler:
    def create_soundboard(self):
        object = Soundboard()
        return object

    def bind_soundboard(self, object, soundlist):
        x = 1
        for sound in soundlist:
            object.sounds['slot'+str(x)] = sound
            x += 1

    def bind_single_sound(self, object, sound, slot):
        object.sounds[slot] = sound


class Sound:
    def __init__(self, filename):
        self. filename = filename
        self.chunk = 1024
        self.playing = False
        self.stream = None
        self.p = None

    def __str__(self):
        return self.filename

    def play_sound(self):
        wf = wave.open(self.filename, 'rb')
        self.p = pyaudio.PyAudio()
        #pyaudio testing
        #print(self.p.)
        for device in range(0,40):
            info = self.p.get_device_info_by_index(device)
            print(info['index'], info['maxInputChannels'], info['maxOutputChannels'], info['name'] )

        self.stream = self.p.open(format=self.p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        #input=True,
                        output=True,
                        #input_device_index=,
                        output_device_index=6)
        data = wf.readframes(self.chunk)
        #self.playing == True
        while data != b'':
            self.stream.write(data)
            data = wf.readframes(self.chunk)

        #self.playing = False
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def pause_sound(self):
        pass

    def stop_sound(self):
        self.playing = False
        self.stream.close()
        self.p.terminate()


class SoundHandler:
    def create_sound(self, filename):
        object = Sound(filename)
        return object

