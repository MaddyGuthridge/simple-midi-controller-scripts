"""
# Common.py

Common utility functions, shared between all scripts.
"""
import plugins
import ui
import midi
import channels


last_active_generator = 0
"""Index of the last active generator plugin"""


def is_plugin_vst(index: int, slotIndex: int = -1) -> bool:
    """
    Plugins are a VST if they have 4240 parameters
    """
    return plugins.getParamCount(index, slotIndex, True) == 4240


def get_active_generator_index() -> int:
    """
    Returns the track index (and optionally slot index) of the active plugin
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

