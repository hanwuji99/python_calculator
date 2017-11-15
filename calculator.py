#!/usr/bin/env python3
import sys

# salary工资
# taxable_income应纳税所得额
# quick_calculation_deduction速算扣除数
# tax_rate税率
# taxable_amount应纳税额

arg = sys.argv
try:

    salary = int(arg[1])

    taxable_income = salary - 3500

    if taxable_income < 1500 or taxable_income == 1500:
        quick_calculation_deduction = 0
        tax_rate = 3 / 100
    elif taxable_income > 1500 and (taxable_income < 4500 or taxable_income == 4500):
        quick_calculation_deduction = 105
        tax_rate = 1 / 10
    elif taxable_income > 4500 and (taxable_income < 9000 or taxable_income == 9000):
        quick_calculation_deduction = 555
        tax_rate = 1 / 5
    elif taxable_income > 9000 and (taxable_income < 35000 or taxable_income == 35000):
        quick_calculation_deduction = 1005
        tax_rate = 1 / 4
    elif taxable_income > 35000 and (taxable_income < 55000 or taxable_income == 55000):
        quick_calculation_deduction = 2755
        tax_rate = 3 / 10
    elif taxable_income > 55000 and (taxable_income < 80000 or taxable_income == 80000):
        quick_calculation_deduction = 5505
        tax_rate = 35 / 100
    elif taxable_income > 80000:
        quick_calculation_deduction = 13505
        tax_rate = 45 / 100

    taxable_amount = taxable_income * tax_rate - quick_calculation_deduction
    print(format(taxable_amount,".2f"))

except:
    print("Parameter Error")
