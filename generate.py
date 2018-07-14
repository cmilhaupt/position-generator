#! /usr/bin/python

import random
import sys

def usage():
    print 'ERROR: You must pass at least and no more than one argument in the form of a formatted file'
    print ''
    print 'Usage:'
    print '\t./generate.py <file with formatted list of names>'
    sys.exit()

if len(sys.argv) != 2:
    usage()

students = []
gds = []
constants = []

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


try:
    for line in open(sys.argv[1]):
        line = line.strip('\n')
        person = line.split('|')
        if len(person) == 2:
            s = Student(person[1], person[0], -1)
        if len(person) == 3:
            s = Student(person[1], person[0], person[2])

except IOError:
    print 'An error occurred trying to open the file. Please make sure that it exists and try again.'
    sys.exit()

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
