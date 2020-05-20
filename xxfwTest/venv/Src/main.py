# -*- coding: UTF-8 -*-

import requests
import json
from suds.client import Client
import sys
import unittest



#todo: XTYPT jrHttp XML /jrjc/api/xxfw/message/xml
#param: fsf; jsf; xxlx; sjbs; body
#tpt: xml jc 法院100001; json jc 检察院 100003
def jrHttpXml():
    url = 'http://172.25.16.7:7070/jrjc/api/xxfw/message/xml';
    payload = {
  "fsf": "100001",
  "jsf": "100003",
  "xxlx": "TZXX",
  "sjbs": "zxl0testHttpXMl0001b",
  "body": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><CaseInfo><PTTYAH>zxl0testHttpXMl0001b</PTTYAH><SJBS>zxl0testHttpXMl0001b</SJBS><XTBS>F56E1AE20ADAA70E11D44171A4C91F7F</XTBS><XXLX>3</XXLX><AJBH>320488FA32EAD704D46FE150CAB2D852</AJBH><AJMC>案件</AJMC><YWLB>业务类别业务类别业务类别</YWLB><JDBH>F8701F8C010F4B270F0BCB0128D0DCCB</JDBH><XXZT>消息状态消息状态消息状态消息状态消息</XXZT><XXNR>消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消息内容消</XXNR><FSDWBH>100001</FSDWBH><JSDWBH>100003</JSDWBH><FSSJ>2020-04-28 14:32:19</FSSJ></CaseInfo>"
};
    data_json = json.dumps(payload);
    response = requests.post(url=url, data=data_json);
    print(response.text);

# 必填项校验测试
def jrHttpXml_TestCase1():
    url = 'http://172.25.16.7:7070/jrjc/api/xxfw/message/xml';
    payload = {
        "fsf": "100003",
        "jsf": "100001",
        "xxlx": "TZXX",
        "sjbs": "zxl0testHttpXMl0021",
        "body": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><CaseInfo><PTTYAH>zxl0testHttpXMl0021</PTTYAH><SJBS>zxl0testHttpXMl0021</SJBS><XTBS>Test-0</XTBS><XXLX>TZXX</XXLX><AJBH>7A8319FA87539643F187BEF30D727DFE</AJBH><AJMC></AJMC><YWLB>Test-YWLB</YWLB><JDBH>Test-JDBH</JDBH><XXZT>Test-XXZT</XXZT><XXNR>This is the notifation</XXNR><FSDWBH>100001</FSDWBH><JSDWBH>100003</JSDWBH><FSSJ>2020-04-28 14:32:19</FSSJ><XZNR>This is the addition</XZNR></CaseInfo>"
    };
    data_json = json.dumps(payload);
    response = requests.post(url=url, data=data_json);
    print(response.text);

def jrHttpXml_TestCase2():
    '''
    :description: 消息体字段类型校验 - FSSJ为DT，消息体中传D
    :return:
    '''
    url = 'http://172.25.16.7:7070/jrjc/api/xxfw/message/xml';
    payload = {
        "fsf": "100003",
        "jsf": "100001",
        "xxlx": "TZXX",
        "sjbs": "zxl0testHttpXMl0200",
        "body": "<?xml version=\"1.0\" encoding=\"UTF-8\"?><CaseInfo><PTTYAH>zxl0testHttpXMl0200</PTTYAH><SJBS>zxl0testHttpXMl0200</SJBS><XTBS>Test-0</XTBS><XXLX>TZXX</XXLX><AJBH>7A8319FA87539643F187BEF30D727DFE</AJBH><AJMC></AJMC><YWLB>Test-YWLB</YWLB><JDBH>Test-JDBH</JDBH><XXZT>Test-XXZT</XXZT><XXNR>This is the notifation</XXNR><FSDWBH>100001</FSDWBH><JSDWBH>100003</JSDWBH><FSSJ>2020-05-08</FSSJ><XZNR>This is the addition</XZNR></CaseInfo>"
    }
    data_json = json.dumps(payload);
    response = requests.post(url=url, data=data_json);
    print(response.text);

# todo: XTYPT jrHttp Json /jrjc/api/xxfw/message/json
# param: fsf; jsf; xxlx; sjbs; body
def jrHttpJson():
    url = "http://172.25.16.7:7070/jrjc/api/xxfw/message/json"
    payload = {
            "fsf": "100001",
            "jsf": "100003",
            "xxlx": "TZXX",
            "sjbs": "zxl0TestJson0004",
            "body": "{\"AJMC\":\"AJMC000\",\"JDBH\":\"JDBH000\",\"FSDWBH\":\"100001\",\"XTBS\":\"XTBS000\",\"XXLX\":\"3\",\"FSSJ\":\"2020-04-28 14:32:19\",\"XXNR\":\"XXNR-TEST-\",\"SJBS\":\"zxl0TestJson0004\",\"AJBH\":\"320488FA32EAD704D46FE150CAB2D852\",\"XXZT\":\"XXZT000\",\"PTTYAH\":\"zxl0TestJson0004\",\"JSDWBH\":\"100003\",\"YWLB\":\"YWLB_TEST\"}"
    };
    data_json = json.dumps(payload);
    response = requests.post(url=url,data=data_json)
    print(response.text)

def jrWebXml():
    '''
    :todo: XTYPT jr webservice xml
    :url: /jrjc/services/xxfwWebService?wsdl
    :namespace: http://service.webservice.xxfw.thunisoft.com/
    :method:sendXmlMessage(xs:string fsf, xs:string jsf, xs:string xxlx, xs:string sjbs, xs:string body)
    :return:
    '''
    url = "http://172.25.16.7:7070/jrjc/services/xxfwWebService?wsdl";
    client = Client(url);
    #print(client);
    response = client.service.sendXmlMessage(fsf = "100001", jsf = "100003",xxlx = "TZXX",
                                  sjbs = "zxl0TestWeb0Xml0006", body = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><CaseInfo><PTTYAH>zxl0TestWeb0Xml0006</PTTYAH><SJBS>zxl0TestWeb0Xml0006</SJBS><XTBS>Test-0</XTBS><XXLX>TZXX</XXLX><AJBH>7A8319FA87539643F187BEF30D727DFE</AJBH><AJMC>案件名称</AJMC><YWLB>Test-YWLB</YWLB><JDBH>Test-JDBH</JDBH><XXZT>Test-XXZT</XXZT><XXNR>This is the notifation</XXNR><FSDWBH>100001</FSDWBH><JSDWBH>100003</JSDWBH><FSSJ>2020-04-28 14:32:19</FSSJ><XZNR>This is the addition</XZNR></CaseInfo>");
    print(response)

def jrWebXml_TestCase1():
    '''
    :todo: xml根节点含namespace
    :return:
    '''
    url = "http://172.25.16.7:7070/jrjc/services/xxfwWebService?wsdl";
    client = Client(url);
    # print(client);
    response = client.service.sendXmlMessage(fsf="100003", jsf="100001", xxlx="TZXX",
                                             sjbs="zxl0TestWeb0Xml0012",
                                             body="<?xml version=\"1.0\" encoding=\"UTF-8\"?><CaseInfo xmlns=\"http://EDI.court.gov.cn/2016\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://EDI.court.gov.cn/2016/data 0201_刑事一审案件.xsd\"><PTTYAH>zxl0TestWeb0Xml0012</PTTYAH><SJBS>zxl0TestWeb0Xml0012</SJBS><XTBS>Test-0</XTBS><XXLX>TZXX</XXLX><AJBH>7A8319FA87539643F187BEF30D727DFE</AJBH><AJMC>案件名称</AJMC><YWLB>Test-YWLB</YWLB><JDBH>Test-JDBH</JDBH><XXZT>Test-XXZT</XXZT><XXNR>This is the notifation</XXNR><FSDWBH>100003</FSDWBH><JSDWBH>100001</JSDWBH><FSSJ>2020-04-28 14:32:19</FSSJ><XZNR>This is the addition</XZNR></CaseInfo>");
    print(response);


def jrWebXml_TestCase2():
    '''
    :description: 消息体中jsf、sjbs与参数中不符合
    :return: 以参数中的数据为准
    '''
    url = "http://172.25.16.7:7070/jrjc/services/xxfwWebService?wsdl";
    client = Client(url);
    fsf = "100003";
    jsf = "100001";
    xxlx = "TZXX";
    sjbs = "zxl0TestWeb0Xml0100";
    response = client.service.sendXmlMessage(fsf = fsf, jsf = jsf, xxlx = xxlx,
                                             sjbs = sjbs,
                                             body = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><CaseInfo><PTTYAH>zxl0TestWeb0Xml0100</PTTYAH><SJBS>zxl0TestWeb0Xml0100</SJBS><XTBS>Test-0</XTBS><XXLX>TZXX</XXLX><AJBH>7A8319FA87539643F187BEF30D727DFE</AJBH><AJMC>案件名称</AJMC><YWLB>Test-YWLB</YWLB><JDBH>Test-JDBH</JDBH><XXZT>Test-XXZT</XXZT><XXNR>This is the notifation</XXNR><FSDWBH>Null</FSDWBH><JSDWBH>100003</JSDWBH><FSSJ>2020-04-28 14:32:19</FSSJ><XZNR>This is the addition</XZNR></CaseInfo>");
    print(response);

def jrWebXml_TestCase3():
    '''
    :description: 消息体中有表结构不符合的数据C_Test
    :return: 不处理Test数据项
    '''
    url = "http://172.25.16.7:7070/jrjc/services/xxfwWebService?wsdl";
    client = Client(url);
    fsf = "100003";
    jsf = "100001";
    xxlx = "TZXX";
    sjbs = "zxl0TestWeb0Xml0300";
    response = client.service.sendXmlMessage(fsf=fsf, jsf=jsf, xxlx=xxlx,
                                             sjbs=sjbs,
                                             body="<?xml version=\"1.0\" encoding=\"UTF-8\"?><CaseInfo><PTTYAH>zxl0TestWeb0Xml0300</PTTYAH><SJBS>zxl0TestWeb0Xml0300</SJBS><XTBS>Test-0</XTBS><XXLX>TZXX</XXLX><AJBH>7A8319FA87539643F187BEF30D727DFE</AJBH><AJMC>案件名称</AJMC><YWLB>Test-YWLB</YWLB><JDBH>Test-JDBH</JDBH><XXZT>Test-XXZT</XXZT><XXNR>This is the notifation</XXNR><FSDWBH>Null</FSDWBH><JSDWBH>100003</JSDWBH><FSSJ>2020-04-28 14:32:19</FSSJ><XZNR>This is the addition</XZNR><Test>测试字段</Test></CaseInfo>");
    print(response);

def jrWebJson():
    '''
    :todo: XTYPT JR JSON webservice
    :method: sendJsonMessage(xs:string fsf, xs:string jsf, xs:string xxlx, xs:string sjbs, xs:string body)
    :return:
    '''
    url = "http://172.25.16.7:7070/jrjc/services/xxfwWebService?wsdl";
    client = Client(url);
    response = client.service.sendJsonMessage(fsf = "100001", jsf = "100003", xxlx = "TZXX",
                                              sjbs = "zxl0TestWeb0Json0002",
                                              body = "{\"AJMC\":\"AJMC000\",\"SJBS\":\"zxl0TestWeb0Json0002\",\"JDBH\":\"JDBH000\",\"FSDWBH\":\"100001\",\"XTBS\":\"XTBS000\",\"XXLX\":\"3\",\"FSSJ\":\"2020-04-28 14:32:19\",\"XXNR\":\"XXNR-TEST-\",\"AJBH\":\"320488FA32EAD704D46FE150CAB2D852\",\"XXZT\":\"XXZT000\",\"PTTYAH\":\"zxl0TestWeb0Json0002\",\"JSDWBH\":\"100003\",\"YWLB\":\"YWLB_TEST\"}");
    print(response);

def jrWebJson_TestCase1():
    '''
    :description: 接口参数部分数据为空
    :return: 300
    '''
    url = "http://172.25.16.7:7070/jrjc/services/xxfwWebService?wsdl";
    client = Client(url);
    response = client.service.sendJsonMessage(fsf="100001", jsf="", xxlx="TZXX",
                                              sjbs="zxl0TestWeb0Json0003",
                                              body="{\"AJMC\":\"AJMC000\",\"SJBS\":\"zxl0TestWeb0Json0003\",\"JDBH\":\"JDBH000\",\"FSDWBH\":\"100001\",\"XTBS\":\"XTBS000\",\"XXLX\":\"3\",\"FSSJ\":\"2020-04-28 14:32:19\",\"XXNR\":\"XXNR-TEST-\",\"AJBH\":\"320488FA32EAD704D46FE150CAB2D852\",\"XXZT\":\"XXZT000\",\"PTTYAH\":\"zxl0TestWeb0Json0003\",\"JSDWBH\":\"100003\",\"YWLB\":\"YWLB_TEST\"}");
    print(response);

if __name__ == '__main__':

    print("接入业务系统请求平台接入XML http 接口\n");

    jrHttpXml();#zxl0testHttpXMl0001b

    jrHttpXml_TestCase1();#zxl0testHttpXMl0021

    jrHttpXml_TestCase2();#zxl0testHttpXMl0200

    print("\n\n接入业务系统请求平台接入Json http 接口\n");
    jrHttpJson(); #zxl0TestJson0004

    print("\n\n接入业务系统请求平台接入XML webservice 接口\n");
    jrWebXml(); #zxl0TestWeb0Xml0006
    jrWebXml_TestCase1();#zxl0TestWeb0Xml0012
    jrWebXml_TestCase2();#zxl0TestWeb0Xml0100
    jrWebXml_TestCase3();#zxl0TestWeb0Xml0300
    
    print("\n\n接入业务系统请求平台接入Json webservice 接口\n");
    jrWebJson();#zxl0TestWeb0Json0002
    jrWebJson_TestCase1();#zxl0TestWeb0Json0003
    jrWebJson();#zxl0TestWeb0Json0002
