def check_temperature(temp_str: str):
        try:
            n = int(temp_str)
        except ValueError:
            print(f"Error: '{temp_str}' is not a valid integer")
            return None
    
        if not 0 <= n <= 40:
            print("Error: Temperature must be between 0°C and 40°C")
            return None
    
        return n