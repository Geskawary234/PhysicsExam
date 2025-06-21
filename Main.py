#Графика
import pyglet
from pyglet import shapes, clock, gl
from pyglet.window import key

#Информация о мониторе
from screeninfo import get_monitors

#Физика
from Box2D.b2 import *

#Математика
from math import cos, sin, tan, radians, pi, sqrt, degrees

#Системные
import sys
from os import _exit

#UI
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from sim_settings import Ui_SimulationSettings

#json
from json import dump

from Methods import resource_path




#C:/Users/danil/Desktop/PhysicsExam/icon.ico


class SimSettings(QMainWindow):
    process_going = True
    can_be_unpaused = True
    icon_pause = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackPause))
    icon_continue = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaPlaybackStart))

    object_type : str = 'Шар'

    def __init__(self):
        super().__init__()
        self.ui = Ui_SimulationSettings()
        self.ui.setupUi(self)

        self.ui.Pause.clicked.connect(self.pause)
        self.ui.SurfAng.valueChanged.connect(self.change_angle)
        self.ui.GroundLevel.valueChanged.connect(self.ChangeGroundLevel)
        self.ui.Restart.clicked.connect(self.restart)
        #self.ui.WriteVel.clicked.connect(self.write_vel)

        self.ui.CylinderSelect.clicked.connect(lambda: self.change_phys_obj(1))
        self.ui.SphereSelect.clicked.connect(lambda: self.change_phys_obj(0))

        self.move(sc_w // 4, sc_h + 600 - sc_h)

        self.change_angle(self.ui.SurfAng.value())
        self.restart()


        

    def write_vel(self):
        global time_velocity
        with open('Velocity.json', 'w') as f:
            additional_data = {
                'Angle': self.ui.SurfAng.value(),
                'L': self.get_surf_len()
            }
            dump(additional_data | time_velocity, f, indent=4)

  


    def pause(self):

        if not self.can_be_unpaused: return
        
        if self.process_going:
            clock.unschedule(process)
        else:
            #ball.physics_body.type = dynamicBody
            clock.schedule(process)

        self.process_going = not self.process_going
        self.update_pause_btn_icon()

    def change_phys_obj(self,obj):
        global ball
        world.DestroyBody(ball.physics_body)
        if obj == 0:
            ball = Sphere(obj_posx, obj_posy, obj_radius)
            self.object_type = 'Шар'
        elif obj == 1:
            ball = Cylinder(obj_posx, obj_posy, obj_radius)
            self.object_type = 'Цилиндр'

        self.change_angle(self.ui.SurfAng.value())
        self.ui.label_2.setText(f'Тип объекта: {self.object_type}')

    def update_pause_btn_icon(self):
        self.ui.Pause.setIcon(self.icon_pause if self.process_going else self.icon_continue)

    def restart(self):
        self.can_be_unpaused = True
        self.clear_data_to_write()
        self.change_angle(surf.rotation)
        #self.pause()

    def clear_data_to_write(self):
        global time_velocity, time_since_start, next_write_time
        time_velocity = {}
        time_since_start = 0
        next_write_time = 0
        

    def get_surf_len(self):
        sf_pos = surf.position[1] - ground_height
        sf_rot = radians(self.ui.SurfAng.value())
        if tan(sf_rot) != 0:
            return (sf_pos/sin(sf_rot))/50
        else:
            return surf.width/100

    def change_angle(self, v):
        self.can_be_unpaused = True
        self.clear_data_to_write()
        
        self.ui.label.setText(f'Угол плоскости: {v}˚')
        self.ui.SurfLen.setText(f'Длинна плоскости: {round(self.get_surf_len(),2)} м')
        self.process_going = True
        self.pause()

        PLATFORM_WIDTH = surf.size_x
        PLATFORM_HEIGHT = surf.size_y
        BALL_RADIUS = ball.radius

        BALL_RELATIVE_X_OFFSET = 0
        BALL_RELATIVE_Y_OFFSET = 0.03 + BALL_RADIUS/50

        surf.set_angle(v)
        angle_rad = surf.body.angle

        rotated_offset_x = BALL_RELATIVE_X_OFFSET * cos(angle_rad) - BALL_RELATIVE_Y_OFFSET * sin(angle_rad)
        rotated_offset_y = BALL_RELATIVE_X_OFFSET * sin(angle_rad) + BALL_RELATIVE_Y_OFFSET * cos(angle_rad)

        ball_final_x = surf.body.position.x + rotated_offset_x
        ball_final_y = surf.body.position.y + rotated_offset_y

        ball.set_position(ball_final_x, ball_final_y)
        ball.physics_body.linearVelocity = (0,0)
        ball.physics_body.angularVelocity = 0
        #ball.physics_body.type = staticBody
        ball.update()

    def closeEvent(self, event):
        _exit(0)

    def ChangeGroundLevel(self,val):
        global ground_height
        ground_height = (val/10) * 50
        
        self.ui.label_3.setText(f'Высота земли: {round(ground_height/50,2)} м')
        self.change_angle(self.ui.SurfAng.value())




class PhysCircle(shapes.Circle):
    
    def __init__(self, x, y, radius, color=(255, 0, 0)):
        global batch
        super().__init__(x * 50, y * 50, radius * 100, color=color, batch=batch)  # enlarged visual
        circle_body_def = bodyDef(type=dynamicBody, position=(x, y))
        
        circle_body = world.CreateBody(circle_body_def)
        
        circle_shape = circleShape(radius=radius)
        
        circle_fixture_def = fixtureDef(
            shape=circle_shape,
            density=100,
            friction=50,
            restitution=0
        )
        
        circle_body.CreateFixture(circle_fixture_def)

        
        self.physics_body = circle_body
        self.radius = radius * 50

    def update(self):
        self.x = self.physics_body.position.x * 50
        self.y = self.physics_body.position.y * 50
        self.rotation = -degrees(self.physics_body.angle)

    def get_velocity(self):
        v = self.physics_body.linearVelocity
        return sqrt(v[0] ** 2 + v[1] ** 2)

    def set_position(self, x, y, add=False):
        if add:
            self.physics_body.position += (x, y)
        else:
            self.physics_body.position = (x, y)

    def draw_velocity_vector(self):
        x = self.position[0]
        y = self.position[1]
        vx = self.physics_body.linearVelocity[0] * 50
        vy = self.physics_body.linearVelocity[1] * 50
        shapes.Line(x,y,x+vx,y+vy,thickness=2,color = (255,255,255,255)).draw()


class Sphere(PhysCircle):
    def __init__(self, x, y, radius, color=(255, 0, 0)):
        super().__init__(x, y, radius, color=color)
        
        SphereMass = (4/3) * pi * radius**3
        SphereI = (2/5) * SphereMass * radius**2

        Mdata = massData(
            mass = SphereMass,
            I = SphereI,
            center = (0,0)
            )

        self.physics_body.massData = Mdata
     
        #self.physics_body.mass = SphereMass
        #self.physics_body.inertia = SphereI

class Cylinder(PhysCircle):
    def __init__(self, x, y, radius, color=(255, 0, 0)):
        super().__init__(x, y, radius, color=color)
        
        cylinder_height = 1
        
        
        CylinderMass = pi * cylinder_height * radius**2
        CylinderI = (1/2) * CylinderMass * radius**2

        Mdata = massData(
            mass = CylinderMass,
            I = CylinderI,
            center = (0,0)
            )

        self.physics_body.massData = Mdata

    





class PhysRect(shapes.Rectangle):
    def __init__(self, x, y, w, h, color=(255, 255, 255)):
        super().__init__(x * 50, y * 50, w * 50, h * 50, color=color, batch=batch)
        self.anchor_position = (w * 25, h * 25)
        self.size_x = w
        self.size_y = h
        self.body = world.CreateStaticBody(position=(x, y), shapes=polygonShape(box=(w / 2, h / 2)))

    def set_angle(self, deg: float, add=False):
        self.rotation = deg if not add else self.rotation + deg
        self.body.angle = -radians(self.rotation)

def draw_grid(width, height, cell_size, color = 30):

    borders = 1
    
    rgb_col = (color, color, color, 255)
    
    for y in range(0,height,cell_size):
        shapes.Rectangle(0,y,width*2,borders,color = rgb_col).draw()

    for x in range(0,width,cell_size):
        shapes.Rectangle(x,0,borders,height*2,color = rgb_col).draw()

    pyglet.text.Label('1 м', font_name='Times New Roman', font_size=16,color = (255,255,255,255), x = width - 120, y = height-60).draw()

def draw_point_on_object(ball):
    rad_rot = -radians(ball.rotation)
    local_offset = (ball.radius-3,0)
    wx = ball.position[0] + (local_offset[0] * cos(rad_rot) - local_offset[1] * sin(rad_rot))
    wy = ball.position[1] + (local_offset[0] * sin(rad_rot) + local_offset[1] * cos(rad_rot))
    shapes.Circle(wx,wy, 3, 3, color = (0,0,255,255)).draw()



def draw_ball_speed(ball):
    global v_pos_x
    global v_pos_y
    
    if ball.x < 1100:
        v_pos_x = ball.x

    if ball.y > ball.radius:
        v_pos_y = ball.y

    
    label = pyglet.text.Label(
        f'{ball.get_velocity():.2f} м/с',
        font_name='Times New Roman',
        font_size=18,
        color=(255, 255, 255, 255),
        x=v_pos_x,
        y=v_pos_y + 40
        ).draw()
    
    

# Initialize physics and screen
monitor = get_monitors()[0]
sc_w = monitor.width
sc_h = monitor.height



window = pyglet.window.Window(1280, 540, 'Симуляция', vsync=True)
window.set_location(sc_w // 4, sc_h // 25)

app_icon = pyglet.image.load(resource_path("icon.ico"))
window.set_icon(app_icon)

world = world(gravity=(0, -9.81))

batch = pyglet.graphics.Batch()


    
    #draw_point_on_object(ball)

    


# Create scene
#ground = PhysRect(10, 0, 50, 1, color = (0,0,0,0))
#wall = PhysRect(19.5, 0, 0.5, 20)
surf = PhysRect(2, 4, 46, 0.05)

#max = 150
ground_height = 0

obj_posx = 3
obj_posy = 4.15
obj_radius = 0.25

ball = Sphere(obj_posx, obj_posy, obj_radius)
v_pos_x = ball.x
v_pos_y = ball.y

#ball = Cylinder(3, 4.15, 0.25)

@window.event
def on_draw():
    window.clear()
    draw_grid(1280,540,50)
    batch.draw()
    #ball.draw_velocity_vector()
    
    '''
    pyglet.text.Label(f'FPS: {int(pyglet.clock.get_frequency())}', font_name='Times New Roman', font_size=18,
                      color=(255, 255, 0, 255), x=10, y=window.height - 30).draw()'''
    
    draw_ball_speed(ball)

    shapes.Rectangle(0,ground_height,1280,1,color = (255,0,0,255)).draw()


    shapes.Circle(surf.x,surf.y,3, color = (0,0,255,255)).draw()


# Simulation data
time_velocity = {}
time_since_start = 0
next_write_time = 0

def process(delta):
    world.Step(delta, 10, 10)
    ball.update()
    
    global time_since_start, next_write_time
    time_since_start += delta
    next_write_time += delta
    if next_write_time >= 0.1:
        next_write_time = 0
        time_velocity[round(time_since_start, 2)] = round(ball.get_velocity(), 3)

    if int(ball.position[1])<= ball.radius + ground_height:
        w.can_be_unpaused = False
        w.process_going = False
        w.update_pause_btn_icon()
        w.write_vel()
        clock.unschedule(process)


clock.schedule(process)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = SimSettings()
    w.show()
    
    
    
    @window.event       
    def on_close():
        _exit(0)

    pyglet.app.run()
    sys.exit(app.exec())

