from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector
from kivy.clock import Clock

class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x,velocity_y)

    #Latest position = current velocity * time + current position
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    def update(self,dt):
    #moving the ball by calling the move function

class PongApp(App):
    def build(self):
        game = PongGame()
        Clock.schedule_interval(game.update,1.0/60.0)
        return PongGame()

PongApp().run()
