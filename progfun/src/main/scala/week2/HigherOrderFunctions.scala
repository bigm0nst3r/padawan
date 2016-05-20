package week2

object HigherOrder {

  def cube(x: Int): Int = {
    x * x * x
  }

  def sumInts(a: Int, b: Int): Int = {
    if (b < a) 0 else a + sumInts(a + 1, b)
  }

  def sumCube(a: Int, b: Int): Int = {
    if (a < b) 0 else cube(a) + sumCube(a + 1, b)
  }

  /**
   * adding a higher order function
   *
   */
  def sum(f: Int => Int, a: Int, b: Int): Int = {
    if (b < a) 0 else f(a) + sum(f, a + 1, b)
  }

  // adding accumulator to the function
  def sumAccumulator(f: Int => Int, a: Int, b: Int): Int = {

    def loop(a: Int, acc: Int): Int = {
      if (a > b) acc else loop(a + 1, acc + f(a))
    }

    loop(a, 0)

  }

  def main(args: Array[String]) = {
    println(sumInts(1, 3))
    println(sum(cube, 1, 3))
    println(sumAccumulator(cube, 1, 3))
  }



}
