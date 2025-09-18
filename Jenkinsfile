pipeline {
    agent any

    environment {
        IMAGE_NAME = "bbabadara/remove_bg_app"
        IMAGE_TAG = "latest"
        DOCKER_REGISTRY = "docker.io"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'jenkins', url: 'https://github.com/bbabadara/remove_bg_app_python'
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
                withCredentials([usernamePassword(credentialsId: 'dockerhub_credential', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push $IMAGE_NAME:$IMAGE_TAG'
                }
            }
        }
        
        stage('Deploy to Render') {
            steps {
                withCredentials([string(credentialsId: 'render_credential', variable: 'RENDER_API_KEY')]) {
                    sh '''
                    curl -X POST "https://api.render.com/deploy/srv-xxxxxxxxxxxxxxxx" \
                    -H "Authorization: Bearer $RENDER_API_KEY" \
                    -H "Content-Type: application/json" \
                    -d '{"clearCache": true}'
                    '''
                }
            }
        }

       
    }
}
