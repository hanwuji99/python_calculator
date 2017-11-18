#!/usr/bin/env python3
import sys
import os.path
import json

from decimal import Decimal


class Config(object):
    def __init__(self, configfile):
        self._config = {}
        self.set_config(configfile)

    def set_config(self, filename):
        if os.path.exists(filename) and filename.endswith('cfg'):
            try:
                with open(filename) as file:
                    for line in file:
                        line_list = line.strip().split(' = ')
                        k = line_list[0]
                        v = line_list[1]
                        self._config[k] = v
                    # print('_config',self._config)
                    return self._config
            except:
                print('Parameter Error')
        else:
            print("Parameter Error")

    def get_config(self, k):
        return self._config[k]


class UserData(object):
    def __init__(self, userdatafile):
        self.userdata = []
        self.set_userdata(userdatafile)

    def set_userdata(self, filename):
        if os.path.exists(filename) and filename.endswith('csv'):
            try:
                with open(filename) as file:
                    line_list = file.readlines()
                    for line in line_list[:-1]:
                        _line = line.strip().split(',')
                        # print('_line',_line)
                        self.userdata.append(_line)
                    # print('userdata', self.userdata)
                    return self.userdata
            except:
                print("Parameter Error")
        return

    def get_usersalary(self):
        return self.userdata

    def calculator(self):
        try:
            SheBaoRate = float(config.get_config('YangLao')) \
                         + float(config.get_config('YiLiao')) \
                         + float(config.get_config('ShiYe')) \
                         + float(config.get_config('GongShang')) \
                         + float(config.get_config('ShengYu')) \
                         + float(config.get_config('GongJiJin'))
            JiShuL = float(config.get_config('JiShuL'))
            JiShuH = float(config.get_config('JiShuH'))
            # print('Sb',SheBaoRate,type(SheBaoRate))
            user_salary = self.get_usersalary()
            # print('user_salary', user_salary)
            data = []
            for i in user_salary:
                salary_info = []
                salary_info.append(int(i[0]))
                salary = int(i[1])
                if salary < JiShuL:
                    taxable_income = 0
                    quick_calculation_deduction = 0
                    tax_rate = 3 / 100
                    # social_security = '%.2f' % (JiShuL * SheBaoRate)
                    social_security = "{:.2f}".format(JiShuL * SheBaoRate).strip()
                    # social_security = float(JiShuL * SheBaoRate)


                elif salary > JiShuL and salary <= 3500:
                    taxable_income = 0
                    quick_calculation_deduction = 0
                    tax_rate = 3 / 100
                    # social_security = '%.2f' % (salary * SheBaoRate)
                    social_security = "{:.2f}".format(salary * SheBaoRate).strip()
                    # social_security = float(salary * SheBaoRate)

                elif salary > 3500 and salary <= JiShuH:
                    taxable_income = salary - salary * SheBaoRate - 3500
                    # social_security = '%.2f' % (salary * SheBaoRate)
                    social_security = "{:.2f}".format(salary * SheBaoRate).strip()
                    # social_security = float(salary * SheBaoRate)

                elif salary > JiShuH:
                    taxable_income = salary - JiShuH * SheBaoRate - 3500
                    # social_security = '%.2f' % (JiShuH * SheBaoRate)
                    social_security = "{:.2f}".format(JiShuH * SheBaoRate).strip()
                    # social_security = float(JiShuH * SheBaoRate)

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
                taxable_amount = format((taxable_income * tax_rate - quick_calculation_deduction), ".2f")
                salary_after_tax = format((salary - float(social_security) - float(taxable_amount)), ".2f")
                # 税前工资, 社保金额, 个税金额, 税后工资

                salary_info.append(i[1])
                salary_info.append(social_security)
                salary_info.append(taxable_amount)
                salary_info.append(salary_after_tax)
                # print('salary_info', type(social_security))
                data.append(salary_info)
            return data
        except:
            print("Parameter Error")

    def dumptofile(self, outputfile):
        result = str(self.calculator()).strip('[[ ]]').replace('[', '\n').replace('],', '')
        # print(result)
        # if os.path.exists(outputfile) and outputfile.endswith("csv"):
        try:
            with open(outputfile, 'w') as file:
                file.write(result)
        except:
            print('Parameter Error')
# configfile = '/home/hope/PycharmProjects/python_calculator/test.cfg'
# userdatafile = '/home/hope/PycharmProjects/python_calculator/user.csv'
# outputfile = '/home/hope/PycharmProjects/python_calculator/gongzi.csv'

if __name__ == "__main__":

    args = sys.argv[1:]
    if len(args) == 6:
        index_c = args.index('-c')
        configfile = args[index_c + 1]
        # print('configfile',configfile)
        index_d = args.index('-d')
        userdatafile = args[index_d + 1]
        # print('userdatafile',userdatafile)
        index_o = args.index('-o')
        outputfile = args[index_o + 1]
        # print('outputfile',outputfile.split('/')[-1])
        config = Config(configfile)
        userdata = UserData(userdatafile)
        userdata.dumptofile(outputfile)
    else:
        print("Parameter Error")
        sys.exit(-1)
    sys.exit(0)
