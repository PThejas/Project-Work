#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def show_employee(ename, sal):
    if sal > 10000:
        grade = 'Manager'
    else:
        grade = 'Consultant'
    print("Employee Name : " + ename)
    print(f"Employee Name :{ename}")
    print('Salary : ' + str(sal))
    print("Grade : " + grade)

show_employee('DEF',100000)

