from os import system
from typing import Iterable
import click

from pathlib import Path


@click.command()
@click.option(
    "-d",
    "--grpc-device-dir",
    default="../grpc-device",
    help="Root grpc-device directory to export to",
)
@click.argument("drivers", nargs=-1)
def generate_stubs(grpc_device_dir: str, drivers: Iterable[str]):
    grpc_device_dir = Path("../grpc-device")
    proto_source_dir = grpc_device_dir / "source/protobuf"
    includes = [proto_source_dir] + [
        grpc_device_dir / "generated" / driver_name for driver_name in drivers
    ]
    include_str = str.join(" ", [f"-I{include_dir}" for include_dir in includes])
    proto_files_str = str.join(
        " ",
        [
            f"{driver_name}.proto"
            for driver_name in list(drivers) + ["session", "nidevice"]
        ],
    )

    system(
        rf"poetry run python -m grpc_tools.protoc {include_str} --python_out=. --grpc_python_out=. --mypy_out=. --mypy_grpc_out=. {proto_files_str}"
    )


if __name__ == "__main__":
    generate_stubs()
