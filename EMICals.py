# p = 100000
# Interest = 10%
# Tenure = 12M
import pdb

class EmiCal():

    def __init__(self,pr,t,r):
        self.pr = pr
        self.t = t
        self.r = r

    def emi_formula(self):
        #t in years
        t = self.t * 12
        r = self.r/(12*100)

        for t in range(t, 0, -1):
            print(f'P={self.pr},t={t},r={r}')
            EMI = (self.pr * r * (1+r)**t)/(((1+r)**t) - 1)

            Interest = r*self.pr
            p_paid  = EMI - Interest
            print(round(p_paid),round(Interest),round(p_paid+Interest),round(self.pr-p_paid)  )
            self.pr=round(self.pr-p_paid)

find = EmiCal(1000,1,12)
find.emi_formula()




