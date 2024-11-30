class Vehicle: 
    # Constructor to initialize the attributes
    def __init__(self, reg_num, vehicle_type, owner):
        self.registration_num = reg_num  # Fixed consistent naming
        self.type = vehicle_type
        self.owner = owner 

    # Method to update the owner
    def update_owner(self, new_owner):
        self.owner = new_owner  # Update the owner attribute
        print(f"Ownership of vehicle {self.registration_num} has been transferred to {self.owner}.")


# Demonstration script
if __name__ == "__main__":
    # Creating the vehicle instances
    Vehicle1 = Vehicle("ABC345", "Car", "Tev")
    Vehicle2 = Vehicle("DFR345", "Truck", "Mal")
    Vehicle3 = Vehicle("BVH234", "Van", "TJ")

    # Displaying the initial details of the vehicles created
    print(f"Vehicle 1: Reg No - {Vehicle1.registration_num}, Type - {Vehicle1.type}, Owner - {Vehicle1.owner}")
    print(f"Vehicle 2: Reg No - {Vehicle2.registration_num}, Type - {Vehicle2.type}, Owner - {Vehicle2.owner}")
    print(f"Vehicle 3: Reg No - {Vehicle3.registration_num}, Type - {Vehicle3.type}, Owner - {Vehicle3.owner}")

    # Updating ownership of Vehicle 1
    Vehicle1.update_owner("Alice")
    Vehicle1.update_owner("Javier")

    # Displaying the updated details
    print(f"Updated Vehicle 1: Reg No - {Vehicle1.registration_num}, Type - {Vehicle1.type}, Owner - {Vehicle1.owner}")
    print(f"Vehicle 2 remains unchanged: Reg No - {Vehicle2.registration_num}, Type - {Vehicle2.type}, Owner - {Vehicle2.owner}")
    print(f"Vehicle 3 remains unchanged: Reg No - {Vehicle3.registration_num}, Type - {Vehicle3.type}, Owner - {Vehicle3.owner}")
