def pqhistogram (profit, year):
    print ("Earnings for WidgetCorp for "+str(year))
    print ("   Dollars for each quarter   ")
    print (" ==============================")
    for i in range(0,4):
        print ("Q"+str(i+1)+": ", end="")
        poundn(int(profit[i]/20000))
        print ("     ", profit[i])

    def poundn (ncharacters):
        for i in range(0,ncharacters):
            print ("#", end="")
            
profit2016 = [190000, 340000, 873000, 439833]
pqhistogram (profit2016, 2016)
