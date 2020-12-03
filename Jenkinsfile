pipeline {
    agent any
        stages {
            stage ('Build') {
                steps {
                    echo 'Running build phase. '
                    sh   'python file1.py'
                }
            }
           stage('test'){
               steps{
                sh  "echo build tests"
                sh  'export PYTHONPATH=$WORKSPACE:$PYTHONPATH'
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