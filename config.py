from pathlib import Path
from dynaconf import Dynaconf

PATH_ROOT = Path(__file__).parent

settings = Dynaconf(
    environments=True,
    envvar_prefix="CONNECTOR-GOOGLE-DV-360",
    settings_files=['settings.toml', '.secrets.toml'],
    includes=[f"{PATH_ROOT}/settings.toml", f"{PATH_ROOT}/.secret.toml"],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
