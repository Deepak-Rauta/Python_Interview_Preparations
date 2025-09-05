# # random_art.py
# import turtle
# import random

# # Setup screen
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.title("🎨 Random Art Drawer")

# # Setup turtle
# artist = turtle.Turtle()
# artist.speed(0)  # fastest drawing speed
# colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink", "white"]

# # Draw random spirograph-style art
# def draw_random_art():
#     artist.pensize(2)
#     for _ in range(200):  # number of shapes
#         artist.color(random.choice(colors))
#         artist.circle(random.randint(20, 100))
#         artist.left(random.randint(10, 60))
#         artist.forward(random.randint(10, 50))

# # Run
# draw_random_art()
# artist.hideturtle()

# # Keep window open until user clicks
# screen.exitonclick()


# abstract_art.py
import matplotlib.pyplot as plt
import numpy as np
import random

def generate_art():
    plt.figure(figsize=(8, 8))
    plt.axis("off")  # Hide axis
    
    # Generate random shapes
    for _ in range(50):  # number of shapes
        shape_type = random.choice(["circle", "rectangle", "polygon"])
        color = np.random.rand(3,)  # random RGB color
        alpha = random.uniform(0.3, 0.8)  # transparency
        
        if shape_type == "circle":
            x, y = np.random.rand(2)
            radius = random.uniform(0.05, 0.2)
            circle = plt.Circle((x, y), radius, color=color, alpha=alpha)
            plt.gca().add_patch(circle)
        
        elif shape_type == "rectangle":
            x, y = np.random.rand(2)
            w, h = np.random.rand(2) * 0.2
            rect = plt.Rectangle((x, y), w, h, color=color, alpha=alpha)
            plt.gca().add_patch(rect)
        
        else:  # polygon
            points = np.random.rand(random.randint(3, 6), 2)
            polygon = plt.Polygon(points, closed=True, color=color, alpha=alpha)
            plt.gca().add_patch(polygon)

    # Show art
    plt.show()

# Run
generate_art()


