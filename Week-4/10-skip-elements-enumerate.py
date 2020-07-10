def skip_elements(elements):
    result = []
    for index, name in enumerate(elements):
        if index % 2 == 0:
            result.append(name)
            index += 2
	
    return result

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
