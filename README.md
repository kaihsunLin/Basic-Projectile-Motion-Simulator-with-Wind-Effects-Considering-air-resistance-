# Basic Projectile Motion Simulator with Wind Effects & Air Resistance

This project is a Python-based physics simulation designed to model projectile motion in realistic environments. Unlike standard textbook examples that assume a vacuum, this simulator accounts for **non-linear air resistance** and **variable wind effects**, providing a comparative visualization of different flight trajectories.

## 1. Features & Technical Principles

### Features
* **Multi-Scenario Simulation**: Simultaneously simulates and plots three scenarios:
    1.  Ideal Motion (Vacuum, Gravity only).
    2.  Air Resistance (Drag force included).
    3.  Real-world Environment (Air Resistance + Wind Speed).
* **Customizable Inputs**: Users can define initial velocity, launch angle, wind speed (vector), mass, and drag coefficient.
* **Data Analysis**: Automatically calculates and outputs the Maximum Height and Maximum Range for each scenario.

### Technical Principles
The simulation avoids simple analytical solutions and instead uses **Numerical Analysis** (Time-stepping method):
* **Gravity**: $F_g = mg$ (Downwards).
* **Air Resistance**: Modeled using the drag equation $F_d = \frac{1}{2} \rho v^2 C_d A$. The force acts opposite to the velocity vector.
* **Wind Effect**: The drag force is calculated based on the **relative velocity** between the object and the air, not just the ground speed:
    $$\vec{v}_{relative} = \vec{v}_{object} - \vec{v}_{wind}$$

## 2. How to Use

1.  **Install Dependencies:**
    Ensure Python 3.x is installed on your system.
    Install the required libraries (`matplotlib` and `numpy`) using the command:
    ```bash
    pip install matplotlib numpy
    ```

2.  **Setup:**
    Ensure the main script file (`program.py`) is located in your current working directory.
    No additional assets (images or sounds) are required for this physics simulation.

3.  **Run the Simulation:**
    Execute the script using Python via your terminal:
    ```bash
    python program.py
    ```

4.  **Simulation Instructions:**
    * The program will prompt you to enter parameters in the terminal.
    * **Velocity**: Enter initial speed (e.g., `50`).
    * **Angle**: Enter launch angle in degrees (e.g., `45`).
    * **Wind**: Enter wind speed components (e.g., `10` for tailwind, `-5` for headwind).
    * After inputs, a Matplotlib window will open displaying the comparative trajectories.

5.  **Replay / Exit:**
    * Close the graph window to end the current session.
    * To simulate a new set of parameters, simply run the command `python program.py` again.

## 3. Program Structure

The code is organized into a modular structure for clarity:
* **`class Projectile`**: Represents the flying object. Stores state variables like position `(x, y)`, velocity `(vx, vy)`, and physical properties (mass, area).
* **`update_position(dt)`**: The core physics engine. It calculates net forces (Gravity + Drag) and updates velocity and position using numerical integration.
* **`calculate_drag(wind_velocity)`**: A helper function that computes drag force based on relative air speed.
* **`simulate()`**: The main loop that runs the time-steps until the projectile hits the ground ($y < 0$).
* **`plot_results()`**: Handles data visualization using `matplotlib.pyplot`.

## 4. Development Process

1.  **Ideation**: The goal was to extend basic physics class concepts by adding "real-world" factors often ignored in introductory problems.
2.  **Core Physics**: Implemented a basic gravity-only model first to verify the parabolic path.
3.  **Adding Drag**: Integrated the air resistance formula. Encountered challenges with vector direction; resolved by decomposing velocity into X and Y components.
4.  **Implementing Wind**: Added wind velocity vectors. This required a significant logic change to calculate drag based on *relative* velocity rather than absolute velocity.
5.  **Visualization**: Finalized the Matplotlib output to show all three curves (Ideal, Drag, Drag+Wind) on one chart for easy comparison.

## 5. References & Modifications

### References
* **Physics Equations**: Halliday, Resnick, Walker, *Fundamentals of Physics* (Chapters on Projectile Motion and Drag Forces).
* **Python Libraries**: Official documentation for [Matplotlib](https://matplotlib.org/) and [NumPy](https://numpy.org/).

### Modifications & AI Usage
* **Originality**: While the basic Euler method loop is standard, the specific implementation of **vector-based wind addition** was developed for this project.
* **AI Assistance**: LLM tools (ChatGPT/Gemini) were used to debug the relative velocity sign errors and to format this README file. (See attached conversation logs in the report for details).
