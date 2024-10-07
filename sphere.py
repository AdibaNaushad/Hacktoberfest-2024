// CPP program to calculate Volume and 
// Surface area of Sphere 
#include<bits/stdc++.h> 
using namespace std; 

// Initializing Value Of PI 
float pi = 3.14159; 

// Function To Calculate Volume Of Sphere 
float volume(float r) 
{ 
	float vol; 
	vol = (float(4) / float(3)) * pi * r * r * r; 
	return vol; 

} 

// Function To Calculate Surface Area of Sphere 
float surface_area(float r) 
{ 
	float sur_ar; 
	sur_ar = 4 * pi * r * r; 
	return sur_ar; 
} 

// Driver Function 
int main() 
{ 
	float radius = 12; 
	float vol, sur_area; 
	
	// Function Call 
	vol = volume(radius); 
	sur_area = surface_area(radius); 

	// Printing Value Of Volume And Surface Area 
	cout << "Volume Of Sphere :" << vol << endl; 
	cout << "Surface Area Of Sphere :" << sur_area << endl; 
	return 0; 
} 
