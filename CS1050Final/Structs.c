#include <stdio.h>
#include <string.h>
#include "Student.h"

int main() {
    Student newStudent = InitStudent("Ashton", "Wooster", 4.0);

    printf("%s", GetName(newStudent));

    return 0;
}