from hubitatcontrol.generic import Switch


class Bulb(Switch):
    @property
    def level(self) -> int:
        return [x for x in self.attributes if "level" in x["name"]][0]['currentValue']


class Advanced_Zigbee_RGBW_Bulb(Bulb):
    @property
    def color_mode(self) -> str:
        return [x for x in self.attributes if "colorMode" in x["name"]][0]['currentValue']

    @property
    def color_name(self) -> str:
        return [x for x in self.attributes if "colorName" in x["name"]][0]['currentValue']

    @property
    def color(self) -> str:
        return [x for x in self.attributes if "color" in x["name"]][0]['currentValue']

    @property
    def color_temp(self) -> int:
        return [x for x in self.attributes if "colorTemperature" in x["name"]][0]['currentValue']

    @property
    def hue(self) -> int:
        return [x for x in self.attributes if "hue" in x["name"]][0]['currentValue']
