package data

class Rational(x: Int, y : Int) {

  require(y != 0, "denominator should be non zero")

  private def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)

  def this(x : Int) = this(x, 1)

  private val g = gcd(x,y)
  def numer  = x / g
  def denom = y / g

  def + (that :Rational): Rational = {
    return new Rational(((this.numer * that.denom) + (this.denom * that.numer)), this.denom * that.denom)
  }

  def unary_- : Rational = {
    return new Rational(- this.numer, this.denom)
  }

  def < (that : Rational): Boolean = numer * that.denom < that.numer * denom

  def max(that : Rational): Rational = if(this < that) that else this

  def - (that : Rational): Rational =  this + -that

  override def toString = numer + "/" + denom

}
