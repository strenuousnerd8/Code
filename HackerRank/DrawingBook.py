# A teacher asks the class to open their books to a page number.
# A student can either start turning pages from the front of the book or from the back of the book.
# They always turn pages one at a time.
# When they open the book, page 1 is always on the right
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    mini = []
    book = list(range(0, n + 1))
    book = [[page, book[i + 1]] for i, page in enumerate(book) if i % 2 == 0 and i != (len(book)-1)]
    if len(book) % 2 != 0 and n not in book[-1]:
        book.append([n])
    for i, pages in enumerate(book):
        if p in pages:
            mini.append(len(book[i:-1]))
            mini.append(len(book[0:i]))
    return min(mini) if n != p else 0

if __name__ == '__main__':

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(str(result) + '\n')
