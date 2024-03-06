pipeline {
    agent any
    
    environment {
        // Define environment variables if needed
        // Example:
            JAVA_HOME = '/path/to/java'
            MAVEN_HOME = '/path/to/maven'
    }

    stages {
       
        /*stage('Build') {
            steps {
                // Build the Spring Boot application using Maven
                script {
                    sh 'mvn clean package'
                }
            }
        }*/

        stage('Deploy') {
            steps {
                // Run the Spring Boot application
                script {
                    sh 'java -jar demo/target/demo-0.0.1-SNAPSHOT.jar'
                }
            }
        }
    }
}
