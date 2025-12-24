# Basic Projectile Motion Simulator with Wind Effects & Air Resistance

## 1. Program Principles & Functions (程式原理與功能)

### Functions
This program is a physics simulation tool designed to compare projectile motion under three different environmental conditions:
1.  **Ideal Vacuum**: Only gravity acts on the object.
2.  **Air Resistance**: Includes non-linear drag force.
3.  **Real-world Environment**: Includes both air resistance and variable wind vectors.

The program outputs a comparative plot of trajectories and calculates the **Maximum Height** and **Maximum Range** for analysis.

### Physical Principles & Equations
Instead of using simple analytical solutions, this program employs **Numerical Analysis** (Euler’s Method) to simulate forces that change dynamically with velocity.

* **Gravity Force ($F_g$)**:
    $$\vec{F}_g = (0, -mg)$$
* **Air Resistance ($F_d$)**:
    modeled using the quadratic drag equation. The force direction is opposite to the relative velocity vector.
    $$F_d = \frac{1}{2} C_d \rho A v^2$$
* **Wind Effect (Vector Math)**:
    Crucially, the drag force depends on the object's speed **relative to the air**, not the ground.
    $$\vec{v}_{relative} = \vec{v}_{object} - \vec{v}_{wind}$$
* **Numerical Integration (Time-stepping)**:
    Position and velocity are updated at every small time step ($\Delta t$):
    $$v_{x, new} = v_{x, old} + \frac{F_x}{m} \Delta t$$
    $$x_{new} = x_{old} + v_{x, new} \Delta t$$

---

## 2. Usage (使用方式)

1.  **Install Dependencies**:
    ```bash
    pip install matplotlib numpy
    ```
2.  **Run the Program**:
    Execute the main script in your terminal:
    ```bash
    python program.py
    ```
3.  **Input Parameters**:
    Follow the on-screen prompts to enter:
    * Initial Velocity (m/s)
    * Launch Angle (degrees)
    * Wind Speed X & Y components (m/s)
4.  **View Results**:
    A window will pop up showing the trajectory comparison. Close the window to end the program or re-run to test new values.

---

## 3. Program Structure (程式架構)

The code structure directly implements the physics principles described in Section 1:

* **`class Projectile`**: The main object representing the particle.
    * *Properties*: Stores mass ($m$), area ($A$), position ($x, y$), and velocity ($v_x, v_y$).
* **`def calculate_drag(self, wind_speed)`**: 
    * **Corresponds to**: The Drag Equation & Wind Vector Math.
    * Calculates relative velocity and returns the drag force components ($F_{d,x}, F_{d,y}$).
* **`def update_position(self, dt)`**:
    * **Corresponds to**: Numerical Integration (Euler's Method).
    * Updates velocity based on net force ($F_g + F_d$) and updates position based on velocity.
* **`def simulate(...)`**: 
    * The main loop that iterates time steps until the projectile hits the ground ($y < 0$).

---

## 4. Development Process (開發過程)

* **Phase 1: Foundation**: Started by writing a basic script for vacuum projectile motion to verify the physics engine against known parabolic equations ($R = v^2 \sin(2\theta)/g$).
* **Phase 2: Adding Drag**: Introduced the drag formula. **Difficulty**: The projectile flew backwards when $v_y$ became negative because I initially calculated drag direction incorrectly. **Solution**: I fixed this by using vector decomposition ($\cos \theta, \sin \theta$) derived from the velocity vector angle.
* **Phase 3: Wind Implementation**: **Difficulty**: Simply adding wind speed to the object's velocity produced wrong physics. **Solution**: realized that wind modifies the *relative air speed*, which then dictates the drag force magnitude and direction. Implemented the vector subtraction logic ($\vec{v}_{rel} = \vec{v}_{obj} - \vec{v}_{wind}$).

---

## 5. References (參考資料來源)

* **Physics Concepts**: Halliday, Resnick, Walker, *Fundamentals of Physics*, Chapter on Projectile Motion and Drag Forces.
* **Coding Libraries**: 
    * Matplotlib Documentation: https://matplotlib.org/
    * NumPy Documentation: https://numpy.org/
* **AI Assistance**: 
    * **Tool**: Google Gemini / ChatGPT.
    * **Usage**: Used LLM to debug the "Relative Velocity" sign errors, generate the initial plot styling code, and assist in formatting this README structure.

---

## 6. Modifications & Enhancements (程式修改或增強內容)

Unlike many basic online tutorials that strictly simulate 1D drag or vacuum motion, my contributions include:

1.  **2D Wind Vector Implementation**:
    * I manually implemented the logic to handle wind coming from any direction (X and Y components), allowing for the simulation of headwind, tailwind, and crosswind (lift/drop) effects.
2.  **Comparative Visualization**:
    * Modified the plotting logic to overlay three distinct curves (Vacuum / Drag / Drag+Wind) on a single chart. This makes it visually intuitive to understand "how much" distance is lost due to air resistance and wind.
3.  **User Interactivity**:
    * Enhanced the script from a static calculation to an interactive tool where users can experiment with different angles and wind speeds without editing the code.


