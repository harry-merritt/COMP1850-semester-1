# About Me

### Languages Known:
* Python
* C++ (almost)
* C# (a little)
* English

### My favourite function:

~~~C
float Q_rsqrt( float number )
{
	long i;
	float x2, y;
	const float threehalfs = 1.5F;

	x2 = number * 0.5F;
	y  = number;
	i  = * ( long * ) &y;                      
	i  = 0x5f3759df - ( i >> 1 );               
	y  = * ( float * ) &i;
	y  = y * ( threehalfs - ( x2 * y * y ) );   
//	y  = y * ( threehalfs - ( x2 * y * y ) );   

	return y;
}
~~~
All credit to the Quake III development team. Code originates from [here](https://github.com/id-Software/Quake-III-Arena/blob/master/code/game/q_math.c).

