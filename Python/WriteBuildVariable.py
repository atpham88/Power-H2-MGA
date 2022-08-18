#Michael Craig
#April 24, 2020
#Write .gms file w/ CE text for time blocks and associated constraints

import os

def writeBuildVariable(ceOps,gamsFileDir):
   txt = 'Positive Variable' if ceOps == 'ED' else 'Integer Variable'
   txt += '\n\tvN(tech)\n\t;\n'
   g = open(os.path.join(gamsFileDir,'CEBuildVariable.gms'),'w')
   g.write(txt)
   g.close()