import flet as ft
from views.song import Song
from views.TimeBar import TimeBar

def player_view(page, song: Song):

    song.audio.play()

    time_bar = TimeBar(song.audio)
    time_bar.start()


    def play_pause(e):
        if song.togglePlay:
            song.audio.pause()
        else:
            song.audio.resume()

        page.update()

    def seek_forward(e):
        song.audio.seek(song.audio.get_current_position() + 10000)
        page.update()

    def seek_backward(e):
        song.audio.seek(song.audio.get_current_position() - 10000)
        page.update()

    def backToPlaylist(e):
        song.audio.pause()
        time_bar.stop()
        page.go("/")

    return ft.View(
        controls = [
            ft.ElevatedButton(text = "back", icon =  ft.icons.KEYBOARD_BACKSPACE, on_click=backToPlaylist),

            ft.Column(
                [
                    ft.Image(
                        src=song.picturePath,
                        width=150,
                        height=150,
                        border_radius=ft.border_radius.all(50),
                    ),
                    ft.Text(song.title + " - " + song.artist, size=20),
                    time_bar.get_progress_bar(),
                    ft.Row(
                        [
                            ft.IconButton(ft.icons.REPLAY_10, on_click=seek_backward),
                            ft.IconButton(ft.icons.PLAY_ARROW, on_click=play_pause),
                            ft.IconButton(ft.icons.FORWARD_10, on_click=seek_forward),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,  # Buttons zentrieren
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,  # Vertikal zentrieren
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,  # Horizontal zentrieren
                expand=True,  # Deckt den gesamten verfügbaren Bereich ab
            ),
        ]
    )