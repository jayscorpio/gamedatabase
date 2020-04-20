#!/usr/bin/python3
from lib.variables import SCRIPT_VERSION, PARSED_ARGS
from lib.build import do_translate, do_build, do_import
from datetime import datetime

startTime = datetime.now()

if PARSED_ARGS.version:
    print("{0} (EpicSevenDB/gamedatabase v2.x)".format(SCRIPT_VERSION))
    exit(0)

# =================================

if PARSED_ARGS.dryrun or not PARSED_ARGS.importonly:
    do_translate()

if not PARSED_ARGS.dryrun and not PARSED_ARGS.buildonly:
    do_build()
    do_import()

print('Translate script ran successfully!')
print('Time to complete: ', datetime.now() - startTime)
exit(0)
