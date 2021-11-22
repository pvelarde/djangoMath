#   function specialMath(int n) {
# 	    if(n==0) return 0
# 	    else if(n==1) return 1
# 	    else return n + specialMath(n-1) + specialMath(n-2)
#   }

def specialMath(number):
    if number in {0,1}:
        return number
    if number == 2:
        return 3
    if number == 3:
        return 7
    last2, last1, cur_number = 1, 3, 7 # n-2 , n-1 , n => n=3
    for i in range(4, number+1):
        last2 = last1
        last1 = cur_number
        cur_number = i + last1 + last2
    return cur_number

if __name__ == '__main__':
    print(specialMath(7))
    print(specialMath(17))
    print(specialMath(90))