# List Comprehensions
# Given three integers x, y and z representing the dimensions
# of a cubiod along with an integer n, print all the possible
# coordinates given by (i, j, k) on a 3D grid where the sum
# i + j + k is not equal to n.

if __name__ == '__main__':
    x = int(input('Enter x:'))
    y = int(input('Enter y:'))
    z = int(input('Enter z:'))
    n = int(input('Enter n:'))
   
    a = [i for i in range(x+1)]
    b = [j for j in range(y+1)]
    c = [k for k in range(z+1)]
    d = [[i, j, k] for [i, j, k] in [(i, j, k) for i in a for j in b for k in c] if sum([i, j, k]) != n]
    print(d)
