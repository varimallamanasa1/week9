pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                echo "Building Docker Image..."
                bat 'docker build -t kubdemoapp:v1 .'
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging into Docker Hub..."
                bat 'docker login -u vishnupriya68 -p "Shivapriya123@"'
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Pushing Docker Image to Docker Hub..."
                bat 'docker tag kubdemoapp:v1 vishnupriya68/sample1:kubeimage1'
                bat 'docker push vishnupriya68/sample1:kubeimage1'
            }
        }

        stage('Deploy to Kubernetes') {
        steps {
        echo "Deploying to Kubernetes..."
        withEnv(['KUBECONFIG=C:\\Users\\Vishnupriya\\.kube\\config']) {
            bat 'kubectl apply -f deployment.yaml --validate=false'
            bat 'kubectl apply -f service.yaml'
        }
    }
}

    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
