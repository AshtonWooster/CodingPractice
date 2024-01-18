#ifndef STUDENT_H_
#define STUDENT_H_

typedef struct Student_Struct {
    char first[20];
    char last[20];
    double gpa;
} Student;

Student InitStudent(char *first, char *last, double gpa);
const char* GetName(Student student);
double GetGPA(Student student);

#endif