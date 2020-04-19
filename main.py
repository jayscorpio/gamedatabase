#!/usr/bin/python3
import argparse # tutorial https://stackabuse.com/command-line-arguments-in-python/
from lib.variables import SCRIPT_VERSION
from lib.build import do_translate, do_build, do_import
from datetime import datetime

startTime = datetime.now()

parser = argparse.ArgumentParser(description = 'Script to parse SRC files into translated collections to be imported to database.')
parser.add_argument("-V", "--version", help="show script version", action="store_true")
parser.add_argument("-B", "--build", help="build only, without attempting to create collections or call mongoimport", action="store_true")
parser.add_argument("-M", "--mongo", help="import only, build dist_py/_collections with current dist_py files and call mongoimport", action="store_true")
parser.add_argument("-D", "--dryrun", help="dry run, will run build without actually saving the files to dist_py, good for testing if code is not breaking", action="store_true")

args = parser.parse_args()

if args.version:
    print("{0} (EpicSevenDB/gamedatabase v2.x)".format(SCRIPT_VERSION))
    exit(0)


# =================================

if not args.dryrun:
    if not args.mongo:
        do_translate()

    if not args.build:
        do_build()
        do_import()
else:
    do_translate(args.dryrun)

print('Translate script ran successfully!')
print('Time to complete: ', datetime.now() - startTime)
exit(0)
