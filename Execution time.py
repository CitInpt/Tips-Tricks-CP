#import the time module
import time

#main function contains the code to be executed
def main():
	#do_something

#variable start is used to track the time before executing the code aka starting a timer
start = time.perf_counter()

#call main function
main()

#variable end is used to stop the timer
end = time.perf_counter()

print("Python program took",round(end - start), "seconds to be executed")
