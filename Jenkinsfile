pipeline{
    agent none
   stages{
        stage('build'){
        steps{
            sh -c 'echo build file1.py'
            }
        }
        stage('test'){
            sh -c "echo build tests.py"
        }
     post {
        always {
          cobertura coberturaReportFile: '*/.xml'
        }
      }
    }
}
