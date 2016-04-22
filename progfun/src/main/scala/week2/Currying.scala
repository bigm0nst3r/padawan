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

  // sum function taking a function as input and returning a function
  // 
  def sum(f: Int => Int): (Int, Int) => Int = {
    def sumF(a: Int, b: Int): Int = {
      if (a > b) 0
      else f(a) + sumF(a + 1, b)
    }
    sumF
  }

  def id = (x : Int) => x

  def main(args: Array[String]) = {
    println(sum (id) (1, 10))
    println("hello")
  }

}
