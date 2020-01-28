pipeline{

        agent any
        environment{
                git_repo = "https://github.com/TomLLew/DwarvenGenerator.git"
                build = "${BUILD_NUMBER}"
        }

        stages{

                stage('clone updated git repo'){

                        steps{
                                sh '''
                                cd ~ 
                                rm -rf DwarvenGenerator
                                export BUILD_NUMBER=${BUILD_NUMBER}
                                git clone ${git_repo}
                                '''
                        }
                }
                stage('compose build'){
                        steps{
                                sh ''' 
                                cd ~
                                cd DwarvenGenerator
                                git checkout kuber
                                docker-compose up -d --build
                                '''
                        }
                }
                stage('image push to registry'){
                        steps{
                                sh '''
                                cd ~
                                cd DwarvenGenerator
                                docker-compose down
                                docker-compose push
                                docker system prune -f
                                '''
                        }
                }
                stage('kubectl service update'){
                        steps{
                                sh '''
                                export BUILD_NUMBER=${BUILD_NUMBER}
                                cd ~
                                cd DwarvenGenerator/kuber-test/
                                kubectl apply -f dwarven-generator-kuber.yaml
                                '''
                        }
                }
        }                
}