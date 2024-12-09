import cv2
import mediapipe as mp
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hand Tracking Game")

# Define the game circle and target
circle_radius = 30
circle_color = (255, 0, 0)

# Set the circle's initial position
circle_x, circle_y = WIDTH // 2, HEIGHT // 2

# Define the target position
target_radius = 20
target_color = (0, 255, 0)

# Set a random target position
target_x, target_y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)

# Set up the clock to control the frame rate
clock = pygame.time.Clock()

# Initialize MediaPipe for hand tracking
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# For drawing landmarks
mp_drawing = mp.solutions.drawing_utils

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Main game loop
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally (for mirror effect)
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB for MediaPipe processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame to detect hands
    results = hands.process(rgb_frame)
    
    # If hands are detected, use the landmarks
    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Get the position of the index finger (landmark 8)
            x = int(landmarks.landmark[8].x * WIDTH)
            y = int(landmarks.landmark[8].y * HEIGHT)

            # Move the circle based on the finger position
            circle_x, circle_y = x, y

    # Check if the circle collides with the target
    distance = ((circle_x - target_x) ** 2 + (circle_y - target_y) ** 2) ** 0.5
    if distance < circle_radius + target_radius:
        target_x, target_y = random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50)

    # Convert the OpenCV frame to a format suitable for Pygame
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = pygame.surfarray.make_surface(frame)
    frame = pygame.transform.rotate(frame, -90)
    frame = pygame.transform.flip(frame, True, False)

    # Draw the video frame as the background
    screen.blit(frame, (0, 0))

    # Draw the target
    pygame.draw.circle(screen, target_color, (target_x, target_y), target_radius)

    # Draw the circle controlled by the hand
    pygame.draw.circle(screen, circle_color, (circle_x, circle_y), circle_radius)

    # Update the Pygame window
    pygame.display.update()

    # Handle quitting the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cap.release()
            cv2.destroyAllWindows()
            pygame.quit()
            exit()

    # Control the frame rate
    clock.tick(30)
