class CSP:
    def __init__(self, variables, domains, constraints):
        self.variables = variables
        self.domains = domains  
        self.constraints = constraints 

    def is_consistent(self, assignment):
        for constraint in self.constraints:
            if not constraint(assignment):
                return False
        return True

    def backtracking_search(self):
        return self.backtrack({}, self.variables)

    def backtrack(self, assignment, unassigned_variables):
        if not unassigned_variables:
            return assignment
        
        var = unassigned_variables[0]
        for value in self.domains[var]:
            new_assignment = assignment.copy()
            new_assignment[var] = value
            if self.is_consistent(new_assignment):
                result = self.backtrack(new_assignment, unassigned_variables[1:])
                if result is not None:
                    return result
        return None


def not_equal_constraint(assignment):
    if 'A' in assignment and 'B' in assignment:
        return assignment['A'] != assignment['B']
    return True

variables = ['A', 'B']
domains = {'A': [1, 2, 3], 'B': [1, 2, 3]}
constraints = [not_equal_constraint]

csp = CSP(variables, domains, constraints)
solution = csp.backtracking_search()
print("Solution:", solution)
