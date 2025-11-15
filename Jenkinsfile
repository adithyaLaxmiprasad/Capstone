pipeline {
  agent any

  environment {
    VENV_DIR = 'venv'
    PYTHON_EXE = 'C:\\Users\\adithya.l\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'
  }

  options {
    ansiColor('xterm')
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '25'))
  }

  stages {

    stage('Checkout Code') {
      steps {
        checkout scm
      }
    }

    stage('Prepare Python Environment') {
      steps {
        bat """
          "%PYTHON_EXE%" -m venv %VENV_DIR%
          %VENV_DIR%\\Scripts\\pip.exe install --upgrade pip
          %VENV_DIR%\\Scripts\\pip.exe install -r requirements.txt
        """
      }
    }

    stage('Run Selenium Tests Only') {
      steps {
        echo "Running Selenium Web Automation Tests..."

        // Clean old allure results
        bat '''
          powershell -Command "Remove-Item -Recurse -Force selenium_framework\\reports\\allure-results -ErrorAction SilentlyContinue"
          powershell -Command "New-Item -ItemType Directory -Force -Path selenium_framework\\reports\\allure-results"
        '''

        bat """
          %VENV_DIR%\\Scripts\\python.exe -m pytest selenium_framework\\tests -q
        """
      }
    }
  }

  post {
    always {
      cleanWs()
    }

    success {
      echo "Selenium CI Pipeline Completed Successfully!"
    }

    failure {
      echo "Selenium Tests Failed — Check Jenkins Console Output"
    }
  }
}
