# name=Simple: Notes and CCs to All Selected Generators
"""
Forwards CC and note events to all selected generator plugins on the channel
rack.

If the active plugin is an FL Studio built-in plugin, events will be ignored,
allowing FL Studio to handle the event itself.

Author: Maddy Guthridge
"""
import plugins
import channels
from common import is_plugin_vst, is_control_mapped
try:
    from fl_classes import FlMidiMsg
except ImportError:
    pass


def OnNoteOn(msg: 'FlMidiMsg') -> None:
    for i in range(channels.channelCount(True)):
        if channels.isChannelSelected(i, True):
            channels.midiNoteOn(i, msg.data1, msg.data2)
            msg.handled = True


def OnNoteOff(msg: 'FlMidiMsg') -> None:
    for i in range(channels.channelCount(True)):
        if channels.isChannelSelected(i, True):
            # Sadly no support for release velocity
            channels.midiNoteOn(i, msg.data1, 0)
            msg.handled = True


def OnControlChange(msg: 'FlMidiMsg') -> None:
    if is_control_mapped(msg):
        return
    for i in range(channels.channelCount(True)):
        if channels.isChannelSelected(i, True):
            if is_plugin_vst(i):
                plugins.setParamValue(
                    msg.data2 / 127,
                    4096 + msg.data1,
                    i,
                    useGlobalIndex=True,
                )
                msg.handled = True
