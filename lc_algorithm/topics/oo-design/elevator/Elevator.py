"""
We can divide into three main components:

User

User:
1. presses the floor button (can be up or down direction) to summon the
elevator. 
2. User presses the elevator button to go to the destination floor.

Button: 

1. An elevator has buttons (ElevatorButton) inside allowing user to choose the
destination floor. 
2. Each floor has two buttons (FloorButton) to summon the
elevator to go up or down from that floor. 
3. When the user presses the button, it
illuminates. When the elevator reaches the desired floor, the button stops
illuminating. 
4. Calls placeRequest() to insert into the ElevatorRequest queue when
button is pressed. 

Elevator:

1. Open or close door. 
2. Moves up/down. 
3. Stores states such as direction (up/down), speed, currentFloor. 

We need a queue to store all request, this can all be
encapsulated in an ElevatorRequests class. When a user presses a button, this
request has to be served and is added to the processing queue. Elevator requests
can be scheduled using different scheduling algorithms. ElevatorController
controls the elevator by giving it instructions such as move up/down, or
start/shutdown. The elevator controller reads the next elevator request and
serves it.

This diagram may help :)


"""