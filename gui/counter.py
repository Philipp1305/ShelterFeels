from dataclasses import dataclass, field

@dataclass
class Counter:
    button_count: int = 1
    color_count: int = 1
    color_list = ["red" , "green" , "blue"]

    def loop_color(self) -> str:
        '''returns the next color, loops through list'''

        color = self.color_list[self.color_count]

        self.color_count += 1
        if self.color_count >= len(self.color_list):
            self.color_count = 0

        return color

counter = Counter()
