pipeline {
    agent any

    environment {
        REGISTRY = "docker.io"
        IMAGE_NAME = "ton-dockerhub-username/flask-app"
        IMAGE_TAG = "latest"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ton-repo/flask-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-cred', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
                }
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    sh '''
                        docker stop flask-container || true
                        docker rm flask-container || true
                        docker run -d --name flask-container -p 5000:5000 $IMAGE_NAME:$IMAGE_TAG
                    '''
                }
            }
        }
    }
}
