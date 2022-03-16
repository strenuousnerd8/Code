# Smallest and simplest solution in hackerrank
# Given an integer n and space-separated integers as input,
# create a tuple of those integers.
# Then compute hash and print the result of it.
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(abs(hash(tuple(integer_list))))