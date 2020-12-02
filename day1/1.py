


def main():
    f = open("input", "r")
    data = f.read()
    num_list= [int(x) for x in data.splitlines()]
    print(num_list)

    #filter out the list
    less_than_yr = [x for x in num_list if x <= 2020]

    #condition
    # sum 2020 then get the product of it

    prod_list = [] 

    '''
    time complexity O(n)
    '''
    for x in less_than_yr:
        diff = 2020 -x
        if diff in less_than_yr: #dnt know the time comp of this 
            prod = x * diff
            prod_list.append(prod)

    print(prod_list)

if __name__ == '__main__':
    import time 
    b = time.time()
    main()
    e = time.time()
    print("execution time:", e-b)
