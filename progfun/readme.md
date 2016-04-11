


# configure ensime - sbt

 1. go to ~/.sbt/0.13/plugins
 
 2. create the file plugins.sbt   and add the following content

    	       resolvers += Resolver.sonatypeRepo("snapshots")

	       addSbtPlugin("org.ensime" % "ensime-sbt" % "0.1.5-SNAPSHOT")

	       addSbtPlugin("com.typesafe.sbteclipse" % "sbteclipse-plugin" % "2.5.0")

  3. save the file

  4. go to projects folder

  5. create a build.properties file and add the following

     	      sbt.version=0.13.6

  6. save the file

  7. open a terminal in the project folder and type in

     	      sbt gen-ensime

  8. wait till the dependencies are downloaded

  9. go to emacs in where is installed - browse to the project folder

  10. run M-x ensime

  11. this creates the project structure for the scala project and resolves dependenies.


 