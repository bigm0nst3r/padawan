package syntax

/**
 * Created by ENSIME
 * @author Sreejith Sreekumar <sreejith.sreekumar@247-inc.com>
 *
 */


object underscore {

  def main(args: Array[String]) = {


    // map function
    println((1 to 5).map(2*))

    // lambda function with more than one statement
    (1 to 5).map { x => val y=x*2; println(y); y}

    //pipeline style anonymous functions
    val filteredList = (1 to 5) filter {_%2 == 0}
    println(filteredList)

    val doubleTest = (1 to 5) map {_*2}
    println(doubleTest)

    // infix sugar
    println(5.+(3))

    // variable number of arguments
    def sum(args: Int*) = args.reduceLeft(_+_)
    println(sum(2,3,5))


    // damn
    def testAbove(args : String*): String = args.reduceLeft(_+ " " + _)
    println(testAbove("foo", "bar "))


    // for each
    val strArray = Array("abc","def","ghi")
    for(a <- strArray){
      println("printing : " + a)
    }


    val numArray : Array[Int] = Array(1,2,3,10)
    val update = for(a <- numArray) yield a * 10
    update.foreach {println}

    println("Done")
    
  }

}
