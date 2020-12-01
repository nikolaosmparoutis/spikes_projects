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
            sh  "echo build tests.py"
            sh  'python /home/nikoscf/PycharmProjects/test_things/tests/file2.py'
        }

          post {
                always {
                  cobertura coberturaReportFile: '*/.xml'
                }
              }
        }
    }