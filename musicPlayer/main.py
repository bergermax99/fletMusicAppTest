import flet as ft
from views.song import Song
from views.playerView import player_view
from views.songListView import song_list_view



songs = [
    Song("Another Brick in the Wall", "Pink Floyd", "assets/AnotherBrickInTheWall_PinkFloyd.mp3", "assets/anotherbrickinthewall.png"),
    Song("Nie mehr Schule", "Falco", "assets/NieMehrSchule_Falco.mp3", "assets/niemehrschule.png"),
    Song("Schools Out", "Alice Cooper", "assets/SchoolsOut_AliceCooper.mp3", "assets/schoolsout.png"),
]


def main(page: ft.Page):
    page.window.width = 500
    page.window.height = 500
    page.title = "Music Player"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.min_width = 375
    page.window.min_height = 450

    for i in songs:
        page.overlay.append(i.audio)


    def route_change(route):
        page.views.clear()

        for s in songs:

            if page.route == "/" + s.audioPath:
                page.views.append(player_view(page,s))
                page.update()

        if page.route == "/":
            page.views.append(song_list_view(page, songs))
            page.update()

        page.update()

    page.on_route_change = route_change
    page.go("/")


ft.app(main)
