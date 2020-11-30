pipeline {
    agent any
        stages {
            stage ('Build') {
                steps {
                    echo 'Running build phase. '
                    sh  'echo build file1.py'
                    sh  'python  https://github.com/nikolaosmparoutis/spikes_projects/test_things/file1.py'
                }
            }
        }
    }