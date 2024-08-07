# name=Forward CCs to Active Plugin
"""
A simple script that forwards CC events to the active plugin.

Author: Maddy Guthridge
"""
import plugins
from common import get_active_plugin_index, is_plugin_vst
try:
    from fl_classes import FlMidiMsg
except ImportError:
    FlMidiMsg = 'FlMidiMsg'  # type: ignore


def OnControlChange(msg: FlMidiMsg) -> None:
    plug_index = get_active_plugin_index()
    if is_plugin_vst(*plug_index):
        plugins.setParamValue(
            msg.data2 / 127,
            4096 + msg.data1,
            *plug_index,
            useGlobalIndex=True,
        )
