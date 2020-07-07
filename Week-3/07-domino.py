for left in range(7):
    for right in range(left, 7):
        # Using end fundtion to end() after the entire loop, Python uses newline() by default.
        # Notice how the syntax uses a ", end=" 
        print("[" + str(left) + " | " + str(right) + "]", end=" ") 
    print()

    