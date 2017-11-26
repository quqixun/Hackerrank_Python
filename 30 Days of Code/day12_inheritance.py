class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
        
class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNum, scores):
        super().__init__(firstName, lastName, idNum)
        self.scores = scores
        self.avg_score = sum(scores) / len(scores)
        
        return

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        if self.avg_score >= 90 and self.avg_score <= 100:
            return "O"
        elif self.avg_score >= 80 and self.avg_score < 90:
            return "E"
        elif self.avg_score >= 70 and self.avg_score < 80:
            return "A"
        elif self.avg_score >= 55 and self.avg_score < 70:
            return "P"
        elif self.avg_score >= 40 and self.avg_score < 55:
            return "D"
        elif self.avg_score >= 0 and self.avg_score < 40:
            return "T"
        else:
            print("Unknown")

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
