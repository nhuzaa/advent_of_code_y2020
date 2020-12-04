'''
--- Day 4: Passport Processing ---

Part 1
'''
import re
def read_data(file):
    with open(file, "r") as f:
        data = f.read()
        pass_list = [x for x in data.split('\n\n')]
    return pass_list 

def validator(passport):
    required_fields = ( 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    
    for f in required_fields:
        if f in passport:
            continue
        else:
            return False

    return True


def main():
    data = read_data("input")
    valid_passports = 0
    passports =[]
    for p in data :
        datum = re.split('\n| ', p)
        single_passport = {}
        for dd in datum:
            foo= dd.split(':')
            if len(foo)>1:
                single_passport[foo[0]] = foo[1]

        valid_passports = valid_passports + 1 if validator(single_passport) else valid_passports
        passports.append(single_passport)
    print(passports)
    print(valid_passports)
            



if __name__ == '__main__':
    import time 
    b = time.time()
    main()
    e = time.time()
    print("execution time:", e-b)

