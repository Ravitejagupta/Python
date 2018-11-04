"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def __init__(self):
        self.ans = 0
        
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        d = {}
        for employee in employees:
            d[employee.id] = [employee.importance, employee.subordinates]
        self.helper(d, id)
        return self.ans
    
    def helper(self, d, id):
        self.ans += d[id][0]
        for i in d[id][1]:
            self.helper(d, i)
            
