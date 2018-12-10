#!/usr/bin/env python

import collections
import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pprint
from copy import deepcopy

ahi_url="https://my.sa.ucsb.edu/catalog/Current/UndergraduateEducation/AHICourseList.aspx"
ethno_url='https://my.sa.ucsb.edu/catalog/Current/UndergraduateEducation/EthnicityCourses.aspx'

def p2courseNumAndName(p_element):
    courseList = []
    p_text = p_element.text.strip()
    course_num = p_text.split("-", 1)[0].strip()
    child_i_element = p_element.find_elements_by_xpath('i')
    course_name = child_i_element[0].text.strip()
    courseFullName = course_num + ' ' + course_name
##    courseList.append(courseFullName)
    return courseFullName

def getGE(url):
    driver = webdriver.Chrome()
    driver.get(url)

    div_id_content = driver.find_elements_by_xpath("//div[@id='content']")
    div_class_contentpadding = driver.find_elements_by_xpath("//div[@id='content']/div[@class='contentpadding']/p")
    list_of_p_elements = driver.find_elements_by_xpath("//div[@id='content']/div[@class='contentpadding']/p")
    GE_list = list(map(p2courseNumAndName,list_of_p_elements))
    driver.close()
    
    GE_dict = {'Course List': '', 'Requirement': ''}
    if url == ahi_url:
        GE_dict['Requirement'] = 'AHI'
    if url == ethno_url:
        GE_dict['Requirement'] = 'Ethnicity'
    GE_dict['Course List'] = GE_list
    return GE_dict

if __name__=="__main__":
    mydict = getGE(ahi_url)
    other_dict = getGE(ethno_url)


