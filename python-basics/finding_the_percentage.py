# Finding the percentage
# The provided code stub will read in a dictionary containing key/value pairs
# of name:[marks] for a list of students.
# Print the average of the marks array for the student name provided, showing
# 2 places after the decimal.


def mean(x):
    '''Get the mean/average'''
    return sum(x)/len(x)


if __name__ == '__main__':
    n = int(input('# of entries:'))
    student_marks = {}
    for _ in range(n):
        name, *line = input('Entries:').split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input('Query name:')

    print('%.2f' % (mean(student_marks.get(query_name))))
