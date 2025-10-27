students = [
    ("Andi", 78),
    ("Budi", 65),
    ("Citra", 85),
    ("Dewi", 72),
    ("Eka", 90),   
]

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][1] < right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

sorted_students = merge_sort(students)
print("Hasil pengurutan nilai siswa secara merge sort: ")
for student in sorted_students:
    print(f"{student[0]}: {student[1]}")