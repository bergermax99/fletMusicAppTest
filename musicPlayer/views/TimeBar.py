import flet as ft
import time
import threading

class TimeBar:
    def __init__(self, audio, width=250):
        self.audio = audio
        self.progress_bar = ft.ProgressBar(value=0.0, width=width)
        self.running = False
        self.update_thread = None

        # Text für aktuelle Zeit und verbleibende Zeit
        self.current_time_text = ft.Text("0:00")
        self.remaining_time_text = ft.Text("0:00")

    def start(self):
        self.running = True
        self.update_thread = threading.Thread(target=self._update_progress, daemon=True)
        self.update_thread.start()

    def stop(self):
        self.running = False
        if self.update_thread:
            self.update_thread.join()

    def _update_progress(self):
        while self.running:
            current_position = self.audio.get_current_position()
            duration = self.audio.get_duration()

            if duration > 0:  # Vermeide Division durch Null
                self.progress_bar.value = current_position / duration

                # Aktualisiere die Zeit-Texte
                self.current_time_text.value = self._format_time(current_position)
                self.remaining_time_text.value = self._format_time(duration - current_position)

                # Update die UI nur, wenn die ProgressBar bereits zur Seite hinzugefügt wurde
                if self.progress_bar.page:
                    self.progress_bar.update()
                    self.current_time_text.update()
                    self.remaining_time_text.update()

            time.sleep(1)  # Warte eine Sekunde

    def get_progress_bar(self):
        return ft.Row(
            controls=[
                self.current_time_text,
                self.progress_bar,
                self.remaining_time_text
            ],
            alignment=ft.MainAxisAlignment.CENTER,  # Vertikal zentrieren

            expand=False,  # Deckt den gesamten verfügbaren Bereich ab
        )

    def _format_time(self, seconds):
        """ Hilfsfunktion zur Formatierung von Sekunden in mm:ss """
        minutes = int(seconds/1000) // 60
        seconds = int(seconds/1000) % 60
        return f"{minutes}:{seconds:02d}"
