import click

from src.tundra.Spesification import Spesification
from src.tundra.Permission_state import Permission_state
from src.tundra.loader_local_file import Local_file_loader


verification_option = click.option(
    "--verification",
    default=false,
    help="""Run permissioin file
              verification""",
)
generate_role_option = click.option(
    "--generate_roles",
    default=false,
    help="""generate AR roles that
              are not in permissions file""",
)
permission_path_option = click.option(
    "--permission_path",
    default=".",
    help="""path to permsisions
              file or directory containing permisisons file""",
)
state_path_option = click.option(
    "--state_path",
    default=".",
    help="""Path to the current
              statefile""",
)
change_path_option = click.option(
    "-change_path",
    default="",
    help="""Path for printing change
             output file""",
)
export_path_option = click.option(
    "--export_path",
    default="./permifrost_permisions.yml",
    help="""Location for the processed permiforst file""",
)


def processing(verification, generate_roles, permission_path):
    permisions = Spesification(verification, generate_roles)
    permisions.load(permission_path)
    permisions.identify_modules()
    permisions.identify_entities()
    permisions.generate()

    return permisions


@click.group()
def cli():
    pass


@click.command("plan")
@verification_option
@generate_role_option
@permission_path_option
@state_path_option
@change_path_option
def plan(permission_path, state_path, change_path):
    permisions = processing(verification, generate_roles, permission_path)
    previouse_state = Permission_state().load(Local_file_loader(), state_path)
    planned_state = Permission_state(permisions).generate()
    planned_state.compare(previouse_state)
    planned_state.plan(change_path)


@click.command('apply')
@verification_option
@generate_role_option
@permission_path_option
@export_path_option
def apply(
    verification, generate_roles, permission_path, state_path, change_path, export_path
):
    permisions = processing(verification, generate_roles, permission_path)
    permisions.export(export_path)


@click.command('verify')
@verification_option
@generate_role_option
@permission_path_option
def verify(verification, generate_roles, permission_path):
    permisions = processing(verification, generate_roles, permission_path)
