from battle import commander
from battle import ROLE
unit_client = commander.Client()

def search_target(data=None, **kwargs):
    towers = unit_client.ask_towers()
    for tower in towers:
        near_tower = unit_client.ask_nearest_enemy([ROLE.TOWER])
        if near_tower:
            tower_id = near_tower["id"]
            unit_client.do_attack(tower_id)
            unit_client.when_item_destroyed(tower_id, search_target)
        else:
            attack_center()

def attack_center(data=None, **kwargs):
    center = unit_client.ask_center()
    unit_client.do_attack(center['id'])
search_target()