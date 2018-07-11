node {
    // Clean workspace before doing anything
    deleteDir()

    try {
        stage('Checkout') {
            echo "Checkout"
            sh "git clone ssh://jenkins@192.168.90.181:29418/9201_1"
            sh "git fetch ssh://jenkins@192.168.90.181:29418/9201_1 refs/changes/18/18/1"
            sh "git checkout ${changeBranch}"
        }
        stage('Build') {
            echo "build"
        }
        stage('Test') {
            echo "Test"
        }
        stage('Deploy') {
            echo "Deploy"
        }
    } catch (err) {
        currentBuild.result = 'FAILED'
        throw err
    }
}
