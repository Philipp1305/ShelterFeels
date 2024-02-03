from dataclasses import dataclass

@dataclass
class Style:
    default_background = 'grey'
    default_text_font = 'Robot Mono'
    default_text_color = 'black'
    default_text_size = 30
    deafault_window_size = 450


style = Style()
