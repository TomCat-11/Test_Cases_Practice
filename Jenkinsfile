pipeline {
    agent any

    environment {
        PYTHON = "python"
    }

    // stages {
    //     stage('Checkout') {
    //         steps {
    //             git 'https://github.com/TomCat-11/Test_Cases_Practice.git'
    //         }
    //     }

        stage('Install Dependencies') {
            steps {
                bat "${env.PYTHON} -m pip install --upgrade pip"
                bat "${env.PYTHON} -m pip install pytest pytest-cov"
            }
        }

        stage('Run Tests') {
            steps {
                bat "${env.PYTHON} -m pytest --cov=calculator --cov-report=xml --junitxml=test-results/results.xml -v"
            }
        }

        stage('Publish Reports') {
            steps {
                junit 'test-results/results.xml'
                archiveArtifacts artifacts: 'coverage.xml', allowEmptyArchive: true
            }
        }
    }

    post {
        always {
            echo "Build finished. Check test results in Jenkins."
        }
    }
}
