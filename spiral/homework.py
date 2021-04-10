def spiralize(number):
    if n < 1 or n % 2 ==0: return None
    elif n == 1: return 1
    
    else:
        numbers = [1]
        numbers_needed = 2 * n -1
        increment = 2
        while len(numbers) < numbers_needed:
            increment = += 2 
            for p in range(4):
                numbers.append(numbers[-1] + increment)     
    return sum(numbers)
if __name__ == "__main__":
    start = time()
    ans = spiralize(501)
    elapsed_time = (timer() - start) * 1000 
    if ans: 
        print "Found Sum"
    else:
        print "No answer found"


    return return_value

