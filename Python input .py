###Here are some examples to master Python input:


PROBLEM_LINK = "https://codeforces.com/contest/1638/problem/A"

INPUT_STATEMENT = """
Each test contains multiple test cases. The first line contains a single integer t (1≤t≤500) — the number of test cases. Description of the test cases follows.

The first line of each test case contains a single integer n (1≤n≤500) — the length of the permutation.

The second line of each test case contains n integers p1,p2,…,pn (1≤pi≤n) — the elements of the permutation.

input example :
4
1
1
3
2 1 3
4
1 4 2 3
5
1 2 3 4 5
"""






#get the number of test cases (integer)
t = int(input())

for i in range(t):
	#first line contains the length of the permutation (integer)
	n = int(input())
	#we might not necessarily need this variable but it is crucial to maintain the structure of the input file
	#in each test case we have two inputs so we need to call input() function twice in each iteration of this for loop
	

	#second line contains the permutation (integer list)
	permutation = map(int, input().split()) #The split() method splits a string into a list. You can specify the separator, default separator is any whitespace (example : "1 2 3 4 5".split() = ['1','2','3','4','5'])
	#the map(int ,list ) function cast each element of the list to an int (list[0]->int(list[0]) ...) 

#now that the input is done we can do some processing on the input to get the result of the program



### We recommend checking the official Python3 documentation [https://docs.python.org/3/](https://docs.python.org/3/) to fully understand the context of split(), map() functions



