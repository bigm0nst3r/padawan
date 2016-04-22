package week2

object Tail {

  def factorial(x: Int): Int = {

    def loop(acc: Int, n: Int) : Int = {
      if (n == 0) acc
      else loop(acc * n, n-1)
    }
    loop(1, x)
  }

  def main(args: Array[String]) = {
    println(factorial(10))
    
  }

}
