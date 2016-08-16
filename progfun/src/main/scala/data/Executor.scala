package data

object rationals {

  def main(args: Array[String]) = {

    val i = new Rational(1, 2)
    val j = new Rational(1, 2)
    println(i.numer)
    println(i.denom)

    println(i.toString())

    println(-i)

    // val k = new Rational(1,0)

    println(i + j)

    
    

  }

}
