import os
import time

def bouncing_ball(width=50, height=20, ball='⚪'):
    # Define the bouncy ball
    bouncy_ball = [
        [ball, ball, ball],
        [ball, ball, ball],
        [ball, ball, ball]
    ]
    
    # Ball's starting position (centered)
    x, y = width // 2, height // 2
    dx, dy = 1, 1
    start_time = time.time()  # Get the current time when animation starts

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen

        for j in range(height):
            for i in range(width):
                # Check if we're in the area where the ball is
                ball_found = False
                for bx in range(3):  # Iterate through 3x3 grid for ball
                    for by in range(3):
                        if x + bx == i and y + by == j:
                            print(ball, end="")
                            ball_found = True
                            break
                    if ball_found:
                        break
                if not ball_found:
                    print(" ", end="")
            print()

        # Update ball position
        x += dx
        y += dy

        # Bounce off the walls
        if x <= 0 or x >= width - 3:
            dx *= -1
        if y <= 0 or y >= height - 3:
            dy *= -1

        time.sleep(0.1)  # Slower animation

        # Stop the animation after 30 seconds
        if time.time() - start_time >= 30:
            print("\nAnimation stopped!")
            break

bouncing_ball()
