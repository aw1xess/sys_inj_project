class Person:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']

class Pilot(Person):
    def __init__(self, **kwargs):
        self.pilot_license = kwargs['pilot_license']
        super().__init__(**kwargs)

class Passenger(Person):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class FuelInjectonSystem:
    def __init__(self):
        self.nozzles_state = "Fuel nozzles closed"
    def start_fuelInjection(self):
        self.nozzles_state = "Fuel nozzles open"
        print(self.nozzles_state)
    def stop_fuelInjection(self):
        self.nozzles_state = "Fuel nozzles closed"
        print(self.nozzles_state)

class Engine:
    def __init__(self):
        self.turbine_state = "Turbine turned off"
        self.traction_state = "none" # тяга
    def start_engine(self):
        self.turbine_state = "Turbine turned on"
        print(self.turbine_state)
    def stop_engine(self):
        self.turbine_state = "Turbine turned off"
        print(self.turbine_state)
    def increase_traction(self):
        self.traction_state = "Traction increased"
        print(self.traction_state)
    def decrease_traction(self):
        self.traction_state = "Traction decreased"
        print(self.traction_state)

class Fuselage:
    def __init__(self):
        self.cargo_state = "Cargo deloaded"
    def load_cargo(self):
        self.cargo_state = "Cargo loaded"
        print(self.cargo_state)
    def deload_cargo(self):
        self.cargo_state = "Cargo deloaded"
        print(self.cargo_state)

class Wing:
    def __init__(self):
        self.flaps_state = "Flaps hidden"  
        self.ailerons_state = "Ailerons not inclined" # літак повертається вокруг своєї вісі
    def release_flaps(self):
        self.flaps_state = "Flaps released"
        print(self.flaps_state)
    def hide_flaps(self):
        self.flaps_state = "Flaps hidden"
        print(self.flaps_state)
    def incline_ailerons(self):
        self.ailerons_state = "Ailerons inclined"
        print(self.ailerons_state)
    def decline_ailerons(self):
        self.ailerons_state = "Ailerons not inclined"
        print(self.ailerons_state)
    
class Empennage:
    def __init__(self):
        self.elevator_state = "Elevator not inclined" # кермо висоти
        self.rudder_state = "Rudder unturned" # стерно
    def incline_elevator(self):
        self.elevator_state = "Elevator inclined"
        print(self.elevator_state)
    def decline_elevator(self):
        self.elevator_state = "Elevator not inclined"
        print(self.elevator_state)
    def turn_rudder(self):
        self.rudder_state = "Rudder turned"
        print(self.rudder_state)
    def unturn_rudder(self):
        self.rudder_state = "Rudder unturned"
        print(self.rudder_state)

class LandingGearSystem:
    def __init__(self):
        self.chassis_state = "Chassis released" # шасі випущено
        self.brakes_state = "Brakes activated"
    def hide_chassis(self):
        self.chassis_state = "Chassis hidden"
        print(self.chassis_state)
    def release_chassis(self):
        self.chassis_state = "Chassis released"
        print(self.chassis_state)
    def deactivate_brakes(self):
        self.brakes_state = "Brakes deactivated"
        print(self.brakes_state)
    def activate_brakes(self):
        self.brakes_state = "Brakes activated"
        print(self.brakes_state)

class FlightControlSystem:
    def __init__(self):
        self.steeringWheel_state = "Steering wheel aligned"
        self.pedals_state = "Pedals unpressed"
        self.tractionControlLever_state = "Traction control lever pulled down"
        self.fuelSupplyButton_state = "Fuel supply button unpressed"
        self.gasButton_state = "Gas button unpressed"
        self.flapsButton_state = "Flaps button unpressed"
        self.chassisButton_state = "Chassis button unpressed"
        self.brakesButton_state = "Brakes button unpressed"
        self.hydraulicButton_state = "Hydraulic button unpressed"
    def raise_steeringWheel(self):
        self.steeringWheel_state = "Steering wheel raised"
        print(self.steeringWheel_state)
    def lower_steeringWheel(self):
        self.steeringWheel_state = "Steering wheel lowered"
        print(self.steeringWheel_state)
    def turnRight_steeringWheel(self):
        self.steeringWheel_state = "Steering wheel turned right"
        print(self.steeringWheel_state)
    def turnLeft_steeringWheel(self):
        self.steeringWheel_state = "Steering wheel turned left"
        print(self.steeringWheel_state)
    def align_steeringWheel(self):
        self.steeringWheel_state = "Steering wheel aligned"
        print(self.steeringWheel_state)
    def pressRight_pedal(self):
        self.pedals_state = "Right pedal pressed"
        print(self.pedals_state)
    def pressLeft_pedal(self):
        self.pedals_state = "Left pedal pressed"
        print(self.pedals_state)
    def pullUp_tractionControlLever(self):
        self.tractionControlLever_state = "Traction control lever pulled up"
        print(self.tractionControlLever_state)
    def pullDown_tractionControlLever(self):
        self.tractionControlLever_state = "Traction control lever pulled down"
        print(self.tractionControlLever_state)
    def press_fuelSupplyButton(self):
        self.fuelSupplyButton_state = "Fuel supply button pressed"
        print(self.fuelSupplyButton_state)
    def unpress_fuelSupplyButton(self):
        self.fuelSupplyButton_state = "Fuel supply button unpressed"
        print(self.fuelSupplyButton_state)
    def press_gasButton(self):
        self.gasButton_state = "Gas button pressed"
        print(self.gasButton_state)
    def unpress_gasButton(self):
        self.gasButton_state = "Gas button unpressed"
        print(self.gasButton_state)
    def press_flapsButton(self):
        self.flapsButton_state = "Flaps button pressed"
        print(self.flapsButton_state)
    def press_chassisButton(self):
        self.chassisButton_state = "Chassis button pressed"
        print(self.chassisButton_state)
    def press_brakesButton(self):
        self.brakesButton_state = "Brakes button pressed"
        print(self.brakesButton_state)
    def press_hydraulicButton(self):
        self.hydraulicButton_state = "Hydraulic button pressed"
        print(self.hydraulicButton_state)

class HydraulicSystem:
    def __init__(self):
        self.hydraulicPump_state = "Hydraulic pump turned off"
    def start_hydraulicPump(self):
        self.hydraulicPump_state = "Hydraulic pump turned on"
        print(self.hydraulicPump_state)
    def stop_hydraulicPump(self):
        self.hydraulicPump_state = "Hydraulic pump turned off"
        print(self.hydraulicPump_state)



class Airplane:
    def __init__(self, pilot, secondpilot, passengers, max_passengers, max_speed, max_fuel, length, wingspan, heigth, weight, engines_number):
        self.pilot = pilot
        self.secondpilot = secondpilot
        self.passengers = passengers
        self.max_passengers = max_passengers
        self.max_speed = max_speed
        self.max_fuel = max_fuel
        self.length = length
        self.wingspan = wingspan
        self.heigth = heigth
        self.weight = weight
        self.engines_number = engines_number
        self.fuelInjection_system = FuelInjectonSystem()
        self.engine_system = Engine()
        self.fuselage_system = Fuselage()
        self.wing_system = Wing()
        self.empennage_system = Empennage()
        self.landingGear_system = LandingGearSystem()
        self.flightControl_system = FlightControlSystem()
        self.hydraulic_system = HydraulicSystem()
        self.plane_state = "none"


# Завантаження вантажу
    def cargo_load(self):
        self.fuselage_system.load_cargo()
        print("Your cargo have been loaded\n")

# Запуск
    def start(self):
        print("!Airplane launch!")
        print(" \n")
        self.flightControl_system.press_hydraulicButton()
        self.hydraulic_system.start_hydraulicPump()
        print(" \n")
        self.flightControl_system.press_flapsButton()
        self.wing_system.release_flaps()
        print(" \n")
        self.flightControl_system.press_brakesButton()
        self.landingGear_system.deactivate_brakes()
        print(" \n")
        self.flightControl_system.press_fuelSupplyButton()
        self.fuelInjection_system.start_fuelInjection()
        print(" \n")
        self.flightControl_system.press_gasButton()
        self.engine_system.start_engine()
        print("\nYour plane is ready to takeoff!")
        print(" \n")
        self.plane_state = "started"

# Зліт
    def takeoff(self):
        if self.plane_state == "started" :
            self.flightControl_system.pullUp_tractionControlLever()
            self.engine_system.increase_traction()
            print(" \n")
            self.flightControl_system.raise_steeringWheel()
            self.empennage_system.incline_elevator()
            print(" \n")
            self.flightControl_system.press_chassisButton()
            self.landingGear_system.hide_chassis()
            print(" \n")
            self.flightControl_system.align_steeringWheel()
            self.empennage_system.decline_elevator()
            print("\n!!!Congratulations!!!")
            print("Your plane is flying now")
            print("You can control the flight by yourself")
            print(" \n")
            self.plane_state = "flight"
        else:
            print("You need to launch your airplane at first!\n")

# Політ
    def raisePlane(self):
        if self.plane_state != "landed":
            if self.plane_state == "flight":
                self.flightControl_system.raise_steeringWheel()
                self.empennage_system.incline_elevator()
                print("You have raised your airplane\n")
            else:
                print("You need to takeoff your airplane at first!\n")
        else:
            print("You cannot do this while your airplane is landed!\n")

    def lowerPlane(self):
        if self.plane_state != "landed":
            if self.plane_state == "flight":
                self.flightControl_system.lower_steeringWheel()
                self.empennage_system.incline_elevator()
                print("You have lowered your airplane\n")
            else:
                print("You need to takeoff your airplane at first!\n")
        else:
            print("You cannot do this while your airplane is landed!\n")

    def inclinePlane_right(self):
        if self.plane_state != "landed":
            if self.plane_state == "flight":
                self.flightControl_system.turnRight_steeringWheel()
                self.wing_system.incline_ailerons()
                print("You have inclined your airplane to the right!\n")
            else:
                print("You need to takeoff your airplane at first!\n")
        else:
            print("You cannot do this while your airplane is landed!\n")

    def inclinePlane_left(self):
        if self.plane_state != "landed":
            if self.plane_state == "flight":
                self.flightControl_system.turnLeft_steeringWheel()
                self.wing_system.incline_ailerons()
                print("You have inclined your airplane to the left!\n")
            else:
                print("You need to takeoff your airplane at first!\n")
        else:
            print("You cannot do this while your airplane is landed!\n")
        
    def turnPlane_right(self):
        if self.plane_state == "flight" or self.plane_state == "landed":
                self.flightControl_system.pressRight_pedal()
                self.empennage_system.turn_rudder()
                print("You have turned your airplane to the right!\n")
        else:
            print("You need to takeoff your airplane at first!\n")

    def turnPlane_left(self):
        if self.plane_state == "flight" or self.plane_state == "landed":
                self.flightControl_system.pressLeft_pedal()
                self.empennage_system.turn_rudder()
                print("You have turned your airplane to the left!\n")
        else:
            print("You need to takeoff your airplane at first!\n")

    def alignPlane(self):
        if self.plane_state == "flight" or self.plane_state == "landed":
                self.flightControl_system.align_steeringWheel()
                self.wing_system.decline_ailerons()
                print("You have aligned your airplane!\n")
        else:
            print("You need to takeoff your airplane at first!\n")

    def increase_speedPlane(self):
        if self.plane_state == "flight" or self.plane_state == "landed":
                self.flightControl_system.pullUp_tractionControlLever()
                print("The speed of your airplane has been increased\n")
        else:
                print("You need to takeoff your airplane at first!\n")
    
    def decrease_speedPlane(self):
        if self.plane_state == "flight" or self.plane_state == "landed":
                self.flightControl_system.pullDown_tractionControlLever()
                print("The speed of your airplane has been already decreased\n")
        else:
            print("You need to takeoff your airplane at first!\n")

# Посадка
    def landing(self):
        if self.plane_state == "flight":
            if self.flightControl_system.steeringWheel_state == "Steering wheel aligned":
                self.flightControl_system.pullDown_tractionControlLever()
                self.engine_system.decrease_traction()
                print(" \n")
                self.flightControl_system.lower_steeringWheel()
                self.empennage_system.incline_elevator()
                print(" \n")
                self.flightControl_system.press_chassisButton()
                self.landingGear_system.release_chassis()
                print("\nYou have successfully landed your plane")
                print("!!!Congratulations!!!")
                print(" \n")
                self.plane_state = "landed"
            else:
                print("You need to align your airplane at first!\n")
        else:
            print("You need to takeoff your airplane at first!\n")

# Зупинка
    def stop(self):
        if self.plane_state == "landed" or self.plane_state == "started":
            self.flightControl_system.unpress_fuelSupplyButton()
            self.fuelInjection_system.stop_fuelInjection()
            print(" \n")
            self.flightControl_system.unpress_gasButton()
            self.engine_system.stop_engine()
            print(" \n")
            self.flightControl_system.press_brakesButton()
            self.landingGear_system.activate_brakes()
            print(" \n")
            self.flightControl_system.press_flapsButton()
            self.wing_system.hide_flaps()
            print(" \n")
            self.flightControl_system.press_hydraulicButton()
            self.hydraulic_system.stop_hydraulicPump()
            print(" \n")
            print("You have stopped your airplane")
            self.plane_state = "stopped"
            if self.fuselage_system.cargo_state == "Cargo loaded":
                self.fuselage_system.deload_cargo()
                print("Your cargo have been deloaded\n")
        else:
            print("You need to land your airplane at first!\n")
