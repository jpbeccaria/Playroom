# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 17:28:02 2021

@author: Juan
"""



def arithmetic_arranger (lista, solved = False):
    ''' 
Takes a list of addition and subtraction and print in screen the aristmatic arrange typically used by chindrens in school
with a certain format asked for freecodecamp.org exercise

allowed attribute, solved reffears of the posibility of show (or not) the solution of problems

Example = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
  
  
    ''' 
    num = []
    den = []
    oper = []
    
    if len(lista) > 5:
        return 'Error: Too many problems.'
        
    for e in lista:
        if '+' in e:
            num_i, den_i = e.split(' + ')
            num.append(num_i)
            den.append(den_i)
            oper.append('+')
        elif '-' in e:
            num_i, den_i = e.split(' - ')
            num.append(num_i)
            den.append(den_i)
            oper.append('-')
        else:
            return "Error: Operator must be '+' or '-'."
      
    # prepearing lines to print 
    
    bottom = []   # bottom is operators and denominators
    for idx, e in enumerate(den):
        line = oper[idx] + ' ' + den[idx]
        bottom.append(line)
             
    # to print with right justif, we need to know the max len of every problem:
    
    top = [] 
    bottom = []
    lines = []
    dashed_lines = []
          
    for idx, e in enumerate(den):
        length = max(len(num[idx]), len(den[idx]))
        if length >= 5:
            return 'Error: Numbers cannot be more than four digits.'
        top.append(num[idx].rjust(length + 2))
        bottom_temp = den[idx].rjust(length)
        bottom_temp2 = oper[idx] + ' ' + bottom_temp
        bottom.append(bottom_temp2)
        dashed_line = "-" * (length + 2)
        dashed_lines.append(dashed_line)
             
    solves = []
    for idx, e in enumerate(den):
        length = max(len(num[idx]), len(den[idx]))
        if oper[idx] == '+':
            try:
                solve = int(num[idx]) + int(den[idx])
                if len(str(solve)) == length:         
                    solves.append(str(solve).rjust(length + 2))
                else:
                    solves.append(str(solve).rjust(length + 2))
            except:
                return 'Error: Numbers must only contain digits.'
                
    
        else:
            try:
                solve = int(num[idx]) - int(den[idx])
                if len(str(solve)) == length:         
                    solves.append(str(solve).rjust(length + 2))
                else:
                    solves.append(str(solve).rjust(length + 2))
            except:
                 return 'Error: Numbers must only contain digits'
                   
    str_top = "" 
    str_bottom = ""
    str_dash = ""
    str_solves = ""
    
    for idx, e in enumerate(top):
        if idx < len(top) - 1:
            str_top += top[idx] + "    "
            str_bottom += bottom [idx] + "    "
            str_dash += dashed_lines[idx] + "    "
            str_solves += solves[idx] + "    "
        else:
            str_top += top[idx]
            str_bottom += bottom [idx]
            str_dash += dashed_lines[idx]
            str_solves += solves[idx]
    
    if solved:
        string = str_top + '\n' + str_bottom + '\n' + str_dash + '\n' + str_solves
        return string
    else:
        string = str_top + '\n' + str_bottom + '\n' + str_dash
        return string
        

    