if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum = 0
    for key,value in student_marks.items():
        if key == query_name:
            for i in value:    
                sum = sum + i
            avg = sum/len(value)
    print(f"{avg:.2f}") 
