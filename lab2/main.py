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

# Runs main() when this file is executed directly
if __name__ == "__main__":
    main()