pipeline {
    agent any
    environment {
        PATH = "/usr/local/bin:${env.PATH}"
    }
    stages {
        stage('Verify Tooling') {
            steps {
                sh '''
                    docker --version
                    docker info
                    docker compose version
                    curl --version
                    jq --version
                '''
            }
        }
    }
}
