#use of range() 
def testRange(n):
    # values = range(4)
    #iterate from i = 0 to i = 12
    print('สูตรคูณแม่ ' + str(n))
    values = range(1,12+1)
    for i in values:
        print("%d * %d = %d" %(n, i, n*i))