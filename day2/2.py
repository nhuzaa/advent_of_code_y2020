

def main():
    f = open("input", "r")
    data = f.read()
    pass_list = [x.split() for x in data.splitlines()]
    print(pass_list)

    valid_pass = 0
    for p in pass_list:
        pos_list = p[0].split('-')
        pos_list = [int(x)-1 for x in pos_list] # noob indexing so -1 
        chr = p[1][0]
        password = p[2]
        print("poss list", pos_list,chr,password)
        chr_count = 0


        try:
            if password[pos_list[0]] == chr and password[pos_list[1]] == chr:
                continue
            elif password[pos_list[0]] == chr:
                valid_pass+=1
            elif password[pos_list[1]] == chr:
                valid_pass+=1

        except IndexError as e:
            print("index error")

    f.close() 

    print("##### Valid pass :", valid_pass)


if __name__ == '__main__':
    import time 
    b = time.time()
    main()
    e = time.time()
    print("execution time:", e-b)
