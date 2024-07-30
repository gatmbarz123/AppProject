pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:${env.PATH}"
    }

    stages {
        stage('Check PATH') {
            steps {
                sh 'echo $PATH'
            }
        }

        stage('Verify Tooling') {
            steps {
                sh '''
                    docker --version
                    docker info
                    docker-compose --version
                    curl --version
                    jq --version
                '''
            }
        }
    }
}

