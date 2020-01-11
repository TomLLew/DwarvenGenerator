pipeline{

        agent any
        environment{
                swarm_ip = "swarm-test"
                git_repo = "https://github.com/TomLLew/DwarvenGenerator.git"
        }

        stages{

                stage('clone updated git repo'){

                        steps{
                                sh ''' 
                                sudo rm -rf DwarvenGenerator
                                git clone ${git_repo}
                                '''
                        }
                }
                stage('compose build'){
                        steps{
                                sh '''
                                export BUILD_NUMBER='${BUILD_NUMBER}'
                                cd DwarvenGenerator
                                docker-compose up -d --build
                                '''
                        }
                }
                stage('image push to registry'){
                        steps{
                                sh '''
                                cd DwarvenGenerator
                                docker-compose down
                                docker-compose push
                                '''
                        }
                }
                stage('service update'){
                steps{
                        sh '''ssh ${swarm_ip} << EOF
                                export BUILD_NUMBER='${BUILD_NUMBER}'
                                docker service update --replicas 4 --image jenkins-test:5000/service1:server-${BUILD_NUMBER} DwarvenGenerator_service1
                                docker service update --replicas 4 --image jenkins-test:5000/service2:server-${BUILD_NUMBER} DwarvenGenerator_service2
                                docker service update --replicas 4 --image jenkins-test:5000/service3:server-${BUILD_NUMBER} DwarvenGenerator_service3
                                docker service update --replicas 4 --image jenkins-test:5000/frontend:server-${BUILD_NUMBER} DwarvenGenerator_frontend
                                EOF
                                '''
                        }
                }
        }                
}