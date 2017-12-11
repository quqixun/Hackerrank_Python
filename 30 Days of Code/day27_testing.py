def print_test(n, k, a):
    print(str(n) + " " + str(k))
    print(" ".join(map(str, a)))


test_cases_num = 5
print(test_cases_num)
print_test(4, 3, [-1, -3, 4, 2])
print_test(5, 2, [0, -1, 2, 1, 4])
print_test(5, 3, [-7, 2, 3, 0, -1])
print_test(3, 1, [-1, 0, 4])
print_test(6, 4, [0, -1, 1, 4, 5, 6])
