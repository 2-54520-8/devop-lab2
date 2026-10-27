def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height ** 2)

    print(f"bmi: {bmi:.2f}")
    if bmi < 18.5:
        cat = "under"
    elif bmi < 25:
        cat = "norm"
    elif bmi < 30:
        cat = "over"
    else:
        cat = "obese"
    print(f"category: {cat}")
    
calculate_bmi(weight=101, height=1.80)   

