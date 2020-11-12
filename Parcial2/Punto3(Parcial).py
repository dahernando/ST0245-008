#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 11:27:36 2020

@author: daho
"""

def calcularPost(pre, inor):
    if pre == "" or inor == "":
        return ""
    if len(pre) == 1 or len(inor) == 1:
        return pre or inor
    post = ""
    inorI= ""
    inorD = ""
    preI = ""
    preD = ""
    i = 0
    while inor[i] != pre[0]:
        inorI += inor[i]
        i += 1
    i += 1
    while i < len(inor):
        inorD += inor[i]
        i += 1
    i = 0
    for j in pre:
        if j in inorI:
            preI += j
        if j in inorD:
            preD += j
    post = post + calcularPost(preI, inorI) + calcularPost(preD, inorD) + pre[0]
    return post

print(calcularPost("GEAIBMCLDFKJH", "IABEGLDCFMKHJ"))