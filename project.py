from project_classes import *

pilot = Pilot(name='Oleg', age='28', pilot_license='ai7fg8dn6')
secondpilot = Pilot(name='Kirill', age='25', pilot_license='i4gh6mk29')
passengers = [Passenger(name="Alex", age="18")]

boing_747 = Airplane(
    pilot=pilot,
    secondpilot=secondpilot,
    passengers= passengers,
    max_passengers=467,
    max_speed=1150,
    max_fuel=227600,
    length=76.4,
    wingspan=68.5,
    heigth=19.4,
    weight=276.7,
    engines_number=4
)


userInputNum = " "
while userInputNum != "b":

    print("0. Load your cargo (optional)")
    print("1. Launch the airplane")
    print("2. Takeoff the airplane")
    print("!During the flight or landed!:")
    print("3. Raise the airplane")
    print("4. Lower the airplane")
    print("5. Incline the airplane right")
    print("6. Incline the airplane left")
    print("7. Turn the airplane right")
    print("8. Turn the airplane left")
    print("9. Increase speed of the airplane")
    print("10. Decrease speed of the airplane")
    print("11. Align the airplane")
    print("12. Land the airplane")
    print("13. Stop the airplane")
    print("To exit the programm type b") # b (break)

    userInputNum = input("\nType a number of the element:")
    print(" ")
    if userInputNum == "0":
        boing_747.cargo_load()
    if userInputNum == "1":
        boing_747.start()
    if userInputNum == "2":
        boing_747.takeoff()
    if userInputNum == "3":
        boing_747.raisePlane()
    if userInputNum == "4":
        boing_747.lowerPlane()
    if userInputNum == "5":
        boing_747.inclinePlane_right()
    if userInputNum == "6":
        boing_747.inclinePlane_left()
    if userInputNum == "7":
        boing_747.turnPlane_right()
    if userInputNum == "8":
        boing_747.turnPlane_left()
    if userInputNum == "9":
        boing_747.increase_speedPlane()
    if userInputNum == "10":
        boing_747.decrease_speedPlane()
    if userInputNum == "11":
        boing_747.alignPlane()
    if userInputNum == "12":
        boing_747.landing()
    if userInputNum == "13":
        boing_747.stop()
    if userInputNum not in "012345678910111213b":
        print("\nТакого елемента меню не існує")
