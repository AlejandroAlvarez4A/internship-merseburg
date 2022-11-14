import tkinter as tk
from tkinter import ttk
import components.ConnectionPort as ConnectionPort
import components.CommandsConsole as CommandsConsole
import components.ArduinoController as ArduinoController
import components.ArrowControl as ArrowControl
import components.CoordinateState as CoordinateState

class ControllerMottors():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Motor controller")
        self.absPosition = [0, 0, 0]
        self.absolutePosicionFrame = ttk.LabelFrame(self.window, text="Absolute position", relief=tk.RIDGE)
        self.statusDisplay = CoordinateState.CoordinateState(self.absolutePosicionFrame, self.absPosition)
        self.arduino = ArduinoController.ArduinoController(self.absPosition, self.statusDisplay)
        self.create_widgets()

    def create_widgets(self):
        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5

        # - - - - - - - - - - - - - - - - - - - - -
        # The Commands frame
        connectionPortFrame = ttk.LabelFrame(self.window, text="Connection Arduino", relief=tk.RIDGE)
        ConnectionPort.ConnectionPort(connectionPortFrame, self.arduino)
        connectionPortFrame.grid(row=1, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        # - - - - - - - - - - - - - - - - - - - - -
        # The Commands console entry frame
        commandsConsoleFrame = ttk.LabelFrame(self.window, text="Commands console", relief=tk.RIDGE)
        CommandsConsole.CommandsConsole(commandsConsoleFrame, self.arduino)
        commandsConsoleFrame.grid(row=2, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        # - - - - - - - - - - - - - - - - - - - - -
        # The Choosing from lists frame
        self.absolutePosicionFrame.grid(row=1, column=2, sticky=tk.E + tk.W + tk.N + tk.S, padx=6)
        
        # - - - - - - - - - - - - - - - - - - - - -
        # Direcctions
        arrowControlFrame = ttk.LabelFrame(self.window, text="Arrow control", relief=tk.RIDGE, padding=6)
        ArrowControl.ArrowControl(arrowControlFrame, self.arduino)
        arrowControlFrame.grid(row=2, column=2, padx=6, sticky=tk.E + tk.W + tk.N + tk.S)

if __name__ == "__main__":
    program = ControllerMottors()
    program.window.mainloop()
    #  template
    # https://runestone.academy/ns/books/published/thinkcspy/GUIandEventDrivenProgramming/03_widgets.html