def tower_of_hanoi(n, first, second, third):
    if n == 1:
        print("Move disk 1 from rod", first , "to rod", second)
        return
    tower_of_hanoi(n-1, first , third , second )
    print("Move disk", n, "from rod", first , "to rod", second )
    tower_of_hanoi(n-1, third , second , first )


n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
