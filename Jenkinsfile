pipeline {
    agent any
        stages {
            stage ('Build') {
                steps {
                    echo 'Running build phase. '
                    sh   'python file1.py'
                }
            }
           stage('Test'){
               steps{
                sh  "echo build tests"
                sh  'python tests/test_file1.py'
                     }
                }
           stage("Report"){
                 steps {
                    echo "Code Coverage"
                    sh  ''' source activate ${BUILD_TAG}
                            coverage run tests/test_file1.py 1 1 2 3
                            python -m coverage xml -o ./reports/coverage.xml
                        '''
                        }
                 post{
                always{
                    step([$class: 'CoberturaPublisher',
                                   autoUpdateHealth: false,
                                   autoUpdateStability: false,
                                   coberturaReportFile: 'reports/coverage.xml',
                                   failNoReports: false,
                                   failUnhealthy: false,
                                   failUnstable: false,
                                   maxNumberOfBuilds: 10,
                                   onlyStable: false,
                                   sourceEncoding: 'ASCII',
                                   zoomCoverageChart: false])
                }
            }
        }
    }
}
