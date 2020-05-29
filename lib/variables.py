#!/usr/bin/python3
import re
import os
import json
import glob
from lib.argparse import parsed_args

SCRIPT_VERSION = 2.1

PARSED_ARGS = parsed_args()

ASSETS_URL = "https://assets.epicsevendb.com/_source/"
COLOR_TAG_RE = re.compile(r"(<#[a-z0-9]{4,6})>|(</>)", re.IGNORECASE)
LANG_FILE_RE = re.compile(r"(.*\/)(text\_)(.*)(\.json)", re.IGNORECASE)
SRC_FOLDER_FILES_RE = re.compile(r"(.*\/src\/)(.*)", re.IGNORECASE)
JSON_FILES_RE = re.compile(r"(.*\/)(.*)(\.json)", re.IGNORECASE)
LINEBREAK_RE = re.compile(r"\\n", re.IGNORECASE)

BASE_PATH = os.getcwd()
BUILD_FOLDER_NAME = "dist_py"
BUILD_FOLDER = BASE_PATH+"/"+BUILD_FOLDER_NAME
TRANSLATION_FOLDERS = ['materials', 'buffs', 'ex_equip', 'hero', 'artifact']

text_en = json.load(open(BASE_PATH+'/src/text/text_en.json'))
lang_files = sorted(glob.glob(BASE_PATH + "/src/text/*.json"))

COLLECTIONS_FOLDER_NAME = '_collections'
COLLECTIONS_FOLDER = BUILD_FOLDER+"/"+COLLECTIONS_FOLDER_NAME

MONGOIMPORT_ATLAS_CMD = "mongoimport --host $E7DB_ATLAS_SHARDS --ssl --username $E7DB_ATLAS_USER --password \"$E7DB_ATLAS_PW\" --authenticationDatabase $E7DB_ATLAS_AUTH_DB --db $E7DB_ATLAS_DB --collection {0} --type json --file {1} --jsonArray --drop;"

MONGOIMPORT_SELF_CMD = "mongoimport --uri \"mongodb://$E7DB_ATLAS_USER:$E7DB_SELF_PW@E7DB_SELF_SHARDS/$E7DB_ATLAS_DB?authSource=$E7DB_ATLAS_AUTH_DB&gssapiServiceName=mongodb\" --collection {0} --type json --file {1} --jsonArray --drop;"
