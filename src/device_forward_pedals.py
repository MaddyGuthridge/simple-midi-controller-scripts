# name=Forward Pedal Events to Active Plugin
import plugins
from common import get_active_generator_index, is_plugin_vst
try:
    from fl_classes import FlMidiMsg
except ImportError:
    FlMidiMsg = 'FlMidiMsg'  # type: ignore


def OnControlChange(msg: FlMidiMsg) -> None:
    if msg.data1 == 0x40:
        generator_index = get_active_generator_index()
        if is_plugin_vst(generator_index):
            plugins.setParamValue(
                msg.data2,
                4096 + 0x40,
                generator_index,
                useGlobalIndex=True,
            )
