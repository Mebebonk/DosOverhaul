import subprocess
import sys
import os

# TODO: add move directories

args = sys.argv

if len(args) != 2:
    print("Wrong number of arguments")
    print("Please provide path to Divinity Original Sin 2")

    exit(1)

source_dirs = ["Projects", "Editor/Mods", "Public", "Mods"]
base_junctions_dir = args[1]

for source_dir in source_dirs:
    subprocess.run(["cmd", "/c", "mklink", "/J",
                    os.path.abspath(f"../{source_dir}/DosOverhaul_39ad2bae-26c8-4050-836c-5398657031c7"),
                    f"{base_junctions_dir}/DefEd/Data/{source_dir}/DosOverhaul_39ad2bae-26c8-4050-836c-5398657031c7"],
                   shell=True)
