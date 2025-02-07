def sim(inp):
	linp = list(inp)

	li = []
	for i in range(0,len(linp)):
		s = ""
		for j in range(i,len(linp)):
			s = s + linp[j]
		li.append(s)

	lis = li
	print lis
	suming = 0
	for i in lis:
		llis = list(i)
		leng = 0
		for j in range(0,(len(llis))):
			if linp[j] == llis[j]:
				leng = leng + 1
			elif linp[j] != llis[j]:
				break
		suming = suming + leng

	print suming

def main():
    testcases = input()
    
    if testcases >=1 and testcases <=10:
        for i in range(testcases):
            string = raw_input()
            if len(string) <= 10000 and string.islower() and string.isalpha():
                sim(string)
            else:
                print "string length exceeded or Uppercase or numbers entered"
    else:
        print "test cases exceeded"
main()