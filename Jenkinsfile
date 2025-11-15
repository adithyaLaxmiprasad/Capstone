pipeline {
  agent any

  environment {
    GITHUB_TOKEN_CREDENTIAL = 'github-token'
    VENV_DIR = 'venv'
    PYTHON_EXE = 'C:\\Users\\adithya.l\\AppData\\Local\\Programs\\Python\\Python314\\python.exe'
  }

  options {
    ansiColor('xterm')
    timestamps()
    buildDiscarder(logRotator(numToKeepStr: '25'))
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Prepare Python') {
      steps {
        script {
          if (isUnix()) {
            sh '''
              python -m venv ${VENV_DIR}
              . ${VENV_DIR}/bin/activate
              python -m pip install --upgrade pip
              pip install -r requirements.txt
            '''
          } else {
            bat """
              "%PYTHON_EXE%" -m venv %VENV_DIR%
              %VENV_DIR%\\Scripts\\pip.exe install --upgrade pip
              %VENV_DIR%\\Scripts\\pip.exe install -r requirements.txt
            """
          }
        }
      }
    }

    stage('Run Unit / Backend Tests (banking_app)') {
      steps {
        script {
          if (isUnix()) {
            sh '''
              . ${VENV_DIR}/bin/activate
              pytest banking_app/tests -q || true
            '''
          } else {
            bat """
              %VENV_DIR%\\Scripts\\python.exe -m pytest banking_app\\tests -q || exit /b 0
            """
          }
        }
      }
    }

    stage('Run Selenium + Appium Tests (Functional)') {
      steps {
        script {
          if (isUnix()) {
            sh '''
              rm -rf selenium_framework/reports/allure-results || true
              mkdir -p selenium_framework/reports/allure-results || true
              . ${VENV_DIR}/bin/activate
              pytest selenium_framework/tests -n 2 --alluredir=selenium_framework/reports/allure-results -q
              pytest mobile_tests -q || true
            '''
          } else {
            bat """
              powershell -Command "Remove-Item -Recurse -Force selenium_framework\\reports\\allure-results -ErrorAction SilentlyContinue"
              powershell -Command "New-Item -ItemType Directory -Force -Path selenium_framework\\reports\\allure-results"
              %VENV_DIR%\\Scripts\\python.exe -m pytest selenium_framework\\tests --alluredir=selenium_framework\\reports\\allure-results -q
              %VENV_DIR%\\Scripts\\python.exe -m pytest mobile_tests -q || exit /b 0
            """
          }
        }
      }
    }

    stage('Generate Allure Report') {
      steps {
        script {
          if (isUnix()) {
            sh '''
              allure generate selenium_framework/reports/allure-results -o selenium_framework/reports/allure-report --clean || true
            '''
          } else {
            bat """
              powershell -Command "if(!(Test-Path selenium_framework\\reports\\allure-results)){Write-Host 'no allure results'}"
              allure generate selenium_framework\\reports\\allure-results -o selenium_framework\\reports\\allure-report --clean || echo "allure generate failed"
            """
          }
        }
      }
      post {
        always {
          archiveArtifacts artifacts: 'selenium_framework/reports/allure-report/**', fingerprint: true
          junit allowEmptyResults: true, testResults: '**/test-results.xml'
        }
      }
    }
  }

  post {
    always {
      cleanWs()
    }
    success {
      echo "Pipeline succeeded"
    }
    failure {
      echo "Pipeline failed - check console output and attached artifacts"
    }
  }
}