pipeline{
    agent any
   stages{
        stage('build'){
        steps{
            sh  'echo build file1.py'
            }
        }
        stage('test'){
            sh  "echo build tests.py"
        }
     post {
        always {
          cobertura coberturaReportFile: '*/.xml'
        }
      }
    }
}
