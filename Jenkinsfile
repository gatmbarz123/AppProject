pipeline {
    agent any
    stages {
        stage('Verify Tooling') {
            steps {
                sh '''
                    docker version
                    docker info
                    docker compose version
                    curl --version
                    jq --version
                '''
            }
        }
    }
}
