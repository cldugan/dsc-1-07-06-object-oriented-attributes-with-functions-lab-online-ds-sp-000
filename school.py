class School():
    def __init__(self, name, roster={}):
        self.name = name
        self.roster = roster
        
    def add_student(self, student_name, grade):
        if grade not in self.roster:
            self.roster[grade] = []
        self.roster[grade].append(student_name)
        
    def grade(self, g):
        return self.roster[g]
    
    def sort_roster(self):
        for x in self.roster:
            self.roster[x].sort()
        return self.roster