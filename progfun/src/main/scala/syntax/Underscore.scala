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

    


    println("Done")
    
  }

}
