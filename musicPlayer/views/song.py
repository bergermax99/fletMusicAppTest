import flet as ft


class Song:
    def __init__(self, title, artist, audioPath, picturePath):
        self.title = title
        self.artist = artist
        self.audioPath = audioPath
        self.picturePath = picturePath
        self.audio = ft.Audio(
            src=audioPath,
            autoplay=False,
            volume=1,
            balance=0,
            on_loaded=lambda _: print("Loaded"),
            on_duration_changed=lambda e: print("Duration changed:", e.data),
            on_position_changed=lambda e: print("Position changed:", e.data),
            # on_state_changed=lambda e: print("State changed:", e.data),
            on_state_changed=self.isPlaying,
            on_seek_complete=lambda _: print("Seek complete"),
        )
        self.togglePlay = True

    def isPlaying(self, e):
        if e.data == "playing":
            self.togglePlay = True
        elif e.data == "paused":
            self.togglePlay = False




