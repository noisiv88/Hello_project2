pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
		sh """
		    date > ./README
		    python ./pipelinetask_mail.py -r andriyshvorak@gmail.com -s Build clean ONL from repository patched with my deb packet -m 'Hi' -a README
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
