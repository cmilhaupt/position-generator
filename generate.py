#! /usr/bin/python

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
        if student.tid == num:
            return student
    return -1;

class Student:
    def __init__(self, name, role, num):
        self.name = name
        fullname = name.split(' ')
        self.first = fullname[0]
        self.last = fullname[1]
        self.tid = int(num)
        if role == 'g':
            gds.append(self)
        elif role == 'c':
            constants.append(self)
        elif role == 'm':
            students.append(self)
        else:
            print 'Incorrect marking for student', name
            print 'Please correct and run again.'
            print 'Exiting...'


for line in open('rosters/tmp-master-roster.txt'):
    line = line.strip('\n')
    person = line.split('|')
    if len(person) == 2:
        s = Student(person[1], person[0], -1)
    if len(person) == 3:
        s = Student(person[1], person[0], person[2])

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
print ''
print 'Assignments in alphabetical order'
print '----------------------------------'

for i in range(0, random.randint(0, 100)):
    random.shuffle(students)

for i in range(len(constants)):
    students.append(constants[i])

j = 0
for i in range(10, 70):
    if getStudentByNumber(i) == -1:
        students[j].tid = i
        j += 1

students.sort(key=lambda x: x.last)

for student in students:
    sys.stdout.write(student.last + ", " + student.first + ": ")
    print "T" + str(student.tid)
