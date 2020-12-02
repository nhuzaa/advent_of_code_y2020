
'''condition
sum 2020 then get the product of it
'''
def main():
    SUMTO =  2020 
    # num_list = [1,2,3,4,5,6,7,8,9,10,11]
    f = open("input2", "r")
    data = f.read()
    num_list= [int(x) for x in data.splitlines()]
    print(num_list)

    #filter out the list
    less_than_yr = [x for x in num_list if x <= 2020]

    #sorting
    less_than_yr.sort()
    print('####sorted',less_than_yr) 
    prod_list = [] 

    '''
    time complexity O(n)
    '''
    right_bound = len(less_than_yr) -1
    for k in range(0,right_bound):
        a = less_than_yr[k]
        for i in range(k,right_bound):
            c = less_than_yr[i]
            b = SUMTO - (a + c)
            # print (a , b , c)
            # print ('right_bound', right_bound)
            if b <= 0:
                right_bound -= i -1
                break
            elif b > 0:
                if b in less_than_yr[k+1:right_bound]: #dnt know the time comp of this a
                    print('b in arry', a , b , c)
                    prod = a * b * c 
                    prod_list.append(prod)

    #answer
    print(prod_list)

if __name__ == '__main__':
    import time 
    b = time.time()
    main()
    e = time.time()
    print("execution time:", e-b)
