#!/usr/bin/env python3
import sys


def calculator(salary):
    try:
        salary = int(salary)
        if salary > 3500:
            taxable_income = salary - salary * (16.5 / 100) - 3500
        else:
            taxable_income = 0
        if taxable_income <= 1500:
            quick_calculation_deduction = 0
            tax_rate = 3 / 100
        elif taxable_income > 1500 and taxable_income <= 4500:
            quick_calculation_deduction = 105
            tax_rate = 1 / 10
        elif taxable_income > 4500 and taxable_income <= 9000:
            quick_calculation_deduction = 555
            tax_rate = 1 / 5
        elif taxable_income > 9000 and taxable_income <= 35000:
            quick_calculation_deduction = 1005
            tax_rate = 1 / 4
        elif taxable_income > 35000 and taxable_income <= 55000:
            quick_calculation_deduction = 2755
            tax_rate = 3 / 10
        elif taxable_income > 55000 and taxable_income <= 80000:
            quick_calculation_deduction = 5505
            tax_rate = 35 / 100
        elif taxable_income > 80000:
            quick_calculation_deduction = 13505
            tax_rate = 45 / 100

        taxable_amount = taxable_income * tax_rate - quick_calculation_deduction
        salary_after_tax = salary - salary * 16.5/100 - taxable_amount
        # print(format(salary_after_tax, ".2f"))
        return salary_after_tax

    except:
        print("Parameter Error")


def print_info(args):
    for arg in args:
        try:
            arg = arg.split(':')
            # print('arg',arg)
            result = calculator(arg[1])
            print(arg[0]+":"+format(result, ".2f"))
        except:
            print("Parameter Error")


if __name__ == "__main__":
    args = sys.argv[1:]
    # print('args',args)
    if len(args) < 1:
        print("Parameter Error")
    else:
        print_info(args)
