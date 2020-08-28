pipeline{
        agent any
        stages{
        stage('Clone Repo'){
                steps{
                sh 'git fetch https://github.com/RWright1992/SFIA-Project-2.git dev'
                }
        }
        stage('Install Pytest + Python'){
                steps{
                sh 'sudo apt update && sudo apt install -y python3 python3-pip'
                sh 'pip3 install pytest'
                sh 'pip3 install Flask-Testing'
                }
        }
	stage('Install docker + docker compose + build images + push'){
	steps{
        	sh 'curl https://get.docker.com | sudo bash'
		sh 'sudo curl -L "https://github.com/docker/compose/releases/download/1.26.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose'
		sh 'sudo chmod +x /usr/local/bin/docker-compose'
		sh 'cd SFIA-Project-2/'
		sh 'sudo docker-compose build'
		sh 'sudo docker-compose push'
                }
	}
        stage(Test){
                steps{
                sh 'cd SFIA-Project-2/service1 && pip3 install -r requirements.txt'
                sh 'cd SFIA-Project-2/service1 && python3 -m pytest'
                sh 'cd ..'
                sh 'cd SFIA-Project-2/service2 && pip3 install -r requirements.txt'
                sh 'cd SFIA-Project-2/service2 && python3 -m pytest'
                sh 'cd ..'
                sh 'cd SFIA-Project-2/service3 && python3 -m pytest'
                sh 'cd ..'
                sh 'cd SFIA-Project-2/service4 && python3 -m pytest'
                }
        }
        stage('Deploy'){
                steps{
		
                sh '/home/jenkins/.local/bin/ansible-playbook -v -i inventory playbook.yaml'
                }
        }
        }
}
