from mitreattack.stix20 import MitreAttackData


def main():
    mitre_attack_data = MitreAttackData("enterprise-attack.json")

    tactics = mitre_attack_data.get_tactics(remove_revoked_deprecated=True)

    for t in tactics:
        print(t['name'], t['description'])
    print(f"Retrieved {len(tactics)} ATT&CK tactics.")


if __name__ == "__main__":
    main()
