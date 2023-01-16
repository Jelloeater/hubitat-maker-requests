import os

from dotenv import load_dotenv

from hubitatcontrol import *

load_dotenv()
host_env = os.getenv("HUBITAT_HOST")
token_env = os.getenv("HUBITAT_API_TOKEN")
app_id_env = os.getenv("HUBITAT_API_APP_ID")


def test_creds():
    import os
    assert os.getenv("HUBITAT_API_APP_ID") is not None
    assert os.getenv("HUBITAT_API_TOKEN") is not None


def test_hub_get():
    h = Hub(host=host_env, token=token_env, app_id=app_id_env)
    if h.devices is not None:
        assert True
    else:
        assert False


def test_device_bulb():
    h = get_hub(host=host_env, token=token_env, app_id=app_id_env)
    test_bulb = lookup_device(h, 'Porch')

    test_bulb.turn_on()
    assert test_bulb.switch == 'on'
    test_bulb.turn_off()
    assert test_bulb.switch == 'off'
    test_bulb.turn_on()
    assert test_bulb.switch == 'on'


# def test_device_outlet():
#     h = Hub(host=host_env, token=token_env, app_id=app_id_env)
#     t = lookup_device(h, 'Den Outlet')
#     assert t
