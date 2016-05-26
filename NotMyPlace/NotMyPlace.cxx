/*
 * NotMyPlace.cxx
 * 
 * Copyright 2016 Nathan Oesterle <nathan@nathan-C55B>
 * 
 */
 
#include <iostream>
#include <stdlib.h>
#include <string>
#include <sstream>

int main(int argc, char **argv)
{
	int MS = 12; //Place you finished in.
	int MAX = 100; //Total number of places.
	std::string VAL; //String of current place that isn't yours.
	for(int i=1; i<= MAX; i++){
		if (i != MS){
			//Make current place a string.
			std::stringstream ss;
			ss <<"";
			ss << i;
			VAL = ss.str(); //Make current place a string
			char last;
			//Gets last character in place sting.
			last = VAL.at(VAL.length() -1);
			
			//Check special cases.
			if (last == '1' and VAL != "11"){
				std::cout << VAL<<"st ";
			}
			else if (last == '2' and VAL != "12"){
				std::cout << VAL<<"nd ";
			}
			else if (last == '3' and VAL != "13"){
				std::cout << VAL<<"rd ";
			}
			//Not a special case.
			else{
				std::cout << VAL<<"th ";
			}
		};
	};
	return 0;
}

