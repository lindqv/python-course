class Device:
    def __init__(self, brand: str, year: int, is_active=True):
        if year < 0:
            raise ValueError("The year cannot be negative.")
        self.brand = brand
        self.year = year
        self.is_active = is_active

class Laptop(Device):
    def __init__(self, brand, year, ram_gb, is_active=True):
        super().__init__(brand, year, is_active) # Reusing the initialization from Device here
        self.ram_gb = ram_gb

class Phone(Device):
    def __init__(self, brand, year, phone_number, is_active=True):
        super().__init__(brand, year, is_active) # Reusing the initialization from Device here
        self.phone_number = phone_number

