#!/usr/bin/python3
import glob
import re
import os
import shutil

from lib.variables import *
from lib.utils import *

# =================================


def do_translate():

    try:
        shutil.rmtree(BUILD_FOLDER)
        os.makedirs(BUILD_FOLDER)
    except:
        pass

    languages = []
    for lang_file in lang_files:
        languages.append(getLangKey(lang_file))

    mPrint('languages to translate: ')
    mPrint(languages)
    # languages = ['en','de','es','fr','ja','kr','pt','zht']

    for folder_to_build in TRANSLATION_FOLDERS:
        translate_folder(BASE_PATH+'/src/' + folder_to_build)
    printline()
    mPrint('Done creating translated files at '+BUILD_FOLDER_NAME)
    printline()


def do_build():
    mkdir(COLLECTIONS_FOLDER_NAME)
    mPrint('building translated files into single jsonArray for mongoimport at ' +
           BUILD_FOLDER_NAME+"/"+COLLECTIONS_FOLDER_NAME)

    build_folder_folders = [f.name for f in os.scandir(
        BUILD_FOLDER) if f.is_dir() and not f.name == COLLECTIONS_FOLDER_NAME]

    for built_folder in build_folder_folders:
        mount_collection_array(built_folder)
    printline()
    mPrint('Done creating collections for mongo')
    printline()


def do_import():
    mPrint('calling mongoimport')
    printline()

    collections = glob.glob(COLLECTIONS_FOLDER+'/*.json')

    for collection_file in collections:
        collection_filename = JSON_FILES_RE.sub(r"\2", collection_file)
        update_mongo(collection_filename, collection_file)

    printline()
    mPrint('Done importing into mongodb')
    printline()
