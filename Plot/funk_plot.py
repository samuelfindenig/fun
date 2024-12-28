import numpy as np
import matplotlib.pyplot as plt

class FunkPlot:
    def __init__(self, x_start, x_end, increments, func, xlabel, ylabel, 
                 x_scale=None, y_scale=None, x_ticks_increment=None, y_ticks_increment=None):
        self.x_start = x_start  # Start of x values
        self.x_end = x_end      # End of x values
        self.increments = increments  # Increment step for x
        self.func = func  # Function to plot
        self.xlabel = xlabel  # Label for x-axis
        self.ylabel = ylabel  # Label for y-axis
        self.x_scale = x_scale  # Scaling for x-axis (optional)
        self.y_scale = y_scale  # Scaling for y-axis (optional)
        self.x_ticks_increment = x_ticks_increment  # Increment for x-axis ticks
        self.y_ticks_increment = y_ticks_increment  # Increment for y-axis ticks

    def x_val(self):
        return np.arange(self.x_start, self.x_end, self.increments)
    
    def y_val(self, x):
        return self.func(x)
    
    def plot(self):
        x = self.x_val()
        y = self.y_val(x)
        
        # Create plot
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x, y, color="black", linewidth=2)
        
        # Set x and y limits based on scaling arguments or automatic range
        if self.x_scale:
            ax.set_xlim(self.x_scale)
        else:
            ax.set_xlim(self.x_start, self.x_end)

        if self.y_scale:
            ax.set_ylim(self.y_scale)
        else:
            y_min, y_max = min(y), max(y)
            margin = 0.1 * (y_max - y_min) if y_max != y_min else 1
            ax.set_ylim(y_min - margin, y_max + margin)
        
        # Configure ticks
        if self.x_ticks_increment:
            x_ticks = np.arange(ax.get_xlim()[0], ax.get_xlim()[1] + self.x_ticks_increment, self.x_ticks_increment)
            ax.set_xticks(x_ticks)
        if self.y_ticks_increment:
            y_ticks = np.arange(ax.get_ylim()[0], ax.get_ylim()[1] + self.y_ticks_increment, self.y_ticks_increment)
            ax.set_yticks(y_ticks)

        # Add arrows for axes
        ax.annotate('', xy=(ax.get_xlim()[1], 0), xytext=(ax.get_xlim()[0], 0), 
                    arrowprops=dict(facecolor='black', arrowstyle='->'))
        ax.annotate('', xy=(0, ax.get_ylim()[1]), xytext=(0, ax.get_ylim()[0]), 
                    arrowprops=dict(facecolor='black', arrowstyle='->'))
        
        # Add x and y labels near arrowheads
        ax.text(ax.get_xlim()[1] * 0.98, -0.5, self.xlabel, fontsize=14, ha='right')
        ax.text(-0.5, ax.get_ylim()[1] * 0.98, self.ylabel, fontsize=14, va='top', rotation=0)
        
        # Style ticks and spines
        ax.tick_params(axis='x', direction='inout', length=10, width=1, color='black', labelsize=10)
        ax.tick_params(axis='y', direction='inout', length=6, width=1, color='black', labelsize=10)
        ax.spines['bottom'].set_visible(True)
        ax.spines['left'].set_visible(True)
        ax.spines['bottom'].set_position(('data', 0))
        ax.spines['left'].set_position(('data', 0))
        ax.spines['bottom'].set_color('black')
        ax.spines['left'].set_color('black')
        ax.spines['bottom'].set_linewidth(1)
        ax.spines['left'].set_linewidth(1)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.grid(False)

        # Show plot
        plt.show()

# Example usage:
def quadratic_function(x):
    return -3 * x**2 + 4 * x - 3

def f(x):
    return np.sin(np.deg2rad(x))

# Example with a quadratic function
plot = FunkPlot(
    x_start=-360, 
    x_end=360, 
    increments=0.1, 
    func=f, 
    xlabel="x", 
    ylabel="f(x)", 
    x_scale=[-360, 360],  # Custom x-axis range
    y_scale=[-1.5, 1.5],  # Custom y-axis range
    x_ticks_increment=180,  # Increment for x-axis ticks
    y_ticks_increment=1  # Increment for y-axis ticks
)
plot.plot()
