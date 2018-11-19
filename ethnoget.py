#!/usr/bin/env python

import json
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import pprint
from copy import deepcopy

def p2dict(p_element):
    p_text = p_element.text.strip()
    course_num = p_text.split("-", 1)[0].strip()
    child_i_element = p_element.find_elements_by_xpath('i')
    course_name = child_i_element[0].text.strip()
    
    return {course_num,course_name}

def ethnoReturn():
    ethno_url="https://my.sa.ucsb.edu/catalog/Current/UndergraduateEducation/EthnicityCourses.aspx"


if __name__!="__main__":
    driver = webdriver.Chrome()
    driver.get(ethno_url)
    expected_title = "UC Santa Barbara General Catalog - Ethnicity Requirement Course List"

    stripped_title=driver.title.strip()
    if expected_title == stripped_title:
        print("Found Correct List")
    else:
        print("Cannot Find Correct List")
        print("Instead, found " + stripped_title)

    div_id_content = driver.find_elements_by_xpath("//div[@id='content']")
    div_class_contentpadding = driver.find_elements_by_xpath("//div[@id='content']/div[@class='contentpadding']/p")
    list_of_p_elements = driver.find_elements_by_xpath("//div[@id='content']/div[@class='contentpadding']/p")
##    print(div_id_content)
##    print(div_class_contentpadding)
##    print(list_of_p_elements)

    ethno_dict = dict(list(map(p2dict,list_of_p_elements)))

##        pprint.pprint(ethno_dict)
    driver.close()
    
##if __name__!="__main__":
    return ethno_dict

ethnoReturn()
