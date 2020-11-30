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
        }
    }