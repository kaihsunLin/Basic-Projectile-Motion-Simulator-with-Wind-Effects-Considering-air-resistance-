import math
import matplotlib.pyplot as plt


def parameter_settings() :
    Cd = float(input("drag coefficient of  the obgect = "))
    D = float(input("dansity of  the air = "))
    A = float(input("surface area of  the obgect = "))
    m = float(input("mass of  the obgect = "))
    v0 = float(input("initial velocity (m/s) = "))
    ang_deg = float(input("Launch angle (deg) = "))
    wind_speed = float(input("wind speed (m/s) = "))
    wind_dir = float(input("wind direction (deg, from +x CCW) = "))
    params = {
        "Cd":Cd,
        "D":D,
        "A":A,
        "m":m,
        "v0": v0,
        "ang_deg": ang_deg,
        "wind_speed": wind_speed,
        "wind_dir": wind_dir,
    }
    return params

def validate_parameters(Cd,D,A,m,v0, ang_deg, wind_speed, g, dt) :
    if Cd <= 0 :
        raise ValueError("drag coefficient of  the obgect must be > 0")
    if D <= 0 :
        raise ValueError("density of  the obgect must be > 0")
    if A <= 0 :
        raise ValueError("surface area of  the obgect must be > 0")
    if m <= 0 :
        raise ValueError("mass of the object must be > 0")
    if v0 <= 0 :
        raise ValueError("initial velocity must be > 0")
    if ang_deg >= 90 or ang_deg <= 0 :
        raise ValueError("Launch angle should be between 0 and 90 degrees for this project")
    if wind_speed < 0 :
        raise ValueError("wind speed must be >= 0")
    if g <= 0 :
        raise ValueError("g must be > 0")
    if dt <= 0 :
        raise ValueError("dt must be > 0")
    pass
    
def deg_tran(deg):
    return deg * math.pi / 180.0
    
def wind_xy(wind_speed, wind_dir) :
    theta = deg_tran(wind_dir % 360.0)
    wx = wind_speed * math.cos(theta)
    wy = wind_speed * math.sin(theta)
    return wx, wy

def velocity(v0, ang_deg):
    theta = deg_tran(ang_deg)
    vx = v0 * math.cos(theta)
    vy = v0 * math.sin(theta)
    return vx, vy

def instant_acceleration(vx, vy, wind_vx, wind_vy, params) :
    g = 9.81
    if params is None:
        return 0, -g
    D = params["D"]
    Cd = params["Cd"]
    A = params["A"]
    m = params["m"]
    vx_real = vx - wind_vx
    vy_real = vy - wind_vy
    v_real = math.sqrt(vx_real ** 2 + vy_real ** 2)
    if v_real == 0:
        return 0, -g
    Fd = 0.5 * D * v_real **2 * Cd * A
    Fd_x = - Fd * vx_real / v_real
    Fd_y = - Fd * vy_real / v_real
    ax = Fd_x / m
    ay = Fd_y / m - g
    return ax, ay

def simulate_trajectory(v0, ang_deg,wind_vx, wind_vy, params) :
    t = 0
    dt = 0.01 
    x, y = 0, 0
    vx, vy = velocity(v0, ang_deg)
    trajectory = []

    while y >= 0:
        trajectory.append((x, y))
        ax, ay = instant_acceleration(vx, vy, wind_vx, wind_vy, params)
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt
        t += dt
    return trajectory

def plot_comparison(trajectory_list, labels):
    plt.figure(figsize=(10, 6)) 
    for i, traj in enumerate(trajectory_list):
        xs, ys = zip(*traj)
        plt.plot(xs, ys, label=labels[i])
    plt.title("Projectile Motion Comparison (with Wind & Drag)")
    plt.xlabel("Distance x (m)")
    plt.ylabel("Height y (m)")
    plt.axhline(0, color='black', linewidth=1) 
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.ylim(bottom=-0.05 * max(max(y for x, y in traj) for traj in trajectory_list))
    plt.show()

def main():
    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    plt.rcParams['axes.unicode_minus'] = False
    print("=== 拋體運動模擬器 (含空氣阻力) ===")
    data = parameter_settings()
    ang_deg = data["ang_deg"]
    theta = deg_tran(ang_deg)
    wx, wy = wind_xy(data['wind_speed'], data['wind_dir'])
    traj_ideal = simulate_trajectory(data['v0'], data['ang_deg'], 0, 0, None)
    traj_real = simulate_trajectory(data['v0'], data['ang_deg'], wx, wy, data)
    plot_comparison([traj_ideal, traj_real], ["理想狀態 (無阻力)", "真實狀態 (有風/有阻力)"])

if __name__ == "__main__":
    main()