import click
import string
import secrets

@click.group()
def cli():
    pass

@click.command()
@click.option('--length', type=int, default=8, help='number of characters in your password')
def simple(length):
    """ Generate an eight-character alphanumeric password """
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    click.echo(f"{password}")


@click.command()
@click.option('--length', type=int, default=12, help='number of characters in your password')
def complex(length):
    """ Generate a ten-character alphanumeric password with at least one lowercase character, 
    at least one uppercase character, and at least three digits 
    """
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(length))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3):
            break
        
    click.echo(f"{password}")


@click.command()
def token():
    """ Generate a hard-to-guess security token suitable for password recovery applications """
    click.echo(f"{secrets.token_urlsafe()}")

cli.add_command(simple)
cli.add_command(complex)
cli.add_command(token)

if __name__ == '__main__':
    cli()