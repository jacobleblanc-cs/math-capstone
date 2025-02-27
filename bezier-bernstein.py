import numpy as np
    import matplotlib.pyplot as plt
    from scipy.special import comb

    def Bézier_curve(control_points, num_points):
        n = len(control_points) - 1
        t = np.linspace(0, 1, num_points)
        curve = np.zeros((num_points, 2))

        for i in range(num_points):
            x_coord = 0
            y_coord = 0
            for k in range(n + 1):
                x_coord += comb(n, k) * (1 - t[i])**(n - k) * t[i]**k * control_points[k][0]
                y_coord += comb(n, k) * (1 - t[i])**(n - k) * t[i]**k * control_points[k][1]
            curve[i] = [x_coord, y_coord]
    
        return curve

    def plot_Bézier_curve(control_points, curve_points):
        plt.plot(control_points[:,0], control_points[:,1], 'bo-', label='Control Points',
                 linestyle='None')
        plt.plot(curve_points[:,0], curve_points[:,1], 'r-', label='Bézier Curve')
        plt.title('Bézier Curve')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
        plt.axis('equal')
        plt.show()
