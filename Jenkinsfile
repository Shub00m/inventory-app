pipeline {
    agent any

    stages {

        stage('Stop Old Container') {
            steps {
                bat 'docker rm -f inventory-container || exit 0'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t inventory-app .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name inventory-container inventory-app'
            }
        }
    }
}