# Nested Lists
# Given the names and grade for each student in a class of N students, store
# them in a nested list and print the name(s) of any student(s) having the
# second lowest grade.

# Note: If there are multiple students with the second lowest grade, order
# their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    records = list()
    for _ in range(int(input('# of students:'))):
        if n >= 2 and n <=5:
            try:
                name = str(input('Enter name:'))
                score = float(input('Enter score:'))

                records.append([name, score])
            except AssertionError as error:
                print(error)
                break

    scores = set([record[-1] for record in records])
    scores.remove(min(scores))

    names = set([record[-2] for record in records if record[-1] == min(scores)])

    for n in names:
        print(n)
