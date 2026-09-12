class Employee:
    def work(self):
        print("Employee is working")


class Developer(Employee):
    def work(self):
        print("Developer is coding")


class Manager(Employee):
    def work(self):
        print("Manager is managing")


for emp in [Developer(), Manager()]:
    emp.work()
