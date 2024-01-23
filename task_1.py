import argparse
import shutil
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(description="Copy")
    parser.add_argument("-s", "--source", type=Path, help="Source folder")
    parser.add_argument(
        "-d",
        "--destination",
        type=Path,
        default=Path("dist"),
        help="Destination folder",
    )
    return parser.parse_args()


def copy_files(source: Path, destination: Path = Path("dist")) -> None:
    if not source:
        print("Please provide source directory name")
        return
    if source.is_dir():
        for child in source.iterdir():
            copy_files(child, destination)

    else:
        file_extention = source.suffix.lstrip(".")

        if file_extention:
            new_folder = Path(f"{destination}/{file_extention}")
            new_folder.mkdir(exist_ok=True, parents=True)
            try:
                shutil.copy(source, new_folder)
            except FileNotFoundError:
                print("Couldn't find file with a name {source}")
            except Exception:
                print("OOoops, some error while copying file")


def main():
    args = parse_args()
    print(args)
    copy_files(args.source, args.destination)


if __name__ == "__main__":
    main()
