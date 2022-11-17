#define _CRT_SECURE_NO_WARNINGS 1

#include<iostream>
#include<iomanip>

using namespace std;

class Student
{
public:
	//friend void Display(Student s);

	friend class Teacher;

	Student(const string& id = "0000", const string& name = "LiHua", const int& score = 0)
		: _id(id)
		, _name(name)
		, _score(score)
	{}

private:
	string _id;
	string _name;
	int _score;
};

class Teacher
{
public:
	void Display(const Student& s) const
	{
		if (s._score >= 90)
			cout << left << setw(20) << s._name << setw(20)
			<< s._score << setw(20) << "����" << endl;
		else if (s._score >= 80 && s._score <= 89)
			cout << left << setw(20) << s._name << setw(20)
			<< s._score << setw(20) << "����" << endl;
		else if (s._score >= 70 && s._score <= 79)
			cout << left << setw(20) << s._name << setw(20)
			<< s._score << setw(20) << "�е�" << endl;
		else if (s._score >= 60 && s._score <= 69)
			cout << left << setw(20) << s._name << setw(20)
			<< s._score << setw(20) << "�ϸ�" << endl;
		else
			cout << left << setw(20) << s._name << setw(20)
			<< s._score << setw(20) << "���ϸ�" << endl;
	}

	void Modifly(const int& score, Student& s) const
	{
		s._score = score;
	}
};

void Menu()
{
	cout << left << setw(20) << "����" << setw(20)
		<< "�ɼ�" << setw(20) << "�ȼ�" << endl;
	cout << "--------------------------------------------" << endl;
}

int main()
{
	Menu();
	Teacher t;
	Student s1("0512", "HuiGu", 90);
	const Student s2("0513", "LingLing", 80);
	t.Display(s1);
	t.Display(s2);
	t.Modifly(80, s1);
	t.Display(s1);
	return 0;
}