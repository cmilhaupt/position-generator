import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-generator',    
    templateUrl: './generator.component.html',    
    styleUrls: ['./generator.component.css']
})
export class GeneratorComponent implements OnInit {

    data: any;
    gds: Student[] = new Array();
    students: Student[] = [];
    constants: Student[] = [];
    list: string = [];

    constructor() { }

    ngOnInit() {
    }

    load(e) {
        this.data = e.split("\n");
        this.process();
    }
    
    test(student: Student) {
        console.log(student.getFirst());
        console.log(student.getLast());
        console.log(student.getId());
        console.log(student.getRole());
    }

    process() {
        for(var student of this.data) {
            var s = student.split('|');
            var stud: Student;
            if (s.length === 2) {
                stud = new Student(s[0], s[1], -1);
            } else if (s.length === 3) {
                stud = new Student(s[0], s[1], s[2]);
            } else {
                console.log('Error with student parsing');
            }

            if (stud.getRole() === 'g') {
                this.gds.push(stud);
            } else if (stud.getRole() === 'c') {
                this.constants.push(stud);
            } else if (stud.getRole() === 'm') {
                this.students.push(stud);
            } else {
                console.log('Error with student role');
            }
        }
    }
}

class Student {
    name: string;
    first: string;
    last: string;
    id: number;
    role: string;

    constructor(role: string, name: string, id: number) {
        this.name = name;
        this.id = id;
        var tmp = name.split(' ');
        this.first = tmp[0];
        this.last = tmp[1];
        this.role = role;
    }

    getFirst() {
        return this.first;
    }

    getLast() {
        return this.last;
    }

    getId() {
        return this.id;
    }

    getRole() {
        return this.role;
    }
}
