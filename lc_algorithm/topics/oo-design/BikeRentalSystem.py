"""
Bike Rental System:

  - Bike
    - Small, Medium, Large
  - Scotter
    - Gas, Electrical

VehicleCatgory: BIKE, SCOTTER, TRI_CYCLE
OrderStatus: PLACED, ACTIVE, COMPLETED, CANCELLED
BikeSize: SMALL, MEDIUM, LARGE
ScotterType: GAS, ELECTRICAL

Bike: id, size, color
Scotter: id, type, single_wheel
VehicleUnitPrice: vehicle_id, cost_per_unit
Inventory: id, vehicle_catogory, vehicle_id(Bike->id, Scotter->id), units
           1  , BIKE, 1 (1, small, green), 50
           2  , BIKE, 2 (2, small, red), 30
           2  , SCOTTER, 1 (1, electrical, true), 60 
Order: id, customer_id, order_status, star_time, end_time
VehicleOrder: order_id, inventory_id, unit, cost
Customer: id, name, email
"""
