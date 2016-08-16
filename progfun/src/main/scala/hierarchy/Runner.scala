package hierarchy


object intset {

  def main(args: Array[String]) = {

    val t1 = new NonEmpty(3, new Empty(), new Empty())
    val t2 = t1 incl 4

    println(t2)

  }

}

