
SLOT_CAPACITY = 40

class CarSlots:
    """
    A class to represent a parking lot with designated slots for cars.

    Attributes:
    slots (dict): A dictionary that maps the slot position to its level and number.
    all_positions (list): A list that stores all available slot positions.
    slot_mapper (dict): A dict that stores the mapping between car numbers and their slot positions.
    """
    def __init__(self) -> None:
        """
        Initializes a new instance of the CarSlots class with all available slots.
        """
        self.slots = self.get_all_slots(SLOT_CAPACITY)
        self.all_positions = list(self.slots.keys())
        self.slot_mapper={}
    

    def get_all_slots(self, slot_range) -> dict:
        """
        Creates a dictionary of all available slots with their level and number.

        Args:
        slot_range (int): The total number of slots available.

        Returns:
        A dictionary that maps the slot position to its level and number.
        """
        slots = {}
        for i in range(1, slot_range+1):
            if i > (slot_range//2):
                slots[i] = {"level": "B", "slot": i-(slot_range//2)}
            else:
                slots[i] = {"level": "A", "slot": i}
        return slots
    
    def assign_slot(self, carno: str) -> str:
        """
        Assigns a parking slot to a car with the given number.

        Args:
        carno (str): The number of the car to be parked.

        Returns:
        A message indicating the status of the parking operation.
        """
        if carno in self.slot_mapper:
            return f"Car {carno} Already Parked, Please Provide Another No"
        position=self.all_positions.pop()
        self.slot_mapper[carno]=position
        return f"Car Parked at {self.slots.get(position)}"
    



    def retrieve_slot(self, carno: str) -> str:
        """
        Retrieves a parked car with the given number.

        Args:
        carno (str): The number of the car to be retrieved.

        Returns:
        A message indicating the status of the retrieval operation.
        """
        if carno not in self.slot_mapper:
            return f"Car {carno} is not parked"
        return f"Car is parked at {self.slots.get(self.slot_mapper.get(carno))}"





def main_final():
    """
    A function to run the main program loop for the parking lot.
    """
    slot_obj = CarSlots()
    while True:
        try:
            print("Enter 1 to assign a parking spot, 2 to retrieve a parking spot, or 0 to exit.")
            choice = int(input())
            if choice == 0:
                print("Exiting...")
                break
            elif choice == 1:
                if not slot_obj.all_positions:
                    print("No Slots Available")
                vehicle_number = input("Enter vehicle number: ")
                response = slot_obj.assign_slot(vehicle_number)
                print(response)
            elif choice == 2:
                vehicle_number = input("Enter vehicle number: ")
                response = slot_obj.retrieve_slot(vehicle_number)
                print(response)
            
        except Exception as err:
            print("Invalid Input, Please Insert Proper Input")


if __name__ == "__main__":
    main_final()
