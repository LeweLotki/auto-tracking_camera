class PID:

    def __init__(self):

        self.P = -0.2
        self.I = 0
        self.D = 0.05

    def evaluate(self, input_value : dict) -> float:

        diff = self.__get_diff(input_value=input_value)
        output_value = (input_value['current']['x'] * self.P) + (diff['x'] * self.D)

        return output_value

    def __get_diff(self, input_value : dict) -> dict:

        diff = {
            'x' : input_value['current']['x'] - input_value['previous']['x'],
            'y' : input_value['current']['y'] - input_value['previous']['y']
        }

        return diff
