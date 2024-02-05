parcel_data = [
    ["ABC123", "Parcel in transit"],
    ["XYZ789", "Parcel out for delivery"],
    ["123456", "Parcel delivered"]
]


def simulate_tracking(tracking_number):
    for parcel in parcel_data:
        if parcel[0] == tracking_number:
            print(f"Tracking Number: {parcel[0]}, Status: {parcel[1]}")
            return
    print("Tracking number not found.")


user_tracking_number = input("Enter parcel tracking number: ")
simulate_tracking(user_tracking_number)