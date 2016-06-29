from fabric.api import local, execute

def build():
    '''
    Builds image
    '''
    local('docker build -t banjocat/blog:latest .')


def run():
    '''
    Run image
    '''
    local('docker run --name blog -p 8000:8000 -d banjocat/blog:latest')


def rebuild():
    '''
    Rebuild image
    '''
    local('docker stop blog')
    local('docker rm blog')
    execute(build)


def log():
    '''
    Check logs
    '''
    local('docker logs blog')

def remove():
    '''
    Remove image
    '''
    local('docker rm blog')


def stop():
    '''
    Stop image
    '''
    local('docker stop blog')


