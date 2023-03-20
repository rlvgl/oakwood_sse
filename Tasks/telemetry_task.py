# get and send telemetry frame

import MakeTelemFields

from Tasks.template_task import Task
# telem = MakeTelemFields.telem

class task(Task):
    priority = 3
    frequency = 1/10 # once every 10s
    name='telem'
    color = 'pink'
    telem = MakeTelemFields.telem

    async def main_task(self):
        packedFrame = self.telem.getPackedTelemetryFrame()
        return packedFrame
    
    def unpack(self, packedFrame):
        unpackedFrame = self.telem.unpacktTelemetryFrame(packedFrame)
        return unpackedFrame