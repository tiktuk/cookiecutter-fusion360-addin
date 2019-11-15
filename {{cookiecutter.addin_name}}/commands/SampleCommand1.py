
import adsk.core
from ..apper import apper
from ..apper.apper import AppObjects


class SampleCommand1(apper.Fusion360CommandBase):
    def on_execute(self, command: adsk.core.Command, inputs: adsk.core.CommandInputs, args, input_values):
        ao = AppObjects()
        ao.ui.messageBox("Hello {{ cookiecutter.author_name }}")
