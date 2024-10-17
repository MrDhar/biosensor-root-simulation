import numpy as np
import matplotlib.pyplot as plt

# Function to simulate the shape of roots based on random growth patterns
def generate_root_structure(depth, spread, num_roots=5):
    x_vals = []
    y_vals = []
    
    for _ in range(num_roots):
        # Random growth pattern for each root
        x = [0]  # Roots start from the center (x = 0)
        y = [0]  # Start at the surface (y = 0)
        
        for _ in range(depth):
            # Random horizontal spread and downward growth
            x.append(x[-1] + np.random.uniform(-spread, spread))
            y.append(y[-1] - np.random.uniform(0.5, 1.5))  # Roots grow downwards
            
        x_vals.append(x)
        y_vals.append(y)
    
    return x_vals, y_vals

# Function to plot root structure
def plot_root_structure(depth, spread, num_roots=5):
    x_vals, y_vals = generate_root_structure(depth, spread, num_roots)
    plt.figure(figsize=(6, 8))
    for x, y in zip(x_vals, y_vals):
        plt.plot(x, y)

    plt.gca().invert_yaxis()  # Invert y-axis to make roots grow downward
    plt.title('Simulated Root Structure')
    plt.xlabel('Horizontal Spread')
    plt.ylabel('Depth')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    # You can adjust the depth, spread, and number of roots as needed
    plot_root_structure(depth=20, spread=2, num_roots=10)
