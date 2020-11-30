pipeline {
    agent any
        stages {
            stage ('Build') {
                steps {
                    echo 'Running build phase. '
                    sh   'echo build file1.py'
                    sh   'python -m /test_things/file1.py'
                }
            }
        }
    }