#include <iostream>
#include <math.h>
#include <typeinfo>
#include <list>
#include <iterator>
#include <vector>
using namespace std;

// HW04 P1

/*
int intersection(int st, int ave){
	double cant_pair;
	cant_pair = (st + ave)*(st+ave+1)/2 + ave;
	return cant_pair;
}

int w(int z){
	int w_val;
	w_val = int(pow(8*z + 1, 0.5) -1) /2;
	return w_val; 
}

//auto w = [](int z){int(pow(8*z+1,0.5) - 1)/2 ; };

int avenue(double inter){
	double ave;
	ave = inter - (pow(w(inter), 2) + w(inter))/2;
	return ave;
}


int street(double inter){
	double str;
	str = w(inter) - avenue(inter);
	return str;
}

int taxicab(int a, int b){
	int str1, ave1, str2, ave2;
	str1 = street(a), ave1 = avenue(a);
	str2 = street(b), ave2 = avenue(b);
	return abs(str1 - str2) + abs(ave1 - ave2);
}

int main(){
	int times_square;
	int ess_a_bagel;
	int x1, y1, x2, y2;
	cout << "Enter coordinates for point 1" << endl;
	cin >> x1;
	cin >> y1;
	cout << "Enter coordinates for point 2" << endl;
	cin >> x2;
	cin >> y2;
	times_square = intersection(x1, y1);
	ess_a_bagel = intersection(x2, y2);
	cout << "The taxicab distance is " << taxicab(times_square, ess_a_bagel) << endl;
	return 0;
}

*/

//HW 04 P2

/*
vector<int> square(vector<int> s){
	vector<int> out;
	for(int it = 0; it < s.size(); it++){
		if(round(pow(s[it], 0.5)) - pow(s[it],0.5) == 0){
			out.push_back(round(pow(s[it], 0.5)));
		}
	}
	return out;
}

int main(){
	vector<int> inp_vector = {8, 49, 8, 9, 2, 1, 100, 102};
	vector<int> out_vector = square(inp_vector);
	for (std::vector<int>::const_iterator i = out_vector.begin(); i != out_vector.end(); i++)
		std::cout << *i << ' ' << endl;
	//cout << "The output vector is " << square(inp_vector) << endl;
	return 0;
}
*/

//HW 04 P3

/*
int g_recursive(int x){
	if(x <= 3) {
		return x;
	} else{
		return g_recursive(x-1) + 2 * g_recursive(x-2) + 3 * g_recursive(x-3);
	}
}

int g_iterative(int x){
	if(x <= 3){
		return x;
	} else {
		int i = 3;
		int curr = 3;
		int prev_val = 2;
		int prev_prev_val = 1;
		int total = 0;
		while(i < x){
			total = curr + 2 * prev_val + 3 * prev_prev_val;
			prev_prev_val = prev_val;
			prev_val = curr;
			curr = total;
			i = i +1;
		}
		return total;
	}
}

int main(){
	int input;
	cout << "Please enter a value " << endl;
	cin >> input;
	cout << "The recursive output of g is " << g_recursive(input) << endl;
	cout << "The iterative output of g is " << g_iterative(input) << endl;
	return 0;
}
*/

