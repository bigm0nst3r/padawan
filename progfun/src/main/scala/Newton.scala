object Newton {

  def sqrt(x: Double) = {

    def abs(x: Double): Double = if (x >= 0) x else -x

    def sqIter(guess: Double): Double =
      if (isGoodEnough(guess)) guess else sqIter(improve(guess))

    def isGoodEnough(guess: Double): Boolean =
      abs(guess * guess - x) < 0.001

    def improve(guess: Double) =
      (guess + x / guess) / 2

    sqIter(1.0)
  }

  def main(args: Array[String]) = {
    println(sqrt(20))
  }

}

