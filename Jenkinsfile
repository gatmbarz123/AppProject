pipeline {
    agent any
    stages {
        stage('Verify Tooling') {
            steps {
                script {
                    echo "Current PATH: ${env.PATH}"
                    sh '''
                        echo "Docker version:"
                        docker --version || echo "Docker is not installed or not accessible"
                        echo "Docker info:"
                        docker info || echo "Unable to retrieve Docker info"
                        echo "Docker Compose version:"
                        docker compose version || echo "Docker Compose is not installed or not accessible"
                        echo "Curl version:"
                        curl --version || echo "Curl is not installed or not accessible"
                        echo "jq version:"
                        jq --version || echo "jq is not installed or not accessible"
                    '''
                }
            }
        }
    }
}


