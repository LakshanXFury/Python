from turtle import Turtle, Screen
from spaceship import SpaceShip
from bullets import Bullet
from enemy import Enemy

screen = Screen()
bullets = []
score = 0

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Space Invaders")
screen.tracer(0)

ship = SpaceShip((0, -250))  # centered near the bottom

screen.listen()
screen.onkey(ship.move_left, "Left")
screen.onkey(ship.move_right, "Right")


def fire_bullet():
    bullet = Bullet((ship.xcor(), ship.ycor() + 10))
    bullets.append(bullet)


screen.onkey(fire_bullet, "space")

enemies = []          # List to store all the enemy objects
rows = 4              # Number of horizontal lines of enemies
cols = 10             # Number of enemies in each row
start_x = -350        # X coordinate of the first enemy on the left
start_y = 200         # Y coordinate of the first enemy (top row)
spacing_x = 70        # Horizontal space between enemies
spacing_y = 50        # Vertical space between rows

for row in range(rows):         # Outer loop for rows (0 to 3)
    for col in range(cols):     # Inner loop for columns (0 to 9)
        x = start_x + col * spacing_x    # Calculate X position
        y = start_y - row * spacing_y    # Calculate Y position
        enemy = Enemy((x, y))            # Create a new enemy at (x, y)
        enemies.append(enemy)           # Add to the list


def check_collisions():
    global score
    for bullet in bullets:
        for enemy in enemies:
            if bullet.distance(enemy) < 20:
                # Same for Bullet
                bullet.hideturtle()
                bullets.remove(bullet)
                enemy.hideturtle()  # visually hides the enemy from screen.
                enemies.remove(enemy)  # removes it from the enemy list, so it doesn’t move anymore.
                score += 1
                print(f"Score: {score}")
                return  # Avoid crash after list change


while True:
    screen.update()
    for bullet in bullets:
        bullet.move()

    for enemy in enemies:
        enemy.move()

    check_collisions()

screen.exitonclick()
