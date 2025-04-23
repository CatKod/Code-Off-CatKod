#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Student {
    string name;
    float mathMark;
};

int main() {
    int numStudents;
    cout << "Enter the number of students: ";
    cin >> numStudents;

    vector<Student> students(numStudents);

    for (int i = 0; i < numStudents; ++i) {
        cout << "Enter name of student " << i + 1 << ": ";
        cin >> students[i].name;
        cout << "Enter Math mark of " << students[i].name << ": ";
        cin >> students[i].mathMark;
    }

    cout << "\nStudents who haven't passed the Math exam (score < 4):\n";
    for (const auto& student : students) {
        if (student.mathMark < 4) {
            cout << student.name << endl;
        }
    }

    return 0;
}
