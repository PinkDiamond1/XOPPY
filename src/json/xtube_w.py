import sys
from PyQt4.QtGui import QIntValidator, QDoubleValidator, QApplication
from Orange.widgets import widget, gui
from Orange.widgets.settings import Setting
import numpy as np

class OWxtube_w(widget.OWWidget):
    name = "xtube_w"
    id = "orange.widgets.dataxtube_w"
    description = "xoppy application to compute..."
    icon = "icons/xoppy.png"
    author = "create_widget.py"
    maintainer_email = "srio@esrf.eu"
    priority = 10
    category = ""
    keywords = ["list", "of", "keywords"]
    #outputs = [{"name": "xoppy_data",
    #            "type": np.ndarray,
    #            "doc": ""}]
    outputs = [{"name": "xoppy_data",
                "type": np.ndarray,
                "doc": ""},
               {"name": "xoppy_file",
                "type": str,
                "doc": ""}]

    #inputs = [{"name": "Name",
    #           "type": type,
    #           "handler": None,
    #           "doc": ""}]

    want_main_area = False

    VOLTAGE = Setting(100.0)
    RIPPLE = Setting(0.0)
    AL_FILTER = Setting(0.0)


    def __init__(self):
        super().__init__()

        box0 = gui.widgetBox(self.controlArea, " ",orientation="horizontal") 
        #widget buttons: compute, set defaults, help
        gui.button(box0, self, "Compute", callback=self.compute)
        gui.button(box0, self, "Set defaults", callback=self.resetSettings)
        gui.button(box0, self, "Help", callback=self.help1)
        self.process_showers()
        box = gui.widgetBox(self.controlArea, " ",orientation="vertical") 
        
        
        idx = -1 
        
        #widget index 0 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "VOLTAGE",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 1 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "RIPPLE",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 2 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "AL_FILTER",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 

        gui.rubber(self.controlArea)

    def unitLabels(self):
         return ['Voltage 30<V<140 (kV)','Voltage ripple (%)','Al filter [mm]']


    def unitFlags(self):
         return ['True','True','True']


    def unitNames(self):
         return ['VOLTAGE','RIPPLE','AL_FILTER']


    def help1(self):
        try:
            from xoppy_calc import xoppy_doc
        except ImportError:
            print("help pressed.")
            print("Error importing: xoppy_doc")
            raise

        xoppy_doc('xtube_w')


    def compute(self):
        try:
            from xoppy_calc import xoppy_calc_xtube_w
        except ImportError:
            print("compute pressed.")
            print("Error importing: xoppy_calc_xtube_w")
            raise
            
        fileName = xoppy_calc_xtube_w(VOLTAGE=self.VOLTAGE,RIPPLE=self.RIPPLE,AL_FILTER=self.AL_FILTER)
        print("Loading file:  ",fileName)
        out = np.loadtxt(fileName)
        print("out.shape: ",out.shape)
        self.send("xoppy_data",out)

    def process_showers(self):

        from PyQt4.QtGui import QLayout
        self.layout().setSizeConstraint(QLayout.SetFixedSize)

        for shower in getattr(self, "showers", []):
            shower()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = OWxtube_w()
    w.show()
    app.exec()
    w.saveSettings()
