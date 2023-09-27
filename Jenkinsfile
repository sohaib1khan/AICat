pipeline {
    agent any 

    environment {
        MY_VARIABLE = 'some_value'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build and Deploy') {
            steps {
                sh 'your build and deploy commands here'
            }
        }
    }
    
    post {
        always {
            sh 'echo "This will always run"'
        }
        
        success {
            sh 'echo "This will run only if the pipeline is successful"'
        }
        
        failure {
            sh 'echo "This will run only if the pipeline fails"'
        }
    }
}
