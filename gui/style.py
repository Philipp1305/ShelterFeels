from dataclasses import dataclass

@dataclass
class Style:
    default_background = 'grey'
    default_text_font = 'Robot Mono'
    default_text_color = 'black'

style = Style()
