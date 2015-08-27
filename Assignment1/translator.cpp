#include <fstream>
#include <string>
#include <iostream>
using namespace std;

int main()
{
	ifstream file("32_bit.asm");
	int found;
	string str;
	string st1,st2,st3,st4,st5;
	st1="rax";	st2="rdi";	st3="rsi";	st4="rdx"; st5="syscall";

	while (getline(file, str))
	{
		found=str.find("eax, 4");
		if(found!=string::npos)
			str.replace(found,6,"rax, 1");

		found=str.find("eax, 1");
		if(found!=string::npos)
			str.replace(found,6,"rax, 60");

		found=str.find("eax");
		if(found!=string::npos)
			str.replace(found,st1.length(),st1);

		found=str.find("ebx");
		if(found!=string::npos)
			str.replace(found,st2.length(),st2);

		found=str.find("ecx");
		if(found!=string::npos)
			str.replace(found,st3.length(),st3);
		
		found=str.find("edx");
		if(found!=string::npos)
			str.replace(found,st4.length(),st4);

		found=str.find("int 80h");
		if(found!=string::npos)
			str.replace(found,st5.length(),st5);

		cout<<str<<endl;
	}
	return 0;
}