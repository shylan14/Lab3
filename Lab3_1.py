def remove_even_elements(lst):
    return [item for item in lst if item % 2 != 0]

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = remove_even_elements(input_list)
print("Список без парних елементів:", result)
