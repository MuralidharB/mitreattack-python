from mitreattack.stix20 import MitreAttackData


def main():
    mitre_attack_data = MitreAttackData("enterprise-attack.json")

    # get all groups related to techniques
    groups_using_techniques = mitre_attack_data.get_all_groups_using_all_techniques()

    print(f"Groups using techniques ({len(groups_using_techniques.keys())} techniques):")
    for id, groups in groups_using_techniques.items():
        attack_id = mitre_attack_data.get_attack_id(id)
        print(f"* {attack_id} - used by {len(groups)} {'group' if len(groups) == 1 else 'groups'}")


if __name__ == "__main__":
    main()
