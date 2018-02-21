pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
		sh """
		    date > ./README
		    python ./pipelinetask_mail.py README
		"""
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
