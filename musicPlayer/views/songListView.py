import flet as ft


def song_list_view(page, songs):

    list_view = ft.Column()

    def goToSong(e, s):
        print(s.audioPath)
        page.go("/" + s.audioPath)

    for s in songs:

        list_view.controls.append(
            ft.ListTile(
                title=ft.Text(s.title + " - " + s.artist, theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
                on_click= lambda e, path=s: goToSong(e, path),
                expand=False,
            ),
        )

    return ft.View("/", [list_view])