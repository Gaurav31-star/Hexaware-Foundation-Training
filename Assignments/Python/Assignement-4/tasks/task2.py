import random
import time


def courier_location_tracking(destination):
    current_location = 0

    print("Courier is on the way to the destination...")

    while current_location < destination:
        distance_covered = random.randint(1, 10)
        current_location += distance_covered
        print(f"Courier location: {current_location} km")
        time.sleep(1)  # 1 second delay

    print("Courier has reached the destination.")


destination_distance = 100
courier_location_tracking(destination_distance)