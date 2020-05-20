'''
@Time   : 2020/5/8 11:48
@Author : Silence
@File   : TestCase.py
@Description: xxfw http\webservice TestCase
@Version: V1.0.0
'''

import unittest
import requests
import json
from suds.client import Client
import sys

class TestCase(unittest.TestCase):

    httpUrl = "http://172.25.16.7:7070/jrjc/api/xxfw/message/xml";
    webUrl = "http://172.25.16.7:7070/jrjc/services/xxfwWebService?wsdl";

    def jrHttpXml_TestCase(self):
        httpUrl = "http://172.25.16.7:7070/jrjc/api/xxfw/message/xml";
        payload = {
            "sender": "100001",
            "receiver": "100003",
            "type": "TZXX",
            "sjbs": "zxl0TestCase0001",
            "body": "{\"AJMC\":\"AJMC000\",\"JDBH\":\"JDBH000\",\"FSDWBH\":\"100001\",\"XTBS\":\"XTBS000\",\"XXLX\":\"3\",\"FSSJ\":\"2020-04-28 14:32:19\",\"XXNR\":\"XXNR-TEST-\",\"SJBS\":\"zxl0TestCase0000\",\"AJBH\":\"320488FA32EAD704D46FE150CAB2D852\",\"XXZT\":\"XXZT000\",\"PTTYAH\":\"(2020)SichuanNo.207\",\"JSDWBH\":\"100003\",\"YWLB\":\"YWLB_TEST\"}"
        };
        data_json = json.dumps(payload);
        response = requests.post(url=httpUrl, data=data_json);
        print(response.text);
        print(response.status_code);
        #self.assertEqual(response.status_code, 200);


    #suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestCase);
    #unittest.TextTestRunner().run(suite);
    TestCase().jrHttpXml_TestCase();