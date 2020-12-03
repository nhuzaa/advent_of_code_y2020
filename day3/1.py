'''
Toboggan Trajectory
Part 1
'''
def main():
    with open("input", "r") as f:
        data = f.read()
        pass_list = [x for x in data.splitlines()]
    print(pass_list)


    width_of_trees = len(pass_list[0])
    no_of_lanes = len(pass_list)
    count_trees_pass = 0
    slope = (3,1)
    current_lane = 0
    plane_pos = [0,0]
    print('width_of_trees', width_of_trees)
    print('no_of_lanes', no_of_lanes)

    
    i = 0
    for y in range (plane_pos[1], no_of_lanes, slope[1]):
        if y > 0:#skip first line
            if pass_list[y][i] == '#':
                count_trees_pass += 1
                print('X')

            else:
                print('0')

        for x in range (plane_pos[0], plane_pos[0]+slope[0]+1): # +1 as range generate (0,3) 0 1 2
            i = x % width_of_trees
            print('mod',x, y)
        print('^')
        plane_pos[0] = x
        
    print("trees encounter", count_trees_pass)

    f.close() 



if __name__ == '__main__':
    import time 
    b = time.time()
    main()
    e = time.time()
    print("execution time:", e-b)
