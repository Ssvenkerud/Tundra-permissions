import pytest
import yaml


space = " " * 2


def load_yaml(yaml_file):
    with open(yaml_file, "r") as in_fh:
        file = yaml.safe_load(in_fh)
    return file


# roles


@pytest.fixture
def roles_object1():
    return [
        {"role1": {"member_of": ["role2"]}},
        {
            "role2": {
                "member_of": [
                    "ar_db_database1_r",
                    "ar_db_database1_w",
                    "ar_db_database2_r",
                    "ar_db_database2_w",
                ]
            }
        },
        {
            "ar_db_database1_r": {
                "privileges": {
                    "databases": {"read": ["database1"]},
                    "schemas": {"read": ["database1.*"]},
                    "tables": {"read": ["database1.*.*"]},
                }
            }
        },
        {
            "ar_db_database1_w": {
                "privileges": {
                    "databases": {"write": ["database1"]},
                    "schemas": {"write": ["database1.*"]},
                    "tables": {"write": ["database1.*.*"]},
                }
            }
        },
        {
            "ar_db_database2_r": {
                "privileges": {
                    "databases": {"read": ["database2"]},
                    "schemas": {"read": ["database2.*"]},
                    "tables": {"read": ["database2.*.*"]},
                }
            }
        },
        {
            "ar_db_database2_w": {
                "privileges": {
                    "databases": {"write": ["database2"]},
                    "schemas": {"write": ["database2.*"]},
                    "tables": {"write": ["database2.*.*"]},
                }
            }
        },
    ]


@pytest.fixture
def roles_object_str_results():
    return f"""roles:\n{space*1}- role1:\n{space*3}member_of:\n{space*4}- role2\n{space*1}- role2:\n{space*3}member_of:\n{space*4}- ar_db_database1_r\n{space*4}- ar_db_database1_w\n{space*4}- ar_db_database2_r\n{space*4}- ar_db_database2_w\n\n{space*1}- ar_db_database1_r:\n{space*3}privileges:\n{space*4}databases:\n{space*5}read:\n{space*6}- database1\n{space*4}schemas:\n{space*5}read:\n{space*6}- database1.*\n{space*4}tables:\n{space*5}read:\n{space*6}- database1.*.*\n{space*1}- ar_db_database1_w:\n{space*3}privileges:\n{space*4}databases:\n{space*5}write:\n{space*6}- database1\n{space*4}schemas:\n{space*5}write:\n{space*6}- database1.*\n{space*4}tables:\n{space*5}write:\n{space*6}- database1.*.*\n{space*1}- ar_db_database2_r:\n{space*3}privileges:\n{space*4}databases:\n{space*5}read:\n{space*6}- database2\n{space*4}schemas:\n{space*5}read:\n{space*6}- database2.*\n{space*4}tables:\n{space*5}read:\n{space*6}- database2.*.*\n{space*1}- ar_db_database2_w:\n{space*3}privileges:\n{space*4}databases:\n{space*5}write:\n{space*6}- database2\n{space*4}schemas:\n{space*5}write:\n{space*6}- database2.*\n{space*4}tables:\n{space*5}write:\n{space*6}- database2.*.*\n"""


# Functional roles


@pytest.fixture
def single_functional_role_object_str_results():
    return f"""{space*1}- role2:\n{space*3}warehouses:\n{space*4}- warehouse1\n{space*3}member_of:\n{space*4}- ar_db_database1_r\n{space*4}- ar_db_database1_w\n{space*4}- ar_db_database2_r\n{space*4}- ar_db_database2_w\n\n"""


@pytest.fixture
def functional_roles_object_str_results(single_functional_role_object_str_results):
    return (
        single_functional_role_object_str_results[:-1]
        + f"""{space*1}- role1:\n{space*3}member_of:\n{space*4}- role2\n\n"""
    )


# Access roles


@pytest.fixture
def single_accsess_role_object_str_results():
    return f"""{space*1}- ar_db_database1_r:\n{space*3}privileges:\n{space*4}databases:\n{space*5}read:\n{space*6}- database1\n{space*4}schemas:\n{space*5}read:\n{space*6}- database1.*\n{space*4}tables:\n{space*5}read:\n{space*6}- database1.*.*\n"""


@pytest.fixture
def accsess_roles_object_str_results(single_accsess_role_object_str_results):
    return (
        single_accsess_role_object_str_results
        + f"""{space*1}- ar_db_database1_w:\n{space*3}privileges:\n{space*4}databases:\n{space*5}write:\n{space*6}- database1\n{space*4}schemas:\n{space*5}write:\n{space*6}- database1.*\n{space*4}tables:\n{space*5}write:\n{space*6}- database1.*.*\n{space*1}- ar_db_database2_r:\n{space*3}privileges:\n{space*4}databases:\n{space*5}read:\n{space*6}- database2\n{space*4}schemas:\n{space*5}read:\n{space*6}- database2.*\n{space*4}tables:\n{space*5}read:\n{space*6}- database2.*.*\n{space*1}- ar_db_database2_w:\n{space*3}privileges:\n{space*4}databases:\n{space*5}write:\n{space*6}- database2\n{space*4}schemas:\n{space*5}write:\n{space*6}- database2.*\n{space*4}tables:\n{space*5}write:\n{space*6}- database2.*.*\n"""
    )


# Databases


@pytest.fixture
def databases_object1():
    return [
        {"database1": {"shared": "yes", "owner": "loader_qlik"}},
        {"database2": {"shared": "no", "owner": "loader_qlik"}},
    ]


@pytest.fixture
def databases_object2():
    return [
        {"database3": {"shared": "yes"}},
        {"database2": {"shared": "no", "owner": "loader_qlik"}},
    ]


@pytest.fixture
def single_database_object_str_results():
    return f"""databases:\n{space*1}- database1:\n{space*3}shared: yes\n{space*3}owner: loader_qlik\n"""


@pytest.fixture
def databases_object_str_results(single_database_object_str_results):
    return (
        single_database_object_str_results
        + f"""{space*1}- database2:\n{space*3}shared: no\n{space*3}owner: loader_qlik\n{space*1}- database3:\n{space*3}shared: yes\n"""
    )


# Users


@pytest.fixture
def user_object1():
    return [
        {"user1": {"can_login": "yes", "member_of": ["role1"]}},
        {"user2": {"can_login": "yes", "member_of": ["role2"]}},
    ]


@pytest.fixture
def user_object2():
    return [
        {"user3": {"can_login": "no", "member_of": ["role3"]}},
        {"user2": {"can_login": "yes", "member_of": ["role2"]}},
    ]


@pytest.fixture
def singel_user_object_str_result():
    return f"""users:\n{space*1}- user1:\n{space*3}can_login: yes\n{space*3}member_of:\n{space*4}- role1\n"""


@pytest.fixture
def users_object_str_results(singel_user_object_str_result):
    return (
        singel_user_object_str_result
        + f"""{space*1}- user2:\n{space*3}can_login: yes\n{space*3}member_of:\n{space*4}- role2\n{space*1}- user3:\n{space*3}can_login: no\n{space*3}member_of:\n{space*4}- role3\n"""
    )


# Warehouses


@pytest.fixture
def single_warehouse_object_str_results():
    return f"""warehouses:\n{space*1}- warehouse1:\n{space*3}size: xsmall\n"""


@pytest.fixture
def warehouses_object_str_results(single_warehouse_object_str_results):
    return f"""{single_warehouse_object_str_results}{space*1}- warehouse2:\n{space*3}size: xsmall\n{space*1}- warehouse3:\n{space*3}size: medium\n"""


@pytest.fixture
def warehouses_object1():
    return [{"warehouse1": {"size": "xsmall"}}, {"warehouse2": {"size": "xsmall"}}]


@pytest.fixture
def warehouses_object2():
    return [{"warehouse3": {"size": "medium"}}, {"warehouse2": {"size": "xsmall"}}]


# Base Module


@pytest.fixture
def object1():
    return [{"entitiy1": {"key": "value"}}, {"entitiy2": {"key": "value"}}]


@pytest.fixture
def object2():
    return [{"entitiy2": {"key": "value"}}, {"entitiy3": {"key": "value"}}]


# Spessification


@pytest.fixture
def yaml_spessification_a():
    file = load_yaml("tests/data/base_premissions/team_a_permisions.yml")
    for key in file:
        if key == "version":
            continue
        else:
            print(key)
            file[key] = sorted(file[key], key=lambda d: list(d.keys()))
    return file


@pytest.fixture
def yaml_spessification_b():
    return load_yaml("tests/data/base_premissions/team_b_permisions.yml")


# State
@pytest.fixture
def team_c_verefied_state_file():
    return {
        "version": "0.1.0",
        "serial": 1,
        "modules": {
            "databases": {
                "database1": {"shared": False},
                "database2": {"owner": "loader_qlik", "shared": False},
            },
            "warehouses": {
                "warehouse1": {"owner": "loader_qlik", "size": "xsmall"},
                "warehouse2": {"size": "xsmall"},
            },
            "users": {
                "user1": {"can_login": True, "member_of": ["role1"]},
                "user2": {"can_login": True, "member_of": ["role2"]},
                "user3": {"can_login": True, "member_of": ["role3"]},
            },
            "roles": {
                "role1": {"member_of": ["role2"], "warehouses": ["warehouse1"]},
                "role2": {
                    "member_of": [
                        "ar_db_database1_r",
                        "ar_db_database1_w",
                        "ar_db_database2_r",
                        "ar_db_database2_w",
                    ]
                },
                "role3": {"member_of": [], "warehouses": ["warehouse1"]},
                "loader_qlik": {"member_of": []},
                "ar_db_database1_r": {
                    "privileges": {
                        "databases": {"read": ["database1"]},
                        "schemas": {"read": ["database1.*"]},
                        "tables": {"read": ["database1.*.*"]},
                    }
                },
                "ar_db_database1_w": {
                    "privileges": {
                        "databases": {"write": ["database1"]},
                        "schemas": {"write": ["database1.*"]},
                        "tables": {"write": ["database1.*.*"]},
                    }
                },
                "ar_db_database2_r": {
                    "privileges": {
                        "databases": {"read": ["database2"]},
                        "schemas": {"read": ["database2.*"]},
                        "tables": {"read": ["database2.*.*"]},
                    }
                },
                "ar_db_database2_w": {
                    "privileges": {
                        "databases": {"write": ["database2"]},
                        "schemas": {"write": ["database2.*"]},
                        "tables": {"write": ["database2.*.*"]},
                    }
                },
            },
        },
        "generated": False,
    }


@pytest.fixture
def team_ac_state_update():
    return set(
        [
            ("roles", "role1"),
            ("roles", "role3"),
            ("roles", "loader_qlik"),
            ("warehouses", "warehouse1"),
            ("users", "user3"),
        ]
    )


@pytest.fixture
def team_ca_state_update():
    return set(
        [
            ("users", "user3"),
            ("warehouses", "warehouse1"),
            ("roles", "loader_qlik"),
            ("roles", "role3"),
            ("roles", "role1"),
        ]
    )


@pytest.fixture
def team_ca_plan():
    return """Changes to the following objects:
    roles: loader_qlik: {'member_of': []}
    roles: role1: {'warehouses': ['warehouse1'], 'member_of': ['role2']}
    roles: role3: {'warehouses': ['warehouse1'], 'member_of': []}
    users: user3: {'can_login': True, 'member_of': ['role3']}
    warehouses: warehouse1: {'size': 'xsmall', 'owner': 'loader_qlik'}
"""


@pytest.fixture
def team_ac_plan():
    return """Changes to the following objects:
    roles: role1: {'member_of': ['role2']}
    warehouses: warehouse1: {'size': 'xsmall'}
Entities to be removed:
    roles: loader_qlik
    roles: role3
    users: user3
"""
