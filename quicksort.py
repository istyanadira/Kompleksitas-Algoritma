students = [
    ("Andi", 78),
    ("Budi", 65),
    ("Citra", 85),
    ("Dewi", 72),
    ("Eka", 90),   
]

def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[len(data) // 2][1]
    left = [x for x in data if x[1] < pivot]
    middle = [x for x in data if x[1] == pivot]
    right = [x for x in data if x[1] > pivot]

    return quick_sort(left) + middle + quick_sort(right)

sorted_students = quick_sort(students)
print("Hasil pengurutan nilai siswa secara quick sort: ")
for student in sorted_students:
    print(f"{student[0]}: {student[1]}")