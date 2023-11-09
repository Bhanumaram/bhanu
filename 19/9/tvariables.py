#create an employee class and add details of employee  using three deferent variables and access that variables in all possible ways.
class employee:
    company_name="Marolix technology Pvt Ltd"#using static variable
    print(company_name)
    def __init__(self,name,id,domain,salary):
        self.name=name
        self.id=id
        self.domain=domain
        self.salary=salary
    def employee_details(self):#using instance variable
        print(self.name)
        print(self.id)
        print(self.domain)
        print(self.salary)
    def emp_credentials(self):#using local variable
        emp_surname="Maram"
        Date_of_Birth="05 may 1999"
        print(emp_surname)
        print(Date_of_Birth)
ref_emp=employee(name="Bhanu",id="02079",domain="python",salary="25000")
ref_emp.employee_details()
ref_emp.emp_credentials()