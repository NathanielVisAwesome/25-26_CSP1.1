# undertale_hearts.py
# Animated Undertale-style hearts using turtle
# Run with: python undertale_hearts.py

import turtle
import math
import random
import time

SCREEN_W, SCREEN_H = 800, 600
FPS = 30
DT_MS = int(1000 / FPS)

# Parametric heart shape generator (returns list of points)
def heart_points(scale=1.0, steps=80):
    pts = []
    for i in range(steps + 1):
        t = math.pi * 2 * i / steps
        # Parametric heart (classic)
        x = 16 * math.sin(t) ** 3
        y = 13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t)
        pts.append((x * scale, y * scale))
    return pts

# Draw heart at (cx, cy) with given scale and color using a given turtle instance
def draw_heart(t: turtle.Turtle, cx, cy, scale, color, heading=0):
    t.clear()
    t.penup()
    pts = heart_points(scale=scale, steps=100)
    # Move to first point (rotated + translated)
    cosh = math.cos(math.radians(heading))
    sinh = math.sin(math.radians(heading))
    def rot(x, y):
        rx = x * cosh - y * sinh
        ry = x * sinh + y * cosh
        return rx, ry

    first_x, first_y = rot(pts[0][0], pts[0][1])
    t.goto(cx + first_x, cy + first_y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for (x, y) in pts[1:]:
        rx, ry = rot(x, y)
        t.goto(cx + rx, cy + ry)
    t.goto(cx + first_x, cy + first_y)
    t.end_fill()
    t.penup()

class Heart:
    def __init__(self, screen, color, x, y, scale, vx, vy, wobble_speed, spin_speed):
        self.t = turtle.Turtle(visible=False)
        self.t.hideturtle()
        self.t.speed(0)
        self.t.penup()
        self.color = color
        self.x = x
        self.y = y
        self.base_scale = scale
        self.scale = scale
        self.vx = vx
        self.vy = vy
        self.wobble_speed = wobble_speed
        self.spin_speed = spin_speed
        self.phase = random.random() * 2 * math.pi
        self.heading = random.uniform(-10, 10)

    def update(self, dt):
        # Movement
        self.x += self.vx * dt
        self.y += self.vy * dt

        # Bounce on edges (wrap-around horizontally, bounce vertically a bit)
        if self.x < -SCREEN_W//2 - 50:
            self.x = SCREEN_W//2 + 50
        if self.x > SCREEN_W//2 + 50:
            self.x = -SCREEN_W//2 - 50
        if self.y < -SCREEN_H//2 + 30:
            self.y = -SCREEN_H//2 + 30
            self.vy = abs(self.vy)
        if self.y > SCREEN_H//2 - 30:
            self.y = SCREEN_H//2 - 30
            self.vy = -abs(self.vy)

        # Pulse / bob
        self.phase += self.wobble_speed * dt
        pulse = 0.08 * math.sin(self.phase * 2.0)  # small pulse amplitude
        self.scale = self.base_scale * (1 + pulse)

        # Spin slowly
        self.heading += self.spin_speed * dt

    def draw(self):
        draw_heart(self.t, self.x, self.y, self.scale, self.color, heading=self.heading)

def make_scene():
    screen = turtle.Screen()
    screen.setup(SCREEN_W, SCREEN_H)
    screen.title("Undertale hearts — turtle animation")
    screen.bgcolor("black")
    screen.tracer(0, 0)  # turn off automatic updates

    # Colors reminiscent of Undertale soul colors (red + others)
    colors = [
        "#FF2D55",  # red-ish
        "#007AFF",  # blue
        "#FF9500",  # orange
        "#34C759",  # green
        "#FFD60A",  # yellow
        "#AF52DE",  # purple
    ]

    hearts = []
    for i in range(6):
        x = random.uniform(-SCREEN_W//4, SCREEN_W//4)
        y = random.uniform(-SCREEN_H//6, SCREEN_H//3)
        scale = random.uniform(6, 10)  # scale multiplier for parametric heart
        vx = random.uniform(-30, 30) / FPS  # per-frame velocity reference; will be multiplied by dt
        vy = random.uniform(-8, 8) / FPS
        wobble_speed = random.uniform(2.0, 4.0)
        spin_speed = random.uniform(-30, 30) / FPS
        h = Heart(screen, colors[i % len(colors)], x, y, scale, vx * FPS, vy * FPS, wobble_speed, spin_speed * FPS)
        hearts.append(h)

    # central "player" red heart larger and in middle
    player = Heart(screen, "#FF2D55", 0, -40, 14, 0, 0, 3.5, 0)
    hearts.append(player)

    # small overlay label (static text) using a separate turtle
    label = turtle.Turtle(visible=False)
    label.hideturtle()
    label.penup()
    label.color("white")
    label.goto(0, SCREEN_H//2 - 60)
    label.write("UNDERTALE HEARTS MEME (turtle)", align="center", font=("Arial", 18, "bold"))
    label.goto(0, -SCREEN_H//2 + 20)
    label.write("Press ESC to quit", align="center", font=("Arial", 10, "normal"))

    last = time.time()

    def loop():
        nonlocal last
        now = time.time()
        dt = now - last
        # clamp dt for stability
        if dt > 0.1:
            dt = 0.1
        last = now

        for h in hearts:
            h.update(dt)
            h.draw()

        screen.update()
        screen.ontimer(loop, DT_MS)

    # exit binding
    def quitprog():
        screen.bye()

    screen.onkey(quitprog, "Escape")
    screen.listen()

    loop()
    screen.mainloop()

if __name__ == "__main__":
    make_scene()
