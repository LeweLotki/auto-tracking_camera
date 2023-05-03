class PID:

    def __init__(self):

        self.P = -0.2
        self.I = 0
        self.D = 1

    def evaluate(self, input_value : dict):

        output_value = input_value['x'] * self.P

        return output_value
