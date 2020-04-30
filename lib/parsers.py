#!/usr/bin/python3
import lib.utils


def get_data_parser(foldername):
    parser = {
        'artifact': artifact_parser,
        'materials': materials_parser,
        'hero': hero_parser,
        'ex_equip': ex_equip_parser,
        'buffs': buffs_parser
    }

    return parser.get(foldername, lambda: "Invalid parser")


def artifact_parser(filename, data, get_translation_specific):
    data["name"] = get_translation_specific(data["name"])
    data["description"] = get_translation_specific(data["description"])
    data["skill.description"] = get_translation_specific(
        data["skill.description"])
    if data["assets.icon"]:
        data["assets.icon"] = lib.utils.mount_assets(
            "item_arti/", data["assets.icon"], "png")
    if data["assets.image"]:
        data["assets.image"] = lib.utils.mount_assets(
            "item_arti/", data["assets.image"], "png")
    if data["assets.thumbnail"]:
        data["assets.thumbnail"] = lib.utils.mount_assets(
            "item_arti/", data["assets.thumbnail"], "jpg")
    return data


def materials_parser(filename, data, get_translation_specific):
    data["name"] = get_translation_specific(data["name"])
    data["description"] = get_translation_specific(data["description"])
    try:
        data["category"] = get_translation_specific(data["category"])
    except:
        pass
    if data["assets.icon"]:
        data["assets.icon"] = lib.utils.mount_assets(
            "item/", data["assets.icon"], "png")
    return data


def hero_parser(filename, data, get_translation_specific):
    data["name"] = get_translation_specific(data["name"])
    data["description"] = get_translation_specific(data["description"])
    data["story"] = get_translation_specific(data["story"])
    data["get_line"] = get_translation_specific(data["get_line"])

    data["assets"] = {}
    data["assets.icon"] = lib.utils.mount_assets(
        "face/", data["id"]+"_s", "png")
    data["assets.image"] = lib.utils.mount_assets(
        "face/", data["id"]+"_su", "png")
    data["assets.thumbnail"] = lib.utils.mount_assets(
        "face/", data["id"]+"_l", "png")

    if data["specialty"]:
        data["specialty.assets"] = {}
        data["specialty.assets.icon"] = lib.utils.mount_assets(
            "skill/", data["specialty.icon"], "png")
        del data["specialty.icon"]

        if data["specialty.name"]:
            data["specialty.name"] = get_translation_specific(
                data["specialty.name"])
        if data["specialty.description"]:
            data["specialty.description"] = get_translation_specific(
                data["specialty.description"])
        if data["specialty.type"]:
            if data["specialty.type.name"]:
                data["specialty.type.name"] = get_translation_specific(
                    data["specialty.type.name"])
            if data["specialty.type.description"]:
                data["specialty.type.description"] = get_translation_specific(
                    data["specialty.type.description"])

    if data["camping"]:
        try:
            for i1 in range(len(data["camping.personalities"])):
                data["camping.personalities"][i1] = get_translation_specific(
                    data["camping.personalities"][i1])
        except:
            pass

        try:
            for i2 in range(len(data["camping.topics"])):
                data["camping.topics"][i2] = get_translation_specific(
                    data["camping.topics"][i2])
        except:
            pass

        try:
            camp_val_keys = data["camping.values"].keys()
            camp_val_new = {}
            for camp_values in camp_val_keys:
                camp_val_new[get_translation_specific(
                    camp_values)] = data["camping.values."+camp_values]
            data["camping.values"] = camp_val_new
        except:
            pass

    # zodiac_tree
    for zodiac_in in range(len(data["zodiac_tree"])):
        data["zodiac_tree"][zodiac_in]["_id"] = "zodiac_{0}".format(zodiac_in)
        data["zodiac_tree"][zodiac_in]["name"] = get_translation_specific(
            data["zodiac_tree"][zodiac_in]["name"])
        data["zodiac_tree"][zodiac_in]["description"] = get_translation_specific(
            data["zodiac_tree"][zodiac_in]["description"])

        for zodiac_cost_index in range(len(data["zodiac_tree"][zodiac_in]["costs"])):
            data["zodiac_tree"][zodiac_in]["costs"][zodiac_cost_index]["_id"] = "zodiac_{0}_cost_{1}".format(
                zodiac_in, zodiac_cost_index)

    # skills
    data["buffs"] = []
    data["debuffs"] = []
    data["common"] = []

    for sk_in in range(len(data["skills"])):
        data["skills"][sk_in]["_id"] = "skill_{0}".format(sk_in)
        data["skills"][sk_in]["name"] = get_translation_specific(
            data["skills"][sk_in]["name"])
        data["skills"][sk_in]["description"] = get_translation_specific(
            data["skills"][sk_in]["description"])

        data["skills"][sk_in]["assets"] = {}
        data["skills"][sk_in]["assets"]["icon"] = lib.utils.mount_assets(
            "skill/", data["skills"][sk_in]["icon"], "png")
        del data["skills"][sk_in]["icon"]

        try:
            for sk_bf_in in range(len(data["skills"][sk_in]["buff"])):
                data["buffs"].append(data["skills"][sk_in]["buff"][sk_bf_in])
        except:
            pass

        try:
            for sk_dbf_in in range(len(data["skills"][sk_in]["debuff"])):
                data["debuffs"].append(
                    data["skills"][sk_in]["debuff"][sk_dbf_in])
        except:
            pass

        try:
            for sk_cm_in in range(len(data["skills"][sk_in]["common"])):
                data["common"].append(
                    data["skills"][sk_in]["common"][sk_cm_in])
        except:
            pass

        try:
            data["skills"][sk_in]["enhanced_description"] = get_translation_specific(
                data["skills"][sk_in]["enhanced_description"])
        except:
            pass

        try:
            data["skills"][sk_in]["soul_description"] = get_translation_specific(
                data["skills"][sk_in]["soul_description"])
        except:
            pass

        try:
            for sk_enh_index in range(len(data["skills"][sk_in]["enhancements"])):
                data["skills"][sk_in]["enhancements"][sk_enh_index]["_id"] = "skill_{0}_enh_{1}".format(
                    sk_in, sk_enh_index)
                data["skills"][sk_in]["enhancements"][sk_enh_index]["string"] = get_translation_specific(
                    data["skills"][sk_in]["enhancements"][sk_enh_index]["string"])

                for sk_enh_cost_index in range(len(data["skills"][sk_in]["enhancements"][sk_enh_index]["costs"])):
                    data["skills"][sk_in]["enhancements"][sk_enh_index]["costs"][sk_enh_cost_index]["_id"] = "skill_{0}_enh_{1}_cost_{2}".format(
                        sk_in, sk_enh_index, sk_enh_cost_index)
        except:
            pass

    # try:
    if data["specialty_change"]:
        if data["specialty_change.quests"] and len(data["specialty_change.quests"]) > 0:
            for sc_in in range(len(data["specialty_change.quests"])):
                data["specialty_change.quests"][sc_in]["category"] = get_translation_specific(
                    data["specialty_change.quests"][sc_in]["category"])
                data["specialty_change.quests"][sc_in]["mission_name"] = get_translation_specific(
                    data["specialty_change.quests"][sc_in]["mission_name"])
                data["specialty_change.quests"][sc_in]["mission_description"] = get_translation_specific(
                    data["specialty_change.quests"][sc_in]["mission_description"])

        if data["specialty_change.tree"] and len(data["specialty_change.tree"]) > 0:
            for sc_tree_in in range(len(data["specialty_change.tree"])):
                for sc_tree_row_in in range(len(data["specialty_change.tree"][sc_tree_in])):
                    for sc_tree_row_enhancements_in in range(len(data["specialty_change.tree"][sc_tree_in][sc_tree_row_in]['enhancements'])):
                        currentEnhancement = data["specialty_change.tree"][sc_tree_in][
                            sc_tree_row_in]['enhancements'][sc_tree_row_enhancements_in]
                        currentEnhancement['description'] = get_translation_specific(
                            currentEnhancement['description'])
                        if currentEnhancement['upgrade']:
                            currentEnhancement['upgrade'] = get_translation_specific(
                                currentEnhancement['upgrade'])
    # except:
    #     pass

    if data["relationships"] and len(data["relationships"]) > 0:
        for relation_in in range(len(data["relationships"])):
            if data["relationships"][relation_in]["name"]:
                data["relationships"][relation_in]["name"] = get_translation_specific(
                    data["relationships"][relation_in]["name"])
            if data["relationships"][relation_in]["description"]:
                data["relationships"][relation_in]["description"] = get_translation_specific(
                    data["relationships"][relation_in]["description"])
            if data["relationships"][relation_in]["relations"] and len(data["relationships"][relation_in]["relations"]) > 0:
                for relationship_relation_in in range(len(data["relationships"][relation_in]["relations"])):
                    try:
                        data["relationships"][relation_in]["relations"][relationship_relation_in]['description'] = get_translation_specific(
                            data["relationships"][relation_in]["relations"][relationship_relation_in]['description'])
                        data["relationships"][relation_in]["relations"][relationship_relation_in]['relation_id'] = data[
                            "relationships"][relation_in]["relations"][relationship_relation_in]['relation']
                        data["relationships"][relation_in]["relations"][relationship_relation_in]['relation'] = get_translation_specific(
                            data["relationships"][relation_in]["relations"][relationship_relation_in]['relation'])
                    except:
                        pass

                    try:
                        data["relationships"][relation_in]["relations"][relationship_relation_in]['upgrade']['description'] = get_translation_specific(
                            data["relationships"][relation_in]["relations"][relationship_relation_in]['upgrade']['description'])
                        data["relationships"][relation_in]["relations"][relationship_relation_in]['upgrade']['relation_id'] = data[
                            "relationships"][relation_in]["relations"][relationship_relation_in]['upgrade']['relation']
                        data["relationships"][relation_in]["relations"][relationship_relation_in]['upgrade']['relation'] = get_translation_specific(
                            data["relationships"][relation_in]["relations"][relationship_relation_in]['upgrade']['relation'])
                    except:
                        pass

    return data


def buffs_parser(filename, data, get_translation_specific):
    data["name"] = get_translation_specific(data["name"])
    data["effect"] = get_translation_specific(data["effect"])

    data["assets"] = {}
    data["assets.icon"] = lib.utils.mount_assets("buff/", data["icon"], "png")
    del data["icon"]

    return data


def ex_equip_parser(filename, data, get_translation_specific):
    data["name"] = get_translation_specific(data["name"])
    data["description"] = get_translation_specific(data["description"])

    data["assets"] = {}
    data["assets.icon"] = lib.utils.mount_assets("img/", data["icon"], "png")
    del data["icon"]

    for sk_exeq_index in range(len(data["skills"])):
        data["skills"][sk_exeq_index]["_id"] = sk_exeq_index

        try:
            data["skills"][sk_exeq_index]["description"] = get_translation_specific(
                data["skills"][sk_exeq_index]["description"])
        except:
            pass

        try:
            if data["skills"][sk_exeq_index]["skill_description"]:
                data["skills"][sk_exeq_index]["skill_description"] = get_translation_specific(
                    data["skills"][sk_exeq_index]["skill_description"])
        except:
            pass

    return data
