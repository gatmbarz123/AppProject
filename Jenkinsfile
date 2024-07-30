pipeline {
   agent any
   stages{
   stage("verify tooling")
     step{
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