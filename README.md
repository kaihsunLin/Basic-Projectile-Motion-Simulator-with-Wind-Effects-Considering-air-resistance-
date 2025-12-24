# Basic Projectile Motion Simulator with Wind Effects & Air Resistance

## 1. Program Principles & Functions (程式原理與功能)

### Functions
This program is a physics simulation tool designed to compare projectile motion under different environmental conditions. It calculates and visualizes the trajectory differences between:
1.  **Ideal State**: Vacuum environment (Gravity only).
2.  **Real State**: Complex environment including **Air Density**, **Drag Coefficient**, and **Wind Velocity**.

### Physical Principles & Equations
The simulation uses **Numerical Analysis** (Time-stepping integration) to calculate position updates based on dynamic forces.

* **Gravity Force ($F_g$)**:
    $$\vec{F}_g = (0, -mg)$$
* **Air Resistance ($F_d$)**:
    The drag force depends on the square of the **relative velocity** ($v_{real}$) between the object and the air.
    $$F_d = \frac{1}{2} C_d \rho A v_{real}^2$$
* **Relative Velocity & Wind**:
    To accurately model wind effects, we calculate acceleration based on the relative speed:
    $$\vec{v}_{real} = \vec{v}_{object} - \vec{v}_{wind}$$
    $$a_{x} = \frac{-(F_d \cdot \cos\theta)}{m}, \quad a_{y} = \frac{-(F_d \cdot \sin\theta)}{m} - g$$

---

## 2. Usage (使用方式)

1.  **Install Dependencies**:
    ```bash
    pip install matplotlib
    ```
    *(Note: The code uses standard libraries `math` and `matplotlib`)*

2.  **Run the Program**:
    Execute the script in your terminal:
    ```bash
    python program.py
    ```

3.  **Input Parameters**:
    The program will prompt you to enter the following physics parameters step-by-step:
    * `Cd`: Drag coefficient (e.g., 0.47 for a sphere)
    * `D`: Air density (kg/m^3, e.g., 1.225)
    * `A`: Surface area (m^2)
    * `m`: Mass (kg)
    * `v0`: Initial velocity (m/s)
    * `ang_deg`: Launch angle (degrees)
    * `wind_speed` & `wind_dir`: Wind velocity magnitude and direction (degrees).

4.  **View Results**:
    A Matplotlib window will appear showing two curves: "Ideal State" (Blue) vs "Real State" (Orange).

---

## 3. Program Structure (程式架構)

The code is organized into functional modules to handle physics calculations and simulation logic separately:

* **`parameter_settings()`**: 
    * Handles user interaction to collect all physical properties ($C_d, \rho, A, m$) and initial conditions. Returns a dictionary of parameters.
* **`wind_xy(wind_speed, wind_dir)`**:
    * Converts scalar wind speed and direction into Vector components ($w_x, w_y$).
* **`instant_acceleration(vx, vy, wind_vx, wind_vy, params)`**:
    * **Core Physics Engine**. It calculates the **Relative Velocity** ($\vec{v} - \vec{w}$) and computes the instantaneous acceleration ($a_x, a_y$) caused by Drag and Gravity.
* **`simulate_trajectory(...)`**:
    * The main simulation loop using time-stepping ($dt = 0.01s$). It repeatedly calls `instant_acceleration` to update velocity and position until the object hits the ground ($y < 0$).
* **`plot_comparison(...)`**:
    * Uses `matplotlib.pyplot` to visualize and compare the generated trajectory lists.

---

## 4. Development Process (開發過程)

* **Phase 1: Logic Design**: Defined the necessary physical parameters (Mass, Density, Area) and structured the code using functional programming.
* **Phase 2: Physics Implementation**: Implemented the `instant_acceleration` function. **Difficulty**: Correctly decomposing the Drag Force into X and Y components based on the velocity vector. **Solution**: Used trigonometry (`vx_real / v_real`) to ensure drag always opposes the motion direction.
* **Phase 3: Wind Integration**: Added `wind_xy` to convert wind direction (degrees) into vectors. This allows the simulation to handle headwind, tailwind, or crosswind arbitrarily.

---

## 5. References (參考資料來源)

* **Physics Concepts**: *Fundamentals of Physics* (Halliday), specifically the chapters on Aerodynamic Drag and Projectile Motion.
* **Python Libraries**: 
    * Matplotlib: https://matplotlib.org/
* **AI Assistance**: 
    * **Tool**: Google Gemini.
    * **Usage**: Used LLM to debug the `instant_acceleration` logic and to format this README file to meet the term project requirements.

---

## 6. Modifications & Enhancements (程式修改或增強內容)

1.  **Detailed Environmental Physics**:
    * Unlike simple simulators that use a fixed "k" constant for drag, this program calculates drag dynamically based on **Air Density ($D$)**, **Area ($A$)**, and **Drag Coefficient ($C_d$)**. This allows users to simulate different objects (e.g., a baseball vs. a beach ball) realistically.
2.  **Vector-Based Wind System**:
    * I implemented a `wind_dir` input allowing for 360-degree wind simulation. The code automatically resolves this into X/Y components to calculate the relative air speed.
3.  **Visual Comparison**:
    * The program runs two distinct simulations (`traj_ideal` and `traj_real`) side-by-side and plots them together, providing a clear visual demonstration of how environmental factors affect flight path and range.
