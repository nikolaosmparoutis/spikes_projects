pipeline{
    agent none
    stages{
        stage('build'){
          agent{
            docker{
                image 'python: node-build'
                }
            }
        steps{
            sh  'echo build file1.py'
            sh  'python /home/nikoscf/PycharmProjects/test_things/file1.py'
            }
        }
        stage('test'){
            sh -c "echo build tests.py"
            sh -c 'python /home/nikoscf/PycharmProjects/test_things/tests/file2.py'
        }

          post {
                always {
                  junit 'test-reports/*.xml'
                  step([$class: 'CoberturaPublisher',
                  autoUpdateHealth: false,
                  autoUpdateStability: false,
                  coberturaReportFile: '**/coverage.xml',
                  failUnhealthy: false,
                  failUnstable: false,
                  maxNumberOfBuilds: 0,
                  onlyStable: false,
                  sourceEncoding: 'ASCII',
                  zoomCoverageChart: false])
                }
              }
    }
}
