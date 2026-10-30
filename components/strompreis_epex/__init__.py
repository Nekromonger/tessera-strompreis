"""Electricity price: the ESPHome side. The tiles, the card and the top bar's item are in strompreis_epex.cpp; the
item shows the price of a tile on the screen. smart_display.register_plugin() reads the id, version, tile memory and
the screen's texts from the manifest and translations/ beside this folder (docs/FIRMWARE_API.md)."""
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import smart_display
from esphome.const import CONF_ID

# The core component every Tessera screen has; the plugin API lives in it.
DEPENDENCIES = ["smart_display"]

strompreis_epex_ns = cg.esphome_ns.namespace("strompreis_epex")
ElectricityPrice = strompreis_epex_ns.class_("ElectricityPrice", cg.Component)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(ElectricityPrice),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await smart_display.register_plugin(var, __file__)
