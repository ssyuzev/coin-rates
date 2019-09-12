"""
Please install fabric3 before run command from this module.

Install fabric3 from console:
>>> python3 -m pip install -U pip
>>> python3 -m pip install -U fabric3
"""

import multiprocessing

from fabric.api import task, local


dc = 'docker-compose'
settings = "--settings how_much_the_coin.settings"


@task
def start():
    """Run docker-compose."""
    local('docker-compose up -d')


@task
def stop():
    """Stop docker-compose."""
    local('docker-compose down')


@task
def status():
    """Show docker-compose status."""
    local('docker-compose ps')


@task
def makemigrations(app='', fake=False):
    """Make django migration."""
    local("{} exec web python3 manage.py makemigrations {} {}".format(
        dc, app, '--fake-initial' if fake else ''))


@task
def migrate(app='', fake=False):
    """Run django migration."""
    local("{} exec web python3 manage.py migrate".format(
        dc, app, '--fake-initial' if fake else ''))


@task
def runserver():
    """Run django development server."""
    local_addr = "0.0.0.0:8000"
    local("{} exec web python3 manage.py runserver {} {}".format(
        dc, local_addr, settings))


@task
def collectstatic():
    """Collect static for production."""
    local("docker-compose exec web python3 manage.py {}".format(
        'collectstatic --noinput'))


@task
def shell():
    """Run django shell in web container."""
    local('docker-compose exec web python3 manage.py shell {}'.format(
        settings))


@task
def bash():
    """Run bash in web container."""
    local('docker-compose exec web /bin/bash')


@task
def manage(command):
    """Run django manage command."""
    local("{} exec web python3 manage.py {} {}".format(
        dc, command, settings))


@task
def pytest(app_name='', multicore=False, isort=False):
    """Run pytest."""
    if multicore:
        cpu_cores = multiprocessing.cpu_count()
        cpu_cores = "-n " + str(cpu_cores)
    else:
        cpu_cores = ''
    use_isort = '--isort' if isort else ''
    pytest_cmd = (
        'docker-compose exec web bash -c "pytest {0} ' +
        '-x -s -v {1} {2} --flake8 --create-db --reuse-db ' +
        '--ds=how_much_the_coin.test_settings"'
    )
    local(pytest_cmd.format(app_name, cpu_cores, use_isort))
