from fabric.api import task, local


def print_msg(msg):
    """Print message in console.

    You need to install `termcolor` package to get colored messages.

    """
    def green_msg(msg):
        """Make message green color in console."""
        return '\033[92m{0}\033[00m'.format(msg)

    print(green_msg('\n{}\n'.format(msg)))


# MAIN COMMANDS
# ============================================================================

@task
def manage(command):
    """Run ``python3 manage.py`` command."""
    return local('python3 manage.py {}'.format(command))


@task
def run():
    """Run server."""
    print_msg('Running server')
    return manage('runserver')


@task
def shell():
    """Run shell."""
    return manage('shell_plus')


# GIT
# ============================================================================

@task
def push():
    """Push changes to all servers."""
    print_msg('1. Pushing to origin')
    local('git push origin master')

    print_msg('2. Pushing to Heroku')
    local('git push heroku master')


# LOCALES
# ============================================================================

@task
def makemessages():
    """Make messages."""
    return manage('makemessages -l ru --no-location')


@task
def compilemessages():
    """Compile messages."""
    return manage('compilemessages')


# MIGRATIONS AND DATABASE
# ============================================================================

@task
def makemigrations():
    """Make migrations for database."""
    manage('makemigrations')


@task
def migrate():
    """Apply migrations to database."""
    print_msg('Applying migrations')
    manage('migrate')


@task
def createsuperuser(email='root@root.ru'):
    """Create superuser with default credentials."""
    print_msg('Creating superuser')
    return manage('createsuperuser --username root --email {}'.format(email))


@task
def resetdb():
    """Reset database to initial state."""
    print_msg('Reset database')
    manage('reset_db')
    migrate()
    createsuperuser()


# STATIC CHECKS: ISORT AND PEP8
# ============================================================================

@task
def isort():
    """Fix imports formatting."""
    print_msg('Running imports fix')
    local('isort apps -y -rc')


@task
def pep8(path='apps'):
    """Check PEP8 errors."""
    print_msg('Checking PEP8 errors')
    return local('flake8 --config=.flake8 {}'.format(path))


# REQUIREMENTS
# ============================================================================

@task
def install_reqs():
    """Install requirements."""
    print_msg('Installing requirements')
    local('pip install -r requirements-local.txt')


@task
def install_base_reqs():
    """Install base requirements."""
    print_msg('Installing base requirements')
    local('pip install -r requirements.txt')


# HEROKU
# ============================================================================

@task
def hlogs():
    local('heroku logs --source app --tail')
