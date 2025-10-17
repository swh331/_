import turtle
import random
import math
import time

# 화면 생성
s = turtle.Screen()
s.setup(800, 600)
s.tracer(0)
s.bgcolor("black")

# 거울 개수 입력
def confirmation():
    ans = s.textinput("거울 개수 입력", "")
    try:
        ans = float(ans)
    except:
        return confirmation()
    if ans < 0 or ans % 1 != 0:
        return confirmation()
    return int(ans)

num = confirmation()
mirrors = []

# 거울 그리기 + 거울 위치 저장
def mirror(x, y, angle, length, color):
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color(color)
    t.pensize(5)
    t.up()
    t.goto(x, y)
    t.setheading(angle)
    t.down()
    t.forward(length / 2)
    t.backward(length)
    t.up()
    t.goto(x, y)
    mirrors.append((x, y, angle, length))
    s.update()
    #광원 그리기
    t.goto(0,0)
    t.color("red")
    t.dot(12)

# 테두리 거울 그리기
mirror(0, 300, 0, 800, "gray")
mirror(0, -300, 0, 800, "gray")
mirror(-400, 0, 90, 600, "gray")
mirror(400, 0, 90, 600, "gray")


# 작은 거울 그리기
for i in range(num):
    x = random.randint(-350, 350)
    y = random.randint(-250, 250)
    angle = random.choice([0, 20, 40, 60, 80, 100, 120, 140, 160])
    mirror(x, y, angle, 100, "white")

# 광선
ray = turtle.Turtle()
ray.hideturtle()
ray.color("red")
ray.pensize(2)
ray.speed(0)
ray.up()
ray.goto(0, 0)
ray.setheading(random.uniform(0, 360))
ray.down()

# 반사
def reflect(inc_ang, mirror_ang):
    return (2 * mirror_ang - inc_ang) % 360

# 광선 방출
while True:
    ray.forward(3)
    x, y = ray.pos()
    
    # 거울 감지
    for mx, my, ang, length in mirrors:
        dx = x - mx
        dy = y - my
        dist = abs(dx * math.sin(math.radians(ang)) - dy * math.cos(math.radians(ang)))
        if dist < 3 and abs(dx * math.cos(math.radians(ang)) + dy * math.sin(math.radians(ang))) < length / 2:
            ref_ang = reflect(ray.heading(), ang)
            ray.setheading(ref_ang)
            break
    s.update()
    time.sleep(0.004)
