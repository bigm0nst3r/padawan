package data



class Rational(x: Int, y : Int) {

  private def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b)

  def numer  = x
  def denom = y

  def add(that :Rational): Rational = {
    return new Rational(((this.numer * that.denom) + (this.denom * that.numer)), this.denom * that.denom)
  }

  def neg: Rational = {
    return new Rational(- this.numer, this.denom)
  }


  def sub(that : Rational): Rational =  add(that.neg)



  override def toString = numer + "/" + denom

}
