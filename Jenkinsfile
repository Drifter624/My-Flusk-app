// Jenkinsfile
pipeline {
    agent {
        docker {
            image 'python:3.9' // Usar una imagen de Python
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

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
