def calculate(percentage_thresholds, max_value):
    result = []

    for note in range(1,6):
        lower_threshold = round(max_value * percentage_thresholds[note - 1])
        if note == 5:
            upper_threshold = max_value
        else:
            upper_threshold = round(max_value * percentage_thresholds[note]) - 1
        data = {"note": note, "lower": lower_threshold, "upper": upper_threshold}
        result.append(data)
    
    return result


if __name__ == "__main__":
    thresholds = [0, 0.2, 0.4, 0.6, 0.8]
    max_value = 31
    data = calculate(thresholds, max_value)
    print(data)
