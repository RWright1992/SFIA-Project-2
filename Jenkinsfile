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
		sh 'pip3 install ansible'
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
                sh 'ls'
                }
        }
        }
}
