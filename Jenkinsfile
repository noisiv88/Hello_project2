pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
		sh """
		    date > ./README
		    python ./pipelinetask_mail.py -r andriy.shvorak@plvision.eu andriyshvorak@gmail.com -s ${env.BUILD_STATUS}  -m 'Hi' -a README
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
