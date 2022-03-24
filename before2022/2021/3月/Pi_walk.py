class PIWalk():
    """A class to generate random walks."""

    def __init__(self, num_points=500):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]
    def fill_walk(self):

        pi = open('pi_million_digits.txt','r')
        S = pi.read().split()
        middle = []
        final = []
        for i in S:
            l = list(str(i))
            middle += (l)
        for i in middle:
            m = int(i)
            final.append(m)

        x_direction = [1, 0, -1, 0]
        y_direction = [0, 1, 0, -1]
        for n in range(0,self.num_points-1):
            x_step = final[n] * x_direction[n % 4]
            y_step = final[n] * y_direction[n % 4]
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

