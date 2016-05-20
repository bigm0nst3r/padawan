

object Exercise {

  def product(f: Int => Int)(a: Int, b: Int): Int = {
    if (a > b) 1 else f(a) * product(f)(a + 1, b)
  }

  def fact(n: Int): Int = {
    product(x => x)(1, n)

  }


  

  def main(args: Array[String]) = {
    println(product(x => x * x)(3, 7))
    println(fact(5))
  }

}

