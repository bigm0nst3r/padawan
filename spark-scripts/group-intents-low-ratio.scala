val inputDataUrl = "file:///home/sreejith.sreekumar/experiment/FirstResponses_WCNormalized"
val csv = sc.textFile(inputDataUrl)
case class Utterance(id: String, text: String, intent: String) {
}
val data = csv.map(line => line.split("\t").map(elem => elem.trim)).filter(elements => elements.length == 4)
def getIntent(x: Array[String]): String = x(2)
val utteranceDF = data.map(attributes => Utterance(attributes(0), attributes(1), attributes(2))).toDF()
val distinct_intents = data.map(getIntent).distinct()
val counts = utteranceDF.groupBy("intent").count()
val total = utteranceDF.count()
val countsRDD = counts.rdd
val ratio_rdd = countsRDD.map(row => (row(0), row(1).toString.toFloat/total))
val ratioMap = ratio_rdd.collectAsMap()
def isLow(intent : String) : String = if(ratioMap(intent) < 0.00166) "Other" else intent
val update = data.map(row => (row(0), row(1), row(2), ratioMap(row(2)), isLow(row(2))))
