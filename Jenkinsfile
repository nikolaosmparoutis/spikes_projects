pipeline {
    agent any
        stages {
            stage ('Build') {
                steps {
                    echo 'Running build phase. '
                    sh   'echo build file1.py'
                    sh   'python file1.py'
                }
            }
           stage('test'){
               steps{
                sh  "echo build tests.py"
                sh  'python tests/file2.py'
                }
            }
           stage("report"){
              steps{
                  post {
                        always {
                          cobertura coberturaReportFile: '*/.xml'
                        }
                    }
                }
           }
        }
    }