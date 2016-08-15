


// object DistTrainWithSpark {
//   def main(args: Array[String]): Unit = {
//     if (args.length != 3) {
//       println(
//         "usage: program  num_of_rounds training_path model_path")
//       sys.exit(1)
//     }
//     // if you do not want to use KryoSerializer in Spark, you can ignore the related configuration
//     val sparkConf = new SparkConf().setMaster("local[*]").setAppName("XGBoost-spark-example")
//       .set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
//     sparkConf.registerKryoClasses(Array(classOf[Booster]))
//     val sc = new SparkContext(sparkConf)
//     val sc = new SparkContext(sparkConf)
//     val inputTrainPath = args(1)
//     val outputModelPath = args(2)
//     // number of iterations
//     val numRound = args(0).toInt
//     val trainRDD = MLUtils.loadLibSVMFile(sc, inputTrainPath)
//     // training parameters
//     val paramMap = List(
//       "eta" -> 0.1f,
//       "max_depth" -> 2,
//       "objective" -> "binary:logistic").toMap
//     // use 5 distributed workers to train the model
//     val model = XGBoost.train(trainRDD, paramMap, numRound, nWorkers = 5)
//     // save model to HDFS path
//     model.saveModelToHadoop(outputModelPath)
//   }
// }
