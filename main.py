from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

class MertAIApp(App):
    def build(self):
        self.title = "Mert AI"
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        header = Label(text="Mert AI", font_size='24sp', size_hint_y=None, height=50, bold=True)
        main_layout.add_widget(header)

        self.scroll = ScrollView()
        self.chat_history = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.chat_history.bind(minimum_height=self.chat_history.setter('height'))
        self.scroll.add_widget(self.chat_history)
        main_layout.add_widget(self.scroll)

        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=10)
        self.entry = TextInput(hint_text="Mert AI'ya yaz...", multiline=False)
        send_btn = Button(text="Gönder", size_hint_x=None, width=100, on_press=self.send_message)
        
        input_layout.add_widget(self.entry)
        input_layout.add_widget(send_btn)
        main_layout.add_widget(input_layout)

        self.add_message("Mert AI", "Merhaba! Ben senin özel asistanın Mert AI.")
        return main_layout

    def add_message(self, sender, message):
        lbl = Label(
            text=f"[b]{sender}:[/b] {message}", 
            markup=True, 
            size_hint_y=None, 
            text_size=(Window.width - 40, None),
            halign='left'
        )
        lbl.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.chat_history.add_widget(lbl)

    def send_message(self, instance):
        msg = self.entry.text.strip()
        if msg:
            self.add_message("Sen", msg)
            self.entry.text = ""
            response = f"'{msg}' mesajını aldım! Tamamen bağımsız bir APK olarak çalışıyorum."
            self.add_message("Mert AI", response)

if __name__ == "__main__":
    MertAIApp().run()
