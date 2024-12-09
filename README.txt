Hand-Tracking Game

Project Description

The **Hand-Tracking Game** is an interactive and engaging project that utilizes **MediaPipe** and **OpenCV** to demonstrate real-time hand gesture control. The game allows players to control a circular object on the screen using hand movements detected via a webcam. The objective of the game is to collide the circular object with a target, which relocates to a random position after each successful interaction.

This project highlights the potential of gesture-based interfaces by integrating computer vision techniques with game mechanics. It is lightweight, accessible, and does not require any specialized hardware, making it suitable for a wide range of users. With its modular design, the project is ideal for developers, educators, and researchers exploring real-time interaction systems.

Features

- **Real-Time Hand Tracking:** Uses MediaPipe to detect and track hand landmarks with high accuracy.
- **Interactive Gameplay:** Dynamic target relocation and smooth gesture-based controls make the game engaging and fun.
- **Lightweight and Accessible:** Requires only a standard webcam and runs efficiently on most systems.
- **Educational Value:** Demonstrates the integration of computer vision and human-computer interaction in an easy-to-understand format.
- **Applications Beyond Gaming:** Potential use cases include education, physical therapy, and gesture-based control systems.

How It Works

1. **Hand Tracking:** The system uses MediaPipe to detect and track the player's hand through a live webcam feed.
2. **Game Mechanics:** The detected hand movements are mapped to control a circle on the screen, allowing it to interact with a randomly placed target.
3. **Collision Detection:** When the circle collides with the target, the target relocates to a new position, creating a dynamic challenge for the player.

Requirements

- Python 3.x
- OpenCV
- MediaPipe
- Pygame

Installation

1. Clone the repository
2. Install dependencies:pip install -r requirements.txt
3. Run the game

## Future Enhancements

- Adding support for multi-hand tracking.
- Incorporating more complex gestures for enhanced gameplay.
- Integrating sound effects and scoring systems.
- Expanding compatibility for AR/VR environments.




