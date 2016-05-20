package week2

object Currying {

  def cube(x: Int): Int = {
    x * x * x
  }

  def sumAccumulator(f: Int => Int, a: Int, b: Int): Int = {
    def loop(a: Int, acc: Int): Int = {
      if (a > b) acc else loop(a + 1, acc + f(a))
    }

    loop(a, 0)

  }

  // earlier we passed a function and two arguments to the sum function

  /**
   * different method
   * define a function that takes a function parameter on which a - b has to be applied
   * return a function which takes a and b and applies f on all element in it
   */
  // sum function taking a function as input and returning a function
  def sum(f: Int => Int): (Int, Int) => Int = {

    def sumF(a: Int, b: Int): Int = {
      if (a > b) 0
      else f(a) + sumF(a + 1, b)
    }

    sumF
  }

  def id = (x: Int) => x

  def square = (x : Int) => x*x

  def main(args: Array[String]) = {


     // now, when we call sum(fun) we have a function which will apply fun on the
     // next set of arguments
     // function application associates to the left
   println(sum(id)(1, 10))
    println(sum(square)(3, 4))



  }

}

