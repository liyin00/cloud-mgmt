pipeline {
    agent { dockerfile true }
    environment {
        PROJECT_ID = 'composed-future-332501'
        CLUSTER_NAME = 'clae-gcp'
        LOCATION = 'asia-southeast1'
        CREDENTIALS_ID = 'gke_composed-future-332501_asia-southeast1_clae-gke'
    }
    stages {
        stage("Checkout code") {
            steps {
                checkout scm
            }
        }
        stage("Build image") {
            steps {
                echo "workspace directory is ${workspace}"
                dir ("$workspace/app"){
                    sh 'docker build -t stock_service -f $WORKSPACE/app/stock_service/Dockerfile .'
                    sh 'docker build -t users_service -f $WORKSPACE/app/users_service/Dockerfile .'
                }

            }
        }
        stage("Push image") {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'lingliyin') {
                            myapp.push("latest")
                            myapp.push("${env.BUILD_ID}")
                    }
                }
            }
        }        
        stage('Deploy to GKE') {
            steps{
                sh "sed -i 's/clae:latest/clae:${env.BUILD_ID}/g' deployment.yaml"
                step([$class: 'KubernetesEngineBuilder', projectId: env.PROJECT_ID, clusterName: env.CLUSTER_NAME, location: env.LOCATION, manifestPattern: 'deployment.yaml', credentialsId: env.CREDENTIALS_ID, verifyDeployments: true])
            }
        }
    }    
}