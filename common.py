"""
# Common.py

Common utility functions, shared between all scripts.
"""
import plugins
import ui
import midi
import channels
import mixer
import device
try:
    from fl_classes import FlMidiMsg
except ImportError:
    FlMidiMsg = 'FlMidiMsg'  # type: ignore


last_active_generator = 0
"""Index of the last active generator plugin"""
last_active_plugin = (0, -1)
"""Index of the last active generator or FX plugin"""


def is_control_mapped(msg: FlMidiMsg) -> bool:
    """Returns whether a control has been mapped by the user"""
    port = device.getPortNumber()
    event_id = midi.EncodeRemoteControlID(port, msg.status & 0xF, msg.data1)
    return device.getLinkedInfo(event_id) != -1


def is_plugin_vst(index: int, slotIndex: int = -1) -> bool:
    """
    Plugins are a VST if they have 4240 parameters
    """
    return plugins.getParamCount(index, slotIndex, True) == 4240


def get_active_generator_index() -> int:
    """
    Returns the track index of the active generator plugin
    """
    global last_active_generator
    # Update the current last active plugin if a plugin or the channel rack is
    # focused
    if (
        ui.getFocused(midi.widChannelRack)
        or ui.getFocused(midi.widPluginGenerator)
    ):
        last_active_generator = channels.channelNumber()
        return last_active_generator
    # Otherwise use the cached value
    else:
        return last_active_generator


def get_active_plugin_index() -> tuple[int, int]:
    """
    Returns the track index (and optionally slot index) of the active plugin.
    """
    global last_active_plugin
    # Update the current last active plugin if a plugin or the channel rack is
    # focused
    if (
        ui.getFocused(midi.widChannelRack)
        or ui.getFocused(midi.widPluginGenerator)
    ):
        last_active_plugin = (channels.channelNumber(), -1)
        return last_active_plugin
    # Or if the mixer or an FX plugin is focused
    elif (
        ui.getFocused(midi.widMixer)
        or ui.getFocused(midi.widPluginEffect)
    ):
        fx_plug = mixer.getActiveEffectIndex()
        if fx_plug is not None:
            last_active_plugin = fx_plug
        return last_active_plugin
    # Otherwise use the cached value
    else:
        return last_active_plugin
