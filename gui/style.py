from dataclasses import dataclass

@dataclass
class Style:
    default_background = 'grey'
    default_text_font = 'Robot Mono'
    default_text_color = 'black'
    default_text_size = 45
    default_window_size = 480
    has_titlebar = True


style = Style()
