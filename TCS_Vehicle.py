def count_vehicle(total_vehicle, total_wheel):
    # First count the four wheeler
    four_wheelers = (total_wheel - 2 * total_vehicle)//2
    # Count the two wheelers
    two_wheelers = total_vehicle - four_wheelers
    # Now check if they are valid or not
    if four_wheelers < 0 or two_wheelers < 0:
        return "No Solution"
    return four_wheelers, two_wheelers
total_vehicles = 200
total_wheels = 540
result = count_vehicle(total_vehicles, total_wheels)
print(result)

