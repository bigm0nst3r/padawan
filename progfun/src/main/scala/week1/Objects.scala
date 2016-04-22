package week1

object Objects {

  def main(args: Array[String]) = {

    val user = new User("foobar")
    println(user.getName)
    sampleMethod

  }

  private def sampleMethod = {
    val x = 10
  }

}
