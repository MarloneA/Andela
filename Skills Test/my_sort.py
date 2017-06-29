def my_sort(num_list):
    even_num = []
    odd_num = []
    for num in num_list:
        if num % 2 == 0:
            even_num.append(num)
        else:
            odd_num.append(num)
    return (sorted(odd_num) + sorted(even_num))
