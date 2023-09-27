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
        
        stage('Build Docker Image') {
            steps {
                sh '''
                    # Build the Docker image locally
                     docker build -t aicat .
                '''
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                // Replace 'your-credentials-id' with the Jenkins credential ID for your Docker Hub account
                withCredentials([usernamePassword(credentialsId: '14fde496-447e-4e10-ae06-5979860090c3', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
                    sh '''
                        # Login to Docker Hub
                        echo "$DOCKERHUB_PASSWORD" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin

                        # Tag the image; replace 'your-dockerhub-repo' with your Docker Hub repository name
                        docker tag my_app:latest $DOCKERHUB_USERNAME/bluedreamz/aicat:latest

                        # Push the image to Docker Hub
                        docker push $DOCKERHUB_USERNAME/bluedreamz/aicat:latest
                    '''
                }
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
