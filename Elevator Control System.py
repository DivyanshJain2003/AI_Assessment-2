#Python code for elevator control system

!pip install scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

distance = ctrl.Antecedent(np.arange(0, 4, 1), 'distance')
elevator_position = ctrl.Consequent(np.arange(0, 4, 1), 'elevator_position')

distance['close'] = fuzz.trimf(distance.universe, [0, 0, 2])
distance['medium'] = fuzz.trimf(distance.universe, [0, 2, 4])
distance['far'] = fuzz.trimf(distance.universe, [2, 4, 4])

elevator_position['first_floor'] = fuzz.trimf(elevator_position.universe, [0, 0, 2])
elevator_position['second_floor'] = fuzz.trimf(elevator_position.universe, [0, 2, 4])
elevator_position['third_floor'] = fuzz.trimf(elevator_position.universe, [2, 4, 4])

rule1 = ctrl.Rule(distance['close'], elevator_position['first_floor'])
rule2 = ctrl.Rule(distance['medium'], elevator_position['second_floor'])
rule3 = ctrl.Rule(distance['far'], elevator_position['third_floor'])

elevator_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
elevator_simulation = ctrl.ControlSystemSimulation(elevator_ctrl)

# Take input from the user for distance to the elevator
user_distance = float(input("Enter the distance to the elevator (0-4): "))
elevator_simulation.input['distance'] = user_distance
elevator_simulation.compute()

print("Position of the elevator:", elevator_simulation.output['elevator_position'])
