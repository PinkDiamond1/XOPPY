import sys
from PyQt4.QtGui import QIntValidator, QDoubleValidator, QApplication
from Orange.widgets import widget, gui
from Orange.widgets.settings import Setting
import numpy as np

class OWxyaup(widget.OWWidget):
    name = "xyaup"
    id = "orange.widgets.dataxyaup"
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

    TITLE = Setting("YAUP EXAMPLE (ESRF BL-8)")
    PERIOD = Setting(4.0)
    NPER = Setting(42)
    NPTS = Setting(40)
    EMIN = Setting(3000.0)
    EMAX = Setting(30000.0)
    NENERGY = Setting(100)
    ENERGY = Setting(6.039999961853027)
    CUR = Setting(0.100000001490116)
    SIGX = Setting(0.425999999046326)
    SIGY = Setting(0.08500000089407)
    SIGX1 = Setting(0.017000000923872)
    SIGY1 = Setting(0.008500000461936)
    D = Setting(30.0)
    XPC = Setting(0.0)
    YPC = Setting(0.0)
    XPS = Setting(2.0)
    YPS = Setting(2.0)
    NXP = Setting(0)
    NYP = Setting(0)
    MODE = Setting(4)
    NSIG = Setting(2)
    TRAJECTORY = Setting("new+keep")
    XSYM = Setting("yes")
    HANNING = Setting(0)
    BFILE = Setting("undul.bf")
    TFILE = Setting("undul.traj")


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
        gui.lineEdit(box1, self, "TITLE",
                     label=self.unitLabels()[idx], addSpace=True)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 1 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "PERIOD",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 2 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "NPER",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=int, validator=QIntValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 3 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "NPTS",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=int, validator=QIntValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 4 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "EMIN",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 5 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "EMAX",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 6 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "NENERGY",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=int, validator=QIntValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 7 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "ENERGY",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 8 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "CUR",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 9 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "SIGX",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 10 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "SIGY",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 11 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "SIGX1",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 12 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "SIGY1",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 13 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "D",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 14 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "XPC",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 15 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "YPC",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 16 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "XPS",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 17 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "YPS",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=float, validator=QDoubleValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 18 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "NXP",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=int, validator=QIntValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 19 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "NYP",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=int, validator=QIntValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 20 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "MODE",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=int, validator=QIntValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 21 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "NSIG",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=int, validator=QIntValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 22 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "TRAJECTORY",
                     label=self.unitLabels()[idx], addSpace=True)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 23 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "XSYM",
                     label=self.unitLabels()[idx], addSpace=True)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 24 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "HANNING",
                     label=self.unitLabels()[idx], addSpace=True,
                    valueType=int, validator=QIntValidator())
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 25 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "BFILE",
                     label=self.unitLabels()[idx], addSpace=True)
        self.show_at(self.unitFlags()[idx], box1) 
        
        #widget index 26 
        idx += 1 
        box1 = gui.widgetBox(box) 
        gui.lineEdit(box1, self, "TFILE",
                     label=self.unitLabels()[idx], addSpace=True)
        self.show_at(self.unitFlags()[idx], box1) 

        gui.rubber(self.controlArea)

    def unitLabels(self):
         return ['Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title','Dummy_title']


    def unitFlags(self):
         return ['True','True','True','True','True','True','True','True','True','True','True','True','True','True','True','True','True','True','True','True','True','True','True','True','True','True','True']


    def unitNames(self):
         return ['TITLE','PERIOD','NPER','NPTS','EMIN','EMAX','NENERGY','ENERGY','CUR','SIGX','SIGY','SIGX1','SIGY1','D','XPC','YPC','XPS','YPS','NXP','NYP','MODE','NSIG','TRAJECTORY','XSYM','HANNING','BFILE','TFILE']


    def help1(self):
        try:
            from xoppy_calc import xoppy_doc
        except ImportError:
            print("help pressed.")
            print("Error importing: xoppy_doc")
            raise

        xoppy_doc('xyaup')


    def compute(self):
        try:
            from xoppy_calc import xoppy_calc_xyaup
        except ImportError:
            print("compute pressed.")
            print("Error importing: xoppy_calc_xyaup")
            raise
            
        fileName = xoppy_calc_xyaup(TITLE=self.TITLE,PERIOD=self.PERIOD,NPER=self.NPER,NPTS=self.NPTS,EMIN=self.EMIN,EMAX=self.EMAX,NENERGY=self.NENERGY,ENERGY=self.ENERGY,CUR=self.CUR,SIGX=self.SIGX,SIGY=self.SIGY,SIGX1=self.SIGX1,SIGY1=self.SIGY1,D=self.D,XPC=self.XPC,YPC=self.YPC,XPS=self.XPS,YPS=self.YPS,NXP=self.NXP,NYP=self.NYP,MODE=self.MODE,NSIG=self.NSIG,TRAJECTORY=self.TRAJECTORY,XSYM=self.XSYM,HANNING=self.HANNING,BFILE=self.BFILE,TFILE=self.TFILE)
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
    w = OWxyaup()
    w.show()
    app.exec()
    w.saveSettings()
