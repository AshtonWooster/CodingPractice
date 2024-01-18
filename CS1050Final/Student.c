#include <stdio.h>
#include <string.h>

#include "Student.h"

Student InitStudent(char *first, char *last, double gpa) {
	Student student;
	strcpy(student.first, first);
	strcpy(student.last, last);
	student.gpa = gpa;
    
	return student;
}

const char* GetLastName(Student student) {
    char fullName[41];
	strcat(fullName, student.first);
    strcat(fullName, " ");
    strcat(fullName, student.last);

    return fullName;
}

double GetGPA(Student student) {
	return student.gpa;
}