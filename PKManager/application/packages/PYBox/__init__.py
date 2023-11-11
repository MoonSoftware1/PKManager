__commands__ = []


class PYBox:
    def __init__(self, text_box):
        self.text_box = text_box
        self.current_text = self.text_box.text()
        self.last_line = self.get_last_line()
        self.on_enter_pressed()

    def get_last_line(self):
        lines = self.current_text.split('\n')
        last_line = lines[-1] if lines else ""
        return last_line

    def on_enter_pressed(self):
        self.current_text += "\n"  # Ajouter un caractère de nouvelle ligne
        self.text_box.setText(self.current_text)