// Jenkinsfile
pipeline {
    agent any

    stages {
        stage('Construcción') {
            steps {
                script {
                    // Instalar dependencias
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Pruebas') {
            steps {
                script {
                    // Ejecutar pruebas
                    sh 'pytest tests/'
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/*.py', fingerprint: true
        }
    }
}
