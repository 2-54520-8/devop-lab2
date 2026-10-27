# Main function: runs the program in order
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

    display_main_menu()                 # Display instructions
    num_list = get_user_input()         # Get the user's temperature readings

    # Calculate and display the results
    print("Average:", calc_average_temperature(num_list))
    print("Min and Max:", calc_min_max_temperature(num_list))
    print("Sorted:", sort_temperature(num_list))
    print("Median:", calc_median_temperature(num_list))

# Displays the instructions for entering numbers
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

# Reads comma-separated numbers and returns a list of floats
def get_user_input() -> list[float]:
    user_input = input()                                    # Read input from the terminal
    string_list = user_input.split(",")                     # Split the string at each comma
    float_list = [float(number) for number in string_list]  # Convert strings to floats
    return float_list                                       # Return the list of numbers

# Calculates and returns the average temperature
def calc_average_temperature(temperatures: list[float]) -> float:
    return sum(temperatures) / len(temperatures)

# Returns a list containing the minimum and maximum temperatures as integers
def calc_min_max_temperature(temperatures: list[float]) -> list[int]:
    return [int(min(temperatures)), int(max(temperatures))]

# Sorts temperatures in ascending order (smallest to largest)
def sort_temperature(temperatures: list[float]) -> list[float]:
    return sorted(temperatures)

# Calculates and returns the median temperature
def calc_median_temperature(temperatures: list[float]) -> float:
    sorted_temperatures = sorted(temperatures)     # Sort the temperatures first
    n = len(sorted_temperatures)                   # Count the readings
    middle = n // 2                                # Find the middle index

    if n % 2 == 1:                                 # Odd number of readings
        return sorted_temperatures[middle]         # Return the middle value
    else:                                          # Even number of readings
        # Return the average of the two middle values
        return (sorted_temperatures[middle - 1] + sorted_temperatures[middle]) / 2

# Runs main() when this file is executed directly
if __name__ == "__main__":
    main()