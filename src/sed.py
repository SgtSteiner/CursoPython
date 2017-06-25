# -*- coding: utf-8 -*-
'''
Created on 25 jun. 2017

@author: Steiner
'''

def sed(s_pattern, s_replace, file_source, file_dest):
    fin = open(file_source, "r", encoding="utf8")
    fout = open(file_dest, "w", encoding="utf8")
    for linea in fin:
        linea = linea.replace(s_pattern, s_replace)
        fout.write(linea)
        

def main():
    s_pattern = "una"
    s_replace = "XXX"
    file_source = "LaRegenta.txt"
    file_dest = "LaRegenta_copy.txt"
    sed(s_pattern, s_replace, file_source, file_dest)
    
if __name__ == '__main__':
    try:
        main()
    except:
        print("Algo está ocurriendo...")