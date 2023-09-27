pipeline {
    agent any 

    environment {
        TIMESTAMP = "${sh(returnStdout: true, script: 'date +%Y%m%d%H%M%S').trim()}"
    }

    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build and Deploy') {
            steps {
                sh '''
                    # Actual build and deploy commands here
                    # For example:
                    # npm install
                    # npm run build
                '''
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
