node {

    try {
        stage('Checkout') {
            echo "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/BSP_NightlyBuild/Checkout.py"
        }
        stage('Build') {
            echo "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/BSP_NightlyBuild/Build.py"
        }
        stage('Test') {
            sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/BSP_NightlyBuild/Test.py"
        }
        stage('Deploy') {
            sh "python ${env.WORKSPACE}/../${env.JOB_NAME}@script/BSP_NightlyBuild/Deploy.py"
        }
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}
