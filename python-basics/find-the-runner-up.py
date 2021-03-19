# Find the runner-up score
# Given the participants' score sheet for your university sports day,
# you are required to find the runner-up score. 
# You are given n scores. Store them in a list and find the score of the
# runner-up.

if __name__ == '__main__':
    n = int(input('Number of scores:'))
    arr = map(int, input('Enter scores:').split())
    scores = set([i for i in arr])
    scores.remove(max(scores))
    print(max(scores))

