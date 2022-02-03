def skip_elements(elements):
    # code goes here
    new_list = []
    for i, chars in enumerate(elements):
        if i % 2 == 0:
            new_list.append(chars)
    return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']