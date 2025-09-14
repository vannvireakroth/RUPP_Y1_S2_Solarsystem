import turtle
import math
import random
import time

# ---------- Configuration ----------
SCREEN_W, SCREEN_H = 1000, 700
SUN_RADIUS = 50
CENTER = (0, 0)

# Bodies provided by the user (kept in the given order)
bodies = [
"vesta","pallas","hygiea","ceres","orcus","Pluto","salacia","haumea","quaoar","makemake","gongong","eris",
"Moon","Io","Europa","Ganymede","Callisto","Titan","Triton","mimas","enceladus","tethys","dions","rhea",
"lapetus","miranda","ariel","Umbriel","titania","oberon","charon"
]

# Visual tuning
MIN_ORBIT_R = 140
ORBIT_GAP = 22
MIN_SIZE = 4
MAX_SIZE = 12

random.seed(42)

# Generate orbit radius, size and angular speed for each body
body_props = []
for i, name in enumerate(bodies):
    radius = MIN_ORBIT_R + i * ORBIT_GAP
    start_angle = random.uniform(0, 360)   # random start
    speed = 0.8 / math.sqrt(1 + i*0.5)     # inner faster, outer slower
    size = int(min(MAX_SIZE, max(MIN_SIZE, random.gauss((MIN_SIZE+MAX_SIZE)/2, 2))))
    palette = ["lightgray","wheat","lightblue","plum","pink","lightgreen","khaki","orchid","salmon","gold","lightcoral","silver"]
    color = palette[i % len(palette)]
    body_props.append({
        "name": name,
        "radius": radius,
        "angle": start_angle,
        "speed": speed,
        "size": size,
        "color": color
    })

# ---------- Turtle setup ----------
screen = turtle.Screen()
screen.setup(SCREEN_W, SCREEN_H)
screen.title("Sun with many orbiting bodies")
screen.bgcolor("black")
screen.tracer(0, 0)

# Draw background stars
bg = turtle.Turtle()
bg.hideturtle()
bg.speed(0)
bg.penup()
for _ in range(260):
    x = random.randint(-SCREEN_W//2 + 10, SCREEN_W//2 - 10)
    y = random.randint(-SCREEN_H//2 + 10, SCREEN_H//2 - 10)
    bg.goto(x, y)
    bg.dot(random.randint(1, 3), "white")

# ---------- Draw the sun ----------
sun = turtle.Turtle()
sun.hideturtle()
sun.speed(0)
sun.penup()
sun.goto(0, -SUN_RADIUS)
sun.pendown()
sun.color("yellow")
sun.begin_fill()
sun.circle(SUN_RADIUS)
sun.end_fill()

# ---------- Create turtles for bodies ----------
orbiters = []
for p in body_props:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.speed(0)
    t.shape("circle")
    t.shapesize(p["size"]/5.0)
    t.color(p["color"])
    ang_rad = math.radians(p["angle"])
    x = p["radius"] * math.cos(ang_rad)
    y = p["radius"] * math.sin(ang_rad)
    t.goto(x, y)
    t.showturtle()
    orbiters.append((t, p))

# Label turtles
label_turtles = []
for t, p in orbiters:
    lt = turtle.Turtle()
    lt.hideturtle()
    lt.penup()
    lt.speed(0)
    lt.color("white")
    lt.goto(t.position()[0] + 8, t.position()[1] + 8)
    lt.write(p["name"], font=("Arial", 9, "normal"))
    label_turtles.append(lt)

# ---------- Draw orbit guides ----------
guide = turtle.Turtle()
guide.hideturtle()
guide.speed(0)
guide.penup()
guide.color("gray")
for p in body_props:
    guide.goto(0, -p["radius"])
    guide.pendown()
    guide.circle(p["radius"])
    guide.penup()

# ---------- Animation loop ----------
running = True
pause = False

def toggle_pause():
    global pause
    pause = not pause

def quit_prog():
    global running
    running = False

screen.listen()
screen.onkey(toggle_pause, "space")  # press Space to pause/unpause
screen.onkey(quit_prog, "q")         # press 'q' to quit

last_time = time.time()

try:
    while running:
        if not pause:
            now = time.time()
            dt = now - last_time
            last_time = now
            for idx, (t, p) in enumerate(orbiters):
                p["angle"] += p["speed"] * 60 * dt
                ang = math.radians(p["angle"])
                x = p["radius"] * math.cos(ang)
                y = p["radius"] * math.sin(ang)
                t.goto(x, y)
                lt = label_turtles[idx]
                lt.clear()
                lt.goto(x + 8, y + 8)
                lt.write(p["name"], font=("Arial", 9, "normal"))
        screen.update()
        time.sleep(0.02)
except turtle.Terminator:
    pass
finally:
    screen.mainloop()
