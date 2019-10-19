#include <iostream>
#include <string>
#include <stack>
#include <sstream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
	string removeSpace(string& s)
	{
		char* printer = &s[0];
		int size = (int)s.size();

		bool inWord = false;
		for (int i = 0; i < size; ++i)
		{
			char ch = s[i];
			if (' ' == ch)
			{
				if (inWord)
				{
					*printer++ = ' ';
					inWord = false;
				}
				else
				{
					continue;
				}
			}
			else
			{
				if (false == inWord)
				{
					inWord = true;
				}
				*printer++ = ch;
			}
		}

		if (*(printer - 1) == ' ')
		{
			printer--;
		}

		return s.substr(0, printer - &s[0]);
	}

	void reverseEachWords(string& s)
	{
		auto end = s.end();

		auto wBegin = s.begin();
		bool inWord = false;
		for (auto it = s.begin(); it != end; ++it)
		{
			if (' ' == *it)
			{
				if (inWord)
				{
					reverse(wBegin, it);
					inWord = false;
				}
				else
				{
					continue;
				}
			}
			else
			{
				if (inWord)
				{
					continue;
				}
				else
				{
					wBegin = it;
					inWord = true;
				}
			}
		}

		if (*(end - 1) != ' ')
		{
			reverse(wBegin, end);
		}
	}

	string reverseWords(string s) {
		reverse(s.begin(), s.end());
		reverseEachWords(s);
		return removeSpace(s);
	}
};