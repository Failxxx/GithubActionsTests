# <pep8 compliant>
import os
import sys
import zipfile
from pathlib import Path

from scripts.utils import (
    zipdir,
    parser,
    bcolors,
    remove_folders_matching_pattern,
    download_stop_motion_obj_addon,
    get_centered_message
)

print(f"{bcolors.OKBLUE}{get_centered_message(' RUN TESTS START ', '=')}{bcolors.ENDC}")

try:
    import blender_addon_tester as BAT
except Exception as e:
    print(e)
    sys.exit(1)


def main():
    """Execute the tests suite."""

    arguments = parser.parse_args()

    # Get blender version(s) to test the addon
    if arguments.b is None:
        print("ERROR: -b option is None.")
        parser.parse_args(['-h'])

    blender_rev = arguments.b

    module = "addon"
    here = Path(__file__).parent
    addon = os.path.join(os.path.abspath("."), module)

    try:
        # Cleanup '__pychache__' folders in the 'addon' folder
        remove_folders_matching_pattern(os.path.join(os.path.abspath("."), module))

        # Download addons on which this addon depends
        smo_addon_dest = os.path.abspath(here.joinpath("../cache").as_posix())
        smo_path, smo_module_name = download_stop_motion_obj_addon(smo_addon_dest)
        os.environ["STOP_MOTION_OBJ_PATH"] = smo_path
        os.environ["STOP_MOTION_OBJ_MODULE"] = smo_module_name

        # Zip addon
        print("Zipping addon - path: " + os.path.abspath(addon))
        zipf = zipfile.ZipFile(module + ".zip", 'w', zipfile.ZIP_DEFLATED)
        zipdir("./" + module, zipf)
        zipf.close()
        addon = os.path.join(os.path.abspath("."), module + ".zip")

    except Exception as e:
        print(e)
        exit_val = 1

    # Custom configuration
    config = {
        "blender_load_tests_script": os.path.abspath(here.joinpath("load_pytest.py").as_posix()),
        "blender_cache": os.path.abspath(here.joinpath("../cache").as_posix()),
        "tests": os.path.abspath(here.joinpath("../tests").as_posix()),
        "coverage": False,
    }

    try:
        # Setup custom blender cache (where the blender versions will be downloaded and extracted)
        # The blender_addon_tester module raises an error when passed as a key in the config dict
        if config.get("blender_cache", None):
            os.environ["BLENDER_CACHE"] = config["blender_cache"]
            config.pop("blender_cache")

        exit_val = BAT.test_blender_addon(addon_path=addon, blender_revision=blender_rev, config=config)
    except Exception as e:
        print(e)
        exit_val = 1

    print(f"{bcolors.OKBLUE}{get_centered_message(' RUN TESTS END ', '=')}{bcolors.ENDC}")
    sys.exit(exit_val)


main()
