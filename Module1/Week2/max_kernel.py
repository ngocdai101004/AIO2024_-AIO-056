
def max_kernel (num_list, window_size):
    if window_size < 1:             
        assert "k must be greater than or equal to 1"
    max_list = []
    n = len(num_list)
    current_maximum_value  = max(num_list[0:window_size])
    max_list.append(current_maximum_value)

    i = 1
    while (i + window_size - 1 <= n - 1):
        if num_list[i + window_size - 1] > current_maximum_value:
                current_maximum_value = num_list[i + window_size - 1] 
        max_list.append(current_maximum_value)
        i+=1
    return max_list


    
if __name__ == "__main__":
    assert max_kernel ([3 , 4 , 5 , 1 , -44] , 3) == [5 , 5 , 5]
    num_list = [3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1]
    k = 3
    print (max_kernel(num_list , k))
