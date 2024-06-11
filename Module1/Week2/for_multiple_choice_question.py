
#Question 5
def check_the_number(N):
    list_of_numbers = []
    result = ""
    for i in range (1 ,5):
        list_of_numbers.append(i)
    if N in list_of_numbers :
        results = "True"
    if N not in list_of_numbers :
        results = "False"
    return results  

#------------------------------------------------------------------------------       

#Question 6
def my_function6 ( data , max , min) :
    result = []
    for i in data :
        if i < min:
            result.append(min)
        elif i > max:
            result.append(max)
        else:
            result.append(i)
    return result


# my_list = [5 , 2 , 5 , 0 , 1]
# max = 1
# min = 0
# assert my_function6 (max = max , min = min , data = my_list ) == [1 , 1 , 1 , 0 , 1]
# my_list = [10 , 2 , 5 , 0 , 1]
# max = 2
# min = 1
# print ( my_function6 ( max = max , min = min , data = my_list ) )

#------------------------------------------------------------------------------  

#Question 7
def my_function7 (x:list, y:list):
    x.extend(y)
    return x

# list_num1 = ['a', 2 , 5]
# list_num2 = [1 , 1]
# list_num3 = [0 , 0]
# assert my_function7 ( list_num1 , my_function7 ( list_num2 , list_num3 ) ) == ['a', 2 , 5 , 1 , 1 , 0, 0]

# list_num1 = [1 , 2]
# list_num2 = [3 , 4]
# list_num3 = [0 , 0]
# print ( my_function7 ( list_num1 , my_function7 ( list_num2 , list_num3 ) ) )

#------------------------------------------------------------------------------  

#Question 8
def my_function8 ( n ) :
    return min(n)

# my_list = [1 , 22 , 93 , -100]
# assert my_function8 ( my_list ) == -100
# my_list = [1 , 2 , 3 , -1]
# print ( my_function8 ( my_list ) )

#------------------------------------------------------------------------------  

#Question 9
def my_function9 ( n ) :
 return max(n)

# my_list = [1001 , 9 , 100 , 0]
# assert my_function9 ( my_list ) == 1001
# my_list = [1 , 9 , 9 , 0]
# print ( my_function9 ( my_list ) )

#------------------------------------------------------------------------------  

#Question 10
def My_function10 ( integers , number = 1) :
    return any([True if i == number else False for i in integers])

# my_list = [1 , 3 , 9 , 4]
# assert My_function10 ( my_list , -1) == False
# my_list = [1 , 2 , 3 , 4]
# print ( My_function10 ( my_list , 2) )

#------------------------------------------------------------------------------  

#Question 11
def my_function11 ( list_nums = [0 , 1 , 2]) :
    var = 0
    for i in list_nums :
        var += i
    return var/len(list_nums)

# assert my_function11 ([4 , 6 , 8]) == 6
# print ( my_function11 () )

#------------------------------------------------------------------------------  

#Question 12

def my_function12 ( data ) :
    var = []
    for i in data :
        if i % 3 == 0:
            var.append(i)
    return var

# assert my_function12 ([3 , 9 , 4 , 5]) == [3 , 9]
# print ( my_function12 ([1 , 2 , 3 , 5 , 6]) )

#------------------------------------------------------------------------------  

#Question 13

def my_function13 (y) :
    var = 1
    while (y > 1):
        var*=y
        y-=1
    return var

# assert my_function13 (8) == 40320
# print ( my_function13 (4) )

#------------------------------------------------------------------------------  

#Question 14

def my_function14 (y) :
    var = ''
    for i in y:
        var = i + var
    return var

# x = 'I can do it'
# assert my_function14 (x ) =="ti od nac I"
# x = 'apricot'
# print ( my_function14 ( x ) )

#------------------------------------------------------------------------------  

#Question 15

def function_helper15 ( x ) :
    return 'T' if x > 0 else 'N'

def my_function15 ( data ) :
    res = [ function_helper15 ( x ) for x in data ]
    return res

# data = [10 , 0 , -10 , -1]
# assert my_function15 ( data ) == ['T', 'N', 'N', 'N']
# data = [2 , 3 , 5 , -1]
# print ( my_function15 ( data ) )

#------------------------------------------------------------------------------  

#Question 16

def function_helper16 ( x, data) :
    for i in data:
        if i == x:
            return 0
    return 1

def my_function16 ( data ) :
    res= []
    for i in data:
        if function_helper16(i, res):
            res.append(i)
    return res


lst = [10 , 10 , 9 , 7 , 7]
assert my_function16 ( lst ) ==[10 , 9 , 7]
lst = [9 , 9 , 8 , 1 , 1]
print ( my_function16 ( lst ) )


