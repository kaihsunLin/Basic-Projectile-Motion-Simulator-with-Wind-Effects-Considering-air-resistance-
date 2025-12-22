How to Use

Install Dependencies:
Ensure Python is installed.
Install required packages if you use plotting:
pip install matplotlib numpy

Run the Program:
Execute the script using Python:
python projectile_simulator.py

Input Instructions:
Enter initial velocity and launch angle.
Enter wind speed and wind direction.
Choose whether to enable air drag.

Output:
The program prints key results and shows a trajectory plot.

Notes:
Wind is treated as a horizontal velocity effect relative to the projectile.
Air drag is optional and will be explained in the report.

Functions

Parameter Input:
Reads inputs from user, including velocity, angle, wind speed, and wind direction.
Optional inputs include gravity, time step, and drag settings.

Parameter Validation:
Checks for invalid inputs, such as negative speed, invalid angles, or non positive time step.
Prevents the simulation from running with unreasonable settings.

Initial State Setup:
Converts angle to x and y components.
Converts wind speed and direction to x and y wind components.
Builds the initial state values used in simulation.

Physics Computation:
Calculates important physical results such as:
Flight time
Maximum height
Range
If air drag is enabled, calculates motion using step by step numerical updates.

Trajectory Simulation:
Generates the position of the projectile over time.
Stops automatically when the projectile hits the ground.

Plot Creation:
Uses matplotlib to draw the projectile trajectory.
Displays key points such as start and landing location.

Program Execution:
Uses a main function to control the flow:
Read parameters
Validate parameters
Run simulation
Print results
Plot results

Development Process
Initial version:
Implemented basic projectile motion without wind.
Verified results using known physics behavior.
Wind extension:
Added wind speed and direction input.
Converted wind into x and y components.
Modified relative velocity handling so wind affects trajectory.
Optional air drag extension:
Added a toggle to enable or disable drag.
Used a simple drag model that depends on relative velocity.
Switched from closed form equations to numerical time stepping when drag is enabled.
Code organization:
All features are separated into functions.
Final execution uses:
if name == "main":
main()

Code Structure
A main
A --> B parameter_settings
A --> C validate_parameters
A --> D simulate_trajectory
D --> E compute_summary_results
A --> F plot_trajectory

Functions List
parameter_settings:
Reads user inputs and returns parameters.
validate_parameters:
Checks input ranges and prevents invalid simulations.
simulate_trajectory:
Generates time, x, y arrays based on parameters.
compute_summary_results:
Computes flight time, range, and maximum height from simulation data.
plot_trajectory:
Draws the trajectory figure.
main:
Controls the entire workflow.

References
Python documentation for basic syntax.
NumPy documentation for numerical arrays.
Matplotlib documentation for plotting.
ChatGPT for code organization suggestions and text polishing.
