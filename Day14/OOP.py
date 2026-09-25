class Employee:
  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
  def display(self):
    print ("name:", self.name)
    print ("salary:", self.salary)
  def bonus(self):
    self.salary += 5000
    print("Salary with bonus:",self.salary)

emp1 = Employee("aan", 50000)

emp1.display()
emp1.bonus()
    