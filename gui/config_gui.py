from dataclasses import dataclass

@dataclass
class Settings:
    default_background = 'grey'
    default_text_font = 'Comic Sans MS'
    default_text_color = 'black'

gui_settings = Settings()
