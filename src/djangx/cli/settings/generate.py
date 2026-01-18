from pathlib import Path

from ... import Conf, ConfField


class FileGeneratorPathsConf(Conf):
    """Generated files configuration settings."""

    _base_dir = Path.cwd()

    dotenv_example = ConfField(default=_base_dir / ".env.example", type=Path)
    vercel_json = ConfField(default=_base_dir / "vercel.json", type=Path)
    api_main_py = ConfField(default=_base_dir / "api" / "main.py", type=Path)


FILE_GENERATOR_PATHS = FileGeneratorPathsConf()


__all__ = ["FILE_GENERATOR_PATHS"]
