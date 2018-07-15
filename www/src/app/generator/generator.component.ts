import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-generator',    
    templateUrl: './generator.component.html',    
    styleUrls: ['./generator.component.css']
})
export class GeneratorComponent implements OnInit {

    tag: string;
    data: any;
    gds: Student[] = [];
    students: Student[] = [];
    constants: Student[] = [];
    list: string[] = [];

    constructor() { }

    ngOnInit() {
    }

    load(e) {
        this.gds = [];
        this.students = [];
        this.constants = [];
        this.list = [];
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
        var check: boolean = true;
        for(var student of this.data) {
            if(check) {
                this.tag = student;
                check = false;
                continue;
            }
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
        this.shuffleStudents();
    }
    
    shuffleStudents() {
        var m = this.students.length, t, i;

        while(m) {
            i = Math.floor(Math.random() * m--);

            t = this.students[m];
            this.students[m] = this.students[i];
            this.students[i] = t;
        }
        
        for(var constant of this.constants) {
            this.students.push(constant);
        }
       
        this.assign();
    }

    assign() {
        var j = 0;
        for(var i = 0; i < this.students.length; i++) {
            if(this.idIsFree(i + 10)) {
                this.students[j++].id = i + 10;
            }
        }
        this.sort();
    }
    
    idIsFree(i: number): boolean {
        for(var student of this.students) {
            if(student.id == i) {
                return false;
            }
        }
        return true;
    }

    sort() {
        this.students.sort(this.compare);
    }

    compare(a, b) {
        if (a.last < b.last)
            return -1;
        if (a.last > b.last)
            return 1;
        return 0;
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
