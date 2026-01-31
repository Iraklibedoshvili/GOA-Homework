def manual_max(arr):
    largest = arr[0]
    for number in arr:
        if number > largest:
            largest = number
    return(number)

def manual_len(sequence):
    count = 0
    for i in sequence:
        count += 1
    return count