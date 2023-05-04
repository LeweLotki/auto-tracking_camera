class PID:

    def __init__(self):

        self.P = -0.2
        self.I = 0.01
        self.D = 0.05

    def evaluate(self, input_value : dict) -> float:

        diff_e = self.__get_diff_e(input_value=input_value)
        sum_e = self.__get_sum_e(input_value=input_value)
        output_value = (input_value['current']['x'] * self.P) + (diff_e['x'] * self.D) + (sum_e['x'] * self.I)

        return output_value

    def __get_diff_e(self, input_value : dict) -> dict:

        diff_e = {
            'x' : input_value['current']['x'] - input_value['previous']['x'],
            'y' : input_value['current']['y'] - input_value['previous']['y']
        }

        return diff_e

    def __get_sum_e(self, input_value : dict) -> dict:

        sum_e = {
             'x' : input_value['current']['x'] + input_value['previous']['x'],
             'y' : input_value['current']['y'] + input_value['previous']['y']
         }

        return sum_e
