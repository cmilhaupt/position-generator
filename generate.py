import random
import sys

students = []
gds = []
constants = []

def printAll(self):
    for s in students:
        print s.name

def printLeaders(self):
    for l in leaders:
        print l.name

def printGDS(self):
    for g in gds:
        print g.name

def getStudentByNumber(num):
    for student in students:
        if int(student.tid) == num:
            return student.name
    return -1;

class Student:
    def __init__(self, name, role, num):
        self.name = name;
        self.tid = num
        if role == 'g':
            gds.append(self)
            return
        students.append(self)
        if role == 'l' or role == 'r':
            constants.append(self)


for line in open('rosters/tmp-master-roster.txt'):
    line = line.strip('\n')
    person = line.split('|')
    if len(person) == 2:
        s = Student(person[1], person[0], -1)
    if len(person) == 3:
        s = Student(person[1], person[0], person[2])

student_set = set(students)
constant_set = set(constants)

toRandomize = student_set - constant_set
randomize = list(toRandomize)

print '/------------------------------\\'
print '| GDS:                         |'
print '|------------------------------|'
for g in gds:
    string = '| '
    string += g.name
    for i in range(len(string), 31):
        string += ' '
    string += '|'
    print string
print '\------------------------------/'

for i in range(0, random.randint(0, 100)):
    random.shuffle(randomize)

j = 0

for i in range(10, 70):
    s = getStudentByNumber(i)
    if s == -1:
        sys.stdout.write('T')
        print i, '-', randomize[j].name
        j += 1
    else:
        sys.stdout.write('T')
        print i, '-', s
