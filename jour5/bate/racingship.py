from ship import Ship

class RacingShip(Ship):
    
    def __init__(self, name, parts=None, max_speed=0):
        super().__init__(name, parts)
        self.max_speed = max_speed
    
    def display_speed(self):
        print(f" Vitesse maximale: {self.max_speed} nœuds")
    
    def display_state(self):
        
        super().display_state()
        self.display_speed()
        print()