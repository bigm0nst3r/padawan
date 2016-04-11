



def square(x : Double) = x*x

def sumOfSquares(x:Double , y : Double) = square(x)+ square(y)

println(square(2))

/**
 * Function evaluation strategy 1 - call by value - arguments are evaluated before function calls
 * 
 */ 
//expressions are evaluated from left to right using the substitution model
// first arguments are evaluated - then it is applied on the function

// sumOfSquares(3*3, 4)
// sumOfSquares(9, 4)
// square(9) + square(4)
// 9*9 + square(4)
// 81 + 4*4
// 81 + 16
// 97


// substitution model can be applied only on expression which do not have a side effect. 
// side effect - eg : c++  : incrementing a value c and returning a value at the same time.
 


// not all functions can be reduced off to a single value
// eg.
def loop : Int = loop

 

/**
 * Function evaluation strategy 2 - call by name - if arguments are unused, they are  not evaluated
 * 
 */ 
// applying arguments on functions without reducing them
// sumOfSquares(3, 2+2)
// square(3) + square(2+2)
// 3*3 + square(2+2)
//9 + (2+2) * (2+2)
//9 + 4 * (2+2)
//9 + 4 + 4
//9 + 8
//17
