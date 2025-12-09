# Moving average of speeds

speeds = [52, 57, 60, 62, 64, 59, 58, 65, 70, 72, 68, 67]

def moving_average(data, window=3):
    result = []
    ma_range = len(data) - window + 1

    for i in range(ma_range):
        avg = sum(data[i:i+window]) / window
        result.append(round(avg, 2))

    return result

print(moving_average(speeds))