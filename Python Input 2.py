# get the number of test cases (integer)
t = int(input())

for i in range(t):
    # first line contains the length of the permutation (integer)
    n = int(input())
    # we might not necessarily need this variable but it is crucial to maintain the structure of the input file
    # in each test case we have two inputs so we need to call input() function twice in each iteration of this for loop

    # second line contains the permutation (integer list)
    permutation = map(int,
                      input().split())  # The split() method splits a string into a list. You can specify the separator, default separator is any whitespace (example : "1 2 3 4 5".split() = ['1','2','3','4','5'])
# the map(int ,list ) function cast each element of the list to an int (list[0]->int(list[0]) ...)

# now that the input is done we can do some processing on the input to get the result of the program
