import main

# Test calc_min_max_temperature()
def test_calc_min_max_temperature():
    temperatures = [5.0,67.0,32.0]
    result = main.calc_min_max_temperature(temperatures)
    assert result == [5.0,67.0]

# Test calc_average_temperature()
def test_calc_average_temperature():
    temperatures = [10.0, 20.0, 30.0]
    result = main.calc_average_temperature(temperatures)
    assert result == 20.0

# Test calc_median_temperature() with odd and even number of readings
def test_calc_median_temperature():
    odd_temperatures = [30.0, 10.0, 20.0]
    odd_result = main.calc_median_temperature(odd_temperatures)
    assert odd_result == 20.0

    even_temperatures = [10.0, 20.0, 30.0, 40.0]
    even_result = main.calc_median_temperature(even_temperatures)
    assert even_result == 25.0