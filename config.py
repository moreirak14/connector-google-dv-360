from pathlib import Path

from dynaconf import Dynaconf

PATH_ROOT = Path(__file__).parent

settings = Dynaconf(
    environments=True,
    envvar_prefix="CONNECTOR-GOOGLE-DV-360",
    settings_files=["settings.toml", ".secrets.toml"],
    includes=[f"{PATH_ROOT}/settings.toml", f"{PATH_ROOT}/.secrets.toml"],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.


def database_uri():
    _database_uri = (
        f"{settings.database_dialect_driver}://"
        f"{settings.database_user}:{settings.database_password}@"
        f"{settings.database_host}:{settings.database_port}/"
        f"{settings.database_name}"
    )

    return _database_uri


settings.database_uri = database_uri()
