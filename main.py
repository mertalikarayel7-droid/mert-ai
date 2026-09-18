from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock

class MertAIApp(App):
    def build(self):
        self.title = "Mert AI"
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        header = Label(text="Mert AI", font_size='20sp', size_hint_y=None, height=40, bold=True)
        main_layout.add_widget(header)
        
        self.scroll = ScrollView(size_hint=(1, 1))
        self.chat_history = Label(
            text="Mert AI: Merhaba Mert Ali! Ben senin özel asistanın Mert AI.\n\n",
            font_size='14sp',
            size_hint_y=None,
            markup=True
        )
        self.chat_history.bind(texture_size=lambda instance, value: setattr(instance, 'height', value[1]))
        self.scroll.add_widget(self.chat_history)
        main_layout.add_widget(self.scroll)
        
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50, spacing=5)
        self.user_input = TextInput(hint_text="Mesajınızı yazın...", multiline=False, font_size='14sp')
        self.user_input.bind(on_text_validate=self.send_message)
        
        send_btn = Button(text="Gönder", size_hint_x=None, width=100, bold=True)
        send_btn.bind(on_press=self.send_message)
        
        input_layout.add_widget(self.user_input)
        input_layout.add_widget(send_btn)
        main_layout.add_widget(input_layout)
        
        return main_layout

    def send_message(self, instance):
        msg = self.user_input.text.strip()
        if msg:
            self.chat_history.text += f"[b]Sen:[/b] {msg}\n\n"
            self.user_input.text = ""
            Clock.schedule_once(lambda dt: self.bot_reply(msg), 0.5)

    def bot_reply(self, user_msg):
        response = f"Mert AI: '{user_msg}' mesajını aldım!"
        self.chat_history.text += f"{response}\n\n"
        self.scroll.scroll_y = 0

if __name__ == "__main__":
    MertAIApp().run()
