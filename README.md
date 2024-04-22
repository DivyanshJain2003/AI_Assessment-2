Importing Libraries:
numpy is imported as np for numerical computations.
skfuzzy is imported for fuzzy logic operations.
control module from skfuzzy is imported to define fuzzy control systems.

Defining Fuzzy Variables:
distance is defined as an Antecedent representing the distance to the elevator, ranging from 0 to 4 units.
elevator_position is defined as a Consequent representing the position of the elevator, also ranging from 0 to 4 units.
Fuzzy membership functions are defined for both variables using triangular membership functions (trimf).

Defining Fuzzy Rules:
Three fuzzy rules are defined to map the distance to the elevator to its position.
For example, if the distance is 'close', the elevator's position is set to 'first_floor'.

Creating Fuzzy Control System:
A fuzzy control system is created using the defined rules.
The control system contains the rules for determining the elevator position based on the distance input.

Setting Input and Computing Output:
The user is prompted to enter the distance to the elevator (0-4 units).
The user input is then assigned to the input variable of the fuzzy control system.
The output position of the elevator is computed using the fuzzy control system.

Displaying Output:
The position of the elevator computed by the fuzzy control system is printed to the console.






