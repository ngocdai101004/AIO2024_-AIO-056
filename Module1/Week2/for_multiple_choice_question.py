
# Question 5
def check_the_number(n):
    list_of_numbers = []
    for i in range(1, 5):
        list_of_numbers.append(i)
    if n in list_of_numbers:
        results = "True"
    if n not in list_of_numbers:
        results = "False"
    return results

# ------------------------------------------------------------------------------

# Question 6


def my_function6(data, max, min):
    result = []
    for i in data:
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


# ------------------------------------------------------------------------------

# Question 7
def my_function7(x: list, y: list):
    x.extend(y)
    return x


# ------------------------------------------------------------------------------

# Question 8


def my_function8(n):
    return min(n)


# ------------------------------------------------------------------------------

# Question 9


def my_function9(n):
    return max(n)

# ------------------------------------------------------------------------------

# Question 10


def my_function10(integers, number=1):
    return any([True if i == number else False for i in integers])


# ------------------------------------------------------------------------------

# Question 11


def my_function11(list_nums=[0, 1, 2]):
    var = 0
    for i in list_nums:
        var += i
    return var/len(list_nums)


# ------------------------------------------------------------------------------

# Question 12


def my_function12(data):
    var = []
    for i in data:
        if i % 3 == 0:
            var.append(i)
    return var


# ------------------------------------------------------------------------------

# Question 13


def my_function13(y):
    var = 1
    while (y > 1):
        var *= y
        y -= 1
    return var


# ------------------------------------------------------------------------------

# Question 14


def my_function14(y):
    var = ''
    for i in y:
        var = i + var
    return var


# ------------------------------------------------------------------------------

# Question 15


def function_helper15(x):
    return 'T' if x > 0 else 'N'


def my_function15(data):
    res = [function_helper15(x) for x in data]
    return res


# ------------------------------------------------------------------------------

# Question 16


def function_helper16(x, data):
    for i in data:
        if i == x:
            return 0
    return 1


def my_function16(data):
    res = []
    for i in data:
        if function_helper16(i, res):
            res.append(i)
    return res
