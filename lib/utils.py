#!/usr/bin/python3
import json
import glob
import re
import os
import copy
import subprocess
from benedict import benedict
from tqdm import tqdm

from lib.variables import *
from lib.parsers import get_data_parser


def mPrint(*argv):
    if not PARSED_ARGS.verbose:
        return
    return print(*argv)


def printline():
    print('=================================')


def getLangKey(langFilePath):
    return LANG_FILE_RE.sub(r"\3", langFilePath)


def mkdir(folderName):
    if PARSED_ARGS.dryrun:
        return

    if not os.path.exists(BUILD_FOLDER + '/' + folderName):
        os.makedirs(BUILD_FOLDER + '/' + folderName)


def saveFile(filename, path, contents):
    if PARSED_ARGS.dryrun:
        return

    filepath = path + "/{0}.json".format(filename)
    with open(filepath, 'w') as f:
        json.dump(contents, f)


def get_translation(customLangData):
    def translate(translationKey):
        translation = ''

        if not translationKey:
            return 'MISSING_TRANSLATION_KEY'

        if not translation and customLangData:
            try:
                translation = customLangData[translationKey]
            except:
                pass

        if not translation:
            try:
                translation = text_en[translationKey]
            except:
                pass

        if not translation:
            return 'MISSING_TRANSLATION_VALUE('+translationKey+')'

        translation = COLOR_TAG_RE.sub("", translation)
        translation = LINEBREAK_RE.sub("\n", translation)

        return translation
    return translate


def get_folder_files(srcFolder):
    return sorted(glob.glob("{0}/*.json".format(srcFolder)))


def translate_folder(srcFolder):
    foldername = SRC_FOLDER_FILES_RE.sub(r"\2", srcFolder)
    fileParser = get_data_parser(foldername)
    printline()
    print("| Translating " + foldername)
    printline()
    if PARSED_ARGS.verbose:
        folder_files = tqdm(get_folder_files(srcFolder))
    else:
        folder_files = get_folder_files(srcFolder)

    for file in folder_files:
        filename = JSON_FILES_RE.sub(r"\2", file)
        file_data = json.load(open(file))
        file_keys = file_data.keys()
        if "_id" not in file_keys:
            file_data["_id"] = filename

        for lang in lang_files:
            currentLanguageData = json.load(open(lang))
            get_translation_specific = get_translation(currentLanguageData)
            lang_key = getLangKey(lang)
            lang_folder = foldername+'-'+lang_key
            if PARSED_ARGS.verbose:
                folder_files.set_description(
                    "Translating {0}::{1}::{2}".format(foldername, filename, lang_key))
            mkdir(lang_folder)
            jsonFileContents = fileParser(filename, benedict(
                copy.deepcopy(file_data)), get_translation_specific)
            saveFile(filename, BUILD_FOLDER+'/'+lang_folder, jsonFileContents)


def mount_assets(folder, imageName, imageExtension):
    if not folder or not imageName or not imageExtension:
        return None
    else:
        return "{0}{1}{2}.{3}".format(ASSETS_URL, folder, imageName, imageExtension)


def mount_collection_array(folderName):
    folder_files = get_folder_files(BUILD_FOLDER+"/"+folderName)
    collection = []

    for file in folder_files:
        data = json.load(open(file))
        collection.append(data)

    saveFile(folderName, COLLECTIONS_FOLDER, collection)
    mPrint('Collection {0} saved'.format(folderName))


def update_mongo(collection, filePath):
    printline()
    mPrint(
        "** Updating MONGODB => collection \"{0}\" with file {1} **\n".format(collection, filePath))

    if PARSED_ARGS.self or PARSED_ARGS.atlas:
        if PARSED_ARGS.self:
            subprocess.call(MONGOIMPORT_SELF_CMD.format(
                collection, filePath), shell=True)

        if PARSED_ARGS.atlas:
            subprocess.call(MONGOIMPORT_ATLAS_CMD.format(
                collection, filePath), shell=True)
    else:
        subprocess.call(MONGOIMPORT_SELF_CMD.format(
            collection, filePath), shell=True)
        subprocess.call(MONGOIMPORT_ATLAS_CMD.format(
            collection, filePath), shell=True)

    mPrint(
        "\n** MONGODB => collection \"{0}\" updated **\n\n".format(collection))
