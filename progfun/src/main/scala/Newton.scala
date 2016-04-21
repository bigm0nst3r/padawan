object Newton {

  def abs(x : Double) : Double = if(x >= 0) x else -x

  def sqIter(guess:Double, x : Double) : Double =
    if(isGoodEnough(guess, x)) guess else sqIter(improve(guess, x), x)

  def isGoodEnough(guess: Double, x : Double) : Boolean =
    abs(guess * guess - x) < 0.001

  def improve(guess : Double, x : Double) =
    (guess + x / guess)/2

  def sqrt(x : Double) : Double =
    sqIter(1.0, x)

  def main(args: Array[String]) = {
    println(sqrt(20))
  }

}


