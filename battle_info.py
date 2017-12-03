from battle import commander
unit_client = commander.Client()
my_info = unit_client.ask_my_info()


def search_target(data=None, **kwargs):
    towers = unit_client.ask_towers()
    print("List of towers:{}".format(towers))
    if towers:
        tower_id = towers[0]["id"]
        unit_client.do_attack(tower_id)
        print("Unit {}".format(my_info['id']))
        print("attak ID:{}".format(tower_id))
        unit_client.when_item_destroyed(tower_id, search_target)
    else:
        attack_center()


def attack_center(data=None, **kwargs):
    center = unit_client.ask_center()
    print("Center ID:{}".format(center['id']))
    print("Unit {}".format(my_info['id']))
    print("attak ID:{}".format(center['id']))
    unit_client.do_attack(center['id'])


search_target()