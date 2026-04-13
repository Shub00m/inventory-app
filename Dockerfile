FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
pipeline {
    agent any

    stages {
        stage('Clone Code') {
            steps {
                git 'https://github.com/Shub00m/inventory-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t inventory-app .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 inventory-app'
            }
        }
    }
}