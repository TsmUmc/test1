# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 09:32:37 2021

@author: Administrator
"""

import xml.etree.ElementTree as et
tree=et.parse('menu.xml')
root=tree.getroot()
# print(root.tag)
for i in root.findall('menu'):
    price=int(i.find('lunch').text)
              # 
    if price>=70:
        root.remove(price)
    # print('tag:',i.tag,'att:',i.attrib)
    # for j in root:    
    #     print('\ttag:',j.tag,'att:',j.attrib)
# print(len(root))
# print(len(root[0]))       
tree.write('menu.xml')