pipeline {
    agent any
        stages {
            stage ('Build') {
                steps {
                    echo 'Running build phase. '
                    sh   'echo build file1'
                    sh   'python file1.py'
                }
            }
           stage('test'){
               steps{
                sh  "echo build tests"
                sh  'python file1.py'
                sh  'echo $PATH'
                sh   'echo $PYTHONPATH'
                sh  'python tests/test_file1.py'
                 }
                }
           stage("report"){
              steps{
                  cobertura coberturaReportFile: '/var/lib/jenkins/workspace/spikes_job_/coverage.xml'
                }
           }
        }
    }