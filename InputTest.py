# Raw integer list input
print(
    list(
        map(int, str(input()).split())
    )
)

# Linear search
k = str(input("Enter search elem:\t"))
print([f'{x}' for x in str(input("Enter the elements:\t").replace(' ', '')) if x == k])
