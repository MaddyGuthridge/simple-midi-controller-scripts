# name=Simple: CCs to Active Plugin
"""
A simple script that forwards CC events to the active plugin.

If the active plugin is an FL Studio built-in plugin, events will be ignored,
allowing FL Studio to handle the event itself.

Author: Maddy Guthridge
"""
import plugins
from common import get_active_plugin_index, is_plugin_vst, is_control_mapped
try:
    from fl_classes import FlMidiMsg
except ImportError:
    pass


def OnControlChange(msg: 'FlMidiMsg') -> None:
    if is_control_mapped(msg):
        return
    plug_index = get_active_plugin_index()
    if is_plugin_vst(*plug_index):
        plugins.setParamValue(
            msg.data2 / 127,
            4096 + msg.data1,
            *plug_index,
            useGlobalIndex=True,
        )
        msg.handled = True
