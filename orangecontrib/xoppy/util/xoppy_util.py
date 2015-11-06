__author__ = 'labx'

import sys
import orangecanvas.resources as resources

class locations:
    @classmethod
    def home_bin(cls):
        return resources.package_dirname("orangecontrib.xoppy.util") + "/bin/" + str(sys.platform) + "/"

    @classmethod
    def home_doc(cls):
        return resources.package_dirname("orangecontrib.xoppy.util") + "/doc_txt/"

    @classmethod
    def home_data(cls):
        return resources.package_dirname("orangecontrib.xoppy.util") + "/data/"

    @classmethod
    def home_bin_run(cls):
        return resources.package_dirname("orangecontrib.xoppy.util") + "/bin_run/"


import urllib

XRAY_SERVER_URL = "http://x-server.gmca.aps.anl.gov/"

class HttpManager():

    @classmethod
    def send_xray_server_request(cls, application, parameters):

        data = urllib.parse.urlencode(parameters)
        data = data.encode('utf-8') # data should be bytes
        req = urllib.request.Request(XRAY_SERVER_URL + application, data)
        resp = urllib.request.urlopen(req)

        return resp.read()
