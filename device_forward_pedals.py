# name=Simple: Pedals to Active Generator
"""
A simple script that forwards pedal events to the active generator plugin.

If the active plugin is an FL Studio built-in plugin, events will be ignored,
allowing FL Studio to handle the event itself.

Author: Maddy Guthridge
"""
import plugins
from common import get_active_generator_index, is_plugin_vst, is_control_mapped
try:
    from fl_classes import FlMidiMsg
except ImportError:
    pass


def OnControlChange(msg: 'FlMidiMsg') -> None:
    # If the control has been manually mapped, ignore it
    if is_control_mapped(msg):
        return
    if msg.data1 == 0x40:
        generator_index = get_active_generator_index()
        if is_plugin_vst(generator_index):
            plugins.setParamValue(
                msg.data2 / 127,
                4096 + 0x40,
                generator_index,
                useGlobalIndex=True,
            )
            msg.handled = True
