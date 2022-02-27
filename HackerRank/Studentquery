# Print the grade of given student in dictionary
# INPUT
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# OUTPUT 56.00
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for _ in student_marks.items():
        if _[0] == query_name:
            print("{:.2f}".format((_[1][0] + _[1][1] + _[1][2]) / 3))