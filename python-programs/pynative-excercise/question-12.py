class calculate_tax:

    def cal_tax(self, salary):
        t1 = 0
        original_salary = salary
        if salary <= 10000:
            t1 = 0
        elif salary <= 20000:
            t1 = (salary - 10000) * 10 / 100
        else:
            t1 = 0
            t1 = 10000 * 10 / 100
            t1 += (salary - 20000) * 20 / 100
        return t1


obj = calculate_tax()
print("Tax on Salary: ",obj.cal_tax(45000))
