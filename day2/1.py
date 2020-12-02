

def main():
    f = open("input", "r")
    data = f.read()
    pass_list = [x.split() for x in data.splitlines()]
    print(pass_list)

    valid_pass = 0
    for p in pass_list:
        min_max_list = p[0].split('-')
        min_max_list = [int(x) for x in min_max_list]
        chr = p[1][0]
        password = p[2]
        print("min_max_list", min_max_list,chr,password)
        chr_count = 0

        for c in password:
            if c == chr:
                chr_count+=1

        if chr_count >= min_max_list[0] and chr_count <= min_max_list[1]:
            valid_pass+=1

    f.close() 

    print("valid pass", valid_pass)


if __name__ == '__main__':
    import time 
    b = time.time()
    main()
    e = time.time()
    print("execution time:", e-b)
