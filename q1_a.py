import numpy as np

def simulate_attendance_record(strength=100):
    return np.random.randint(2, size=strength)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def find_absentee_count(attendance_record):
    low, high = 0, len(attendance_record)

    while low < high:
        mid = (low + high) // 2
        
        if attendance_record[mid] == 0:
            low = mid + 1
        else:
            high = mid

    return low

# Dummy test record
# attendance_records = [1, 1, 0, 0, 1, 1, 0, 1, 0, 0]

attendance_record = simulate_attendance_record()
sorted_attendance = merge_sort(attendance_record)

print(find_absentee_count(sorted_attendance))
