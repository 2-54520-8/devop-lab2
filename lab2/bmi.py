def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height ** 2)

    print(f"bmi: {bmi:.2f}")
    if bmi < 18.5:
        cat = "under"
        return -1
    elif bmi < 25:
        cat = "norm"
        return 0
    elif bmi < 30:
        cat = "over"
        return 1
    else:
        cat = "obese"
        return 2
    print(f"category: {cat}")
    
calculate_bmi(weight=101, height=1.80)

