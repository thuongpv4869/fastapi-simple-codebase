import typer

from app import services
from app.db.session import SessionLocal
from app.scripts.fake_data import fake_customers

cli = typer.Typer()
db = SessionLocal()


@cli.command()
def main():
    pass


@cli.command()
def create_admin_user(username: str, plain_pass: str):
    services.crud_user.create_admin_user(db, username, plain_pass)
    print(f"Admin user has been created: {username}/{plain_pass}")


@cli.command()
def gen_customers():
    fake_customers(db)


if __name__ == "__main__":
    cli()
    db.close()
