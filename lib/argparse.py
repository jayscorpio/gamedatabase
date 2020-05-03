#!/usr/bin/python3
import argparse  # tutorial https://stackabuse.com/command-line-arguments-in-python/

parser = argparse.ArgumentParser(
    description='Script to parse SRC files into translated collections to be imported to database.')
parser.add_argument("-V", "--version",
                    help="show script version", action="store_true")
parser.add_argument("-B", "--buildonly",
                    help="build only, without attempting to create collections or call mongoimport", action="store_true")
parser.add_argument("-I", "--importonly",
                    help="import only, build dist_py/_collections with current dist_py files and call mongoimport", action="store_true")
parser.add_argument(
    "-D", "--dryrun", help="dry run, will run build without actually saving the files to dist_py, good for testing if code is not breaking", action="store_true")
parser.add_argument(
    "-v", "--verbose", help="verbose, will print all actions done", action="store_true")
parser.add_argument(
    "-S", "--self", help="import to localhost as URI instead of atlas shard cluster", action="store_true")

args = parser.parse_args()


def parsed_args():
    return args
