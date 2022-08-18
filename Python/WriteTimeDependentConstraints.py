#Michael Craig
#April 24, 2020
#Write .gms file w/ CE text for time blocks and associated constraints

import os
from GAMSAddSetToDatabaseFuncs import createHourSubsetName

def writeTimeDependentConstraints(blockNamesChronoList,stoInCE,seasSto,gamsFileDir,ceOps,lastRepBlockNames,specialBlocksPrior):
   setText,setDefns = writeSets(blockNamesChronoList,stoInCE)
   paramText,paramDefns = writeParameters(blockNamesChronoList,stoInCE,seasSto,ceOps)
   importText = writeImport(blockNamesChronoList,stoInCE,seasSto,ceOps) 
   varText = writeVariables(blockNamesChronoList) if seasSto else ''
   eqnText = writeEquationsNames(blockNamesChronoList,stoInCE,seasSto,ceOps)
   eqnText += writeEquations(blockNamesChronoList,stoInCE,seasSto,ceOps,lastRepBlockNames,specialBlocksPrior)
   allText = setText + paramText + importText + paramDefns + setDefns + varText + eqnText
   g = open(os.path.join(gamsFileDir,'CETimeDependentConstraints.gms'),'w')
   g.write(allText)
   g.close()

def writeSets(blockNamesChronoList,stoInCE):
   setText,setDefns = 'Sets\n','\n'
   #Create names for set blocks
   for nB in blockNamesChronoList: setText += '\t' + createHourSubsetName(nB) + '(h)\n'
   #Set which hours are not initial hours
   if stoInCE:
      nonInit = 'nonInitH(h)'
      setDefns += nonInit + '= yes;\n'
      for nB in blockNamesChronoList:
         setDefns += nonInit + '$[ord(h)=' + createInitHourName(nB) + '] = no;\n'
   return setText + '\t;\n',setDefns

def writeParameters(blockNamesChronoList,stoInCE,seasSto,ceOps):
   paramText,paramDefns = 'Parameters\n','\n'
   #Weights to scale up costs and emissions
   for nB in blockNamesChronoList: paramText += '\tpWeight' + createHourSubsetName(nB) + '\n'
   #Init SOC parameters, initial hour, and final hour parameters
   if stoInCE:
      for et in ['storageegu','storagetech']: paramText += createNameWithSets('pInitSOC',et) + '\n'
      for nB in blockNamesChronoList: 
         nBInitHour = createInitHourName(nB)
         nBFinalHour = createFinalHourName(nB)
         paramText += '\t' + nBInitHour + '\n' + '\t' + nBFinalHour + '\n'
         if seasSto:
            paramText += '\tpSOCScalar{0}\n'.format(createHourSubsetName(nB)) if nB != blockNamesChronoList[0] else '' #no SOC scalar for first block
         paramDefns += nBInitHour + ' = smin(h$' + createHourSubsetName(nB) + '(h),ord(h));\n'
         paramDefns += nBFinalHour + ' = smax(h$' + createHourSubsetName(nB) + '(h),ord(h));\n'
         if ceOps == 'UC': paramText += 'pOnoroffinit' + createHourSubsetName(nB) + '(egu)\n'
   return '\n' + paramText + '\t;\n',paramDefns

def createInitSOCName(nB):
   return 'pInitSOC' + createHourSubsetName(nB)

def createFinalHourName(nB):
   return 'pHourFinal' + createHourSubsetName(nB)

def createInitHourName(nB):
   return 'pHourInit' + createHourSubsetName(nB)# + createSetsText(['h'])

#Write $load block text for importing parameters defined above
def writeImport(blockNamesChronoList,stoInCE,seasSto,ceOps):
   importText = """\n$if not set gdxincname $abort 'no include file name for data file provided'\n"""
   importText += '$gdxin %gdxincname%\n'
   blocks = ','.join([createHourSubsetName(nB) for nB in blockNamesChronoList])
   weights = ','.join(['pWeight' + createHourSubsetName(nB) for nB in blockNamesChronoList])
   if stoInCE:
      if seasSto:
         scalars = ','.join(['pSOCScalar' + createHourSubsetName(nB) for nB in blockNamesChronoList[1:]]) #no SOC scalar for first block
      ets,initSOCs = ['storageegu','storagetech'],''
      initSOCs += ','.join(['pInitSOC' + techLbl(et) for et in ets]) + ','
   if ceOps == 'UC': onOffInits = ','.join(['pOnoroffinit' + createHourSubsetName(nB) for nB in blockNamesChronoList])
   #Combine all text
   if stoInCE and seasSto: allText = [blocks,weights,scalars,initSOCs.rstrip(',')]
   elif stoInCE: allText = [blocks,weights,initSOCs.rstrip(',')]
   else: allText = [blocks,weights]
   if ceOps == 'UC': allText += [onOffInits]
   importText += '\n'.join(['$load ' + l for l in allText])
   return importText + '\n$gdxin\n'

#Write variables
def writeVariables(blockNamesChronoList):
   varText = '\nVariables\n'
   for v in ['vInitSOC']:
      for et in ['storageegu','storagetech']: 
         for nB in blockNamesChronoList[1:]:
            varText += ('\t' + v + createHourSubsetName(nB) + techLbl(et) + '(' + et + ')' + '\n')
   for v in ['vFinalSOC','vChangeSOC']:
      for et in ['storageegu','storagetech']: 
         for nB in blockNamesChronoList:
            varText += ('\t' + v + createHourSubsetName(nB) + techLbl(et) + '(' + et + ')' + '\n')
   return varText + '\t;\n'

#Write equation names
def writeEquationsNames(blockNamesChronoList,stoInCE,seasSto,ceOps):
   eqnText = '\nEquations\n'
   gens,stos = ['egu','tech'],['storageegu','storagetech']
   for eqn in ['varCost','co2Ems']: eqnText += '\t' + eqn + '\n'
   if stoInCE:
      for et in stos:
         for eqn in ['defSOC','genPlusUpResToSOC']:
            eqnText += createNameWithSets(eqn,et,'h') + '\n'
         if seasSto:
            for nB in blockNamesChronoList[1:]:
               eqnText += 'setInitSOC{b}{e}({e})'.format(b=createHourSubsetName(nB),e='lt'+et) + '\n'
               # createNameWithSets('setInitSOC'+createHourSubsetName(nB)+'lt','lt' + et) + '\n'
            for nB in blockNamesChronoList:
               eqnText += createNameWithSets('defFinalSOC'+createHourSubsetName(nB),et,'h') + '\n'
               eqnText += createNameWithSets('defChangeSOC'+createHourSubsetName(nB),et) + '\n'
         for nB in blockNamesChronoList[1:]:
               eqnText += 'setInitSOC{b}{e}({e})'.format(b=createHourSubsetName(nB),e='st'+et) + '\n'
   for g in gens:
      for nB in blockNamesChronoList:
         eqnText += createNameWithSets('rampUp'+createHourSubsetName(nB),g,createHourSubsetName(nB)) + '\n'
         if ceOps == 'UC': eqnText += createNameWithSets('commitment'+createHourSubsetName(nB),g,createHourSubsetName(nB)) + '\n'
   return eqnText + '\t;\n'

def createNameWithSets(eqn,*argv):
   setsText = createSetsText(argv)
   return '\t' + eqn + techLbl(setsText) + setsText

def createSetsText(args):
   setsText = '(' 
   for arg in args: setsText += arg + ',' 
   return setsText.rstrip(',') + ')'

def techLbl(et):
   return 'tech' if 'tech' in et else ''

def getGenPlusReserves(et,setsText):
   return 'vGen{0}{1}+vRegup{0}{1}+vFlex{0}{1}+vCont{0}{1}'.format(techLbl(et),setsText)

def getGenAboveMinPlusReserves(et,setsText):
   return 'vGenabovemin{0}{1}+vRegup{0}{1}+vFlex{0}{1}+vCont{0}{1}'.format(techLbl(et),setsText)   

#Write equations
def writeEquations(blockNamesChronoList,stoInCE,seasSto,ceOps,lastRepBlockNames,specialBlocksPrior):
   eqns = ''
   #Storage equations
   if stoInCE:
      for et in ['storageegu','storagetech']:
         eqns += '\n'
         setsText = createSetsText([et,'h'])

         #create text for initial SOC in each time block (pInitSOC in first block & vInitSOC for other blocks)
         initsText = ''
         for nB in blockNamesChronoList:
            if nB == blockNamesChronoList[0]: socName = 'pInitSOC'
            else: socName = ' + vInitSOC' + createHourSubsetName(nB)
            # socName += createHourSubsetName(nB) #10/20/21
            initsText += '{0}{1}({2})$[ord(h)={3}]'.format(socName,techLbl(et),et,createInitHourName(nB))
            if 'tech' in et and 'pInit' in socName: initsText += '*vEneBuiltSto({t})'.format(t=et) #multiply by # built if pInit (otherwise RHS > 0)

         #defSOC
         socDefnSharedText = '''vStateofcharge{0}({1}, h-1)$nonInitH(h) - 
               1/sqrt(pEfficiency{0}({1})) * vGen{0}({1},h) + 
               sqrt(pEfficiency{0}({1})) * vCharge{0}({1},h)'''.format(techLbl(et),et)
         eqns += 'defSOC{0}{1}.. vStateofcharge{0}{1} =e= {2} +\n\t{3};\n'.format(techLbl(et),setsText,initsText,socDefnSharedText)
         #genPlusUpResToSOC
         genSOCSharedText = getGenPlusReserves(et,setsText)
         eqns += '''genPlusUpResToSOC{0}{1}.. {2} =l= vStateofcharge{0}({3}, h-1)$nonInitH(h)
                     + {4};\n'''.format(techLbl(et),setsText,genSOCSharedText,et,initsText) 

         #set initial SOC variable for long-term (seasonal) (lt) storage
         if seasSto:
            #define initial SOC
            for bNum in range(1,len(blockNamesChronoList)):
               nB,blockName = blockNamesChronoList[bNum],createHourSubsetName(blockNamesChronoList[bNum])
               lastBlock,priorSpBlocks = lastRepBlockNames[nB],specialBlocksPrior[nB]
               socChangeText = ''
               for psb in priorSpBlocks: socChangeText += '+ vChangeSOC{b}{t}({e})'.format(b=createHourSubsetName(psb),t=techLbl(et),e='lt'+et)
               eqns += '''setInitSOC{b}{e}({e}).. vInitSOC{b}{t}({e}) =e= vFinalSOC{blast}{t}({e}) + vChangeSOC{blast}{t}({e})*pSOCScalar{b} {sct}
                        ;\n'''.format(b=blockName,blast=createHourSubsetName(lastBlock),t=techLbl(et),e='lt'+et,i=createInitHourName(nB),sct=socChangeText)
            #set final and change in SOC for lt storage
            for nB in blockNamesChronoList:
               finalSOCText = 'vFinalSOC' + '{b}{t}({s})'.format(b=createHourSubsetName(nB),t=techLbl(et),s='lt'+et)
               eqns += '''defFinalSOC{b}{t}({e},h)$[ord(h)=pHourFinal{b}].. vFinalSOC{b}{t}({e}) =e= 
                           vStateofcharge{t}({e},h);\n'''.format(b=createHourSubsetName(nB),t=techLbl(et),
                           e='lt'+et)
               initSOCText = 'pInitSOC' if nB == blockNamesChronoList[0] else 'vInitSOC' + createHourSubsetName(nB)
               initSOCText += '{t}({s})'.format(t=techLbl(et),s='lt'+et)
               if 'tech' in et and 'pInit' in initSOCText: initSOCText += '*vEneBuiltSto({s})'.format(s='lt'+et) #multiply by # built if pInit (otherwise RHS > 0)
               eqns += '''defChangeSOC{0}{1}({2}).. vChangeSOC{0}{1}({2}) =e= vFinalSOC{0}{1}({2}) 
                              - {3};\n'''.format(createHourSubsetName(nB),techLbl(et),'lt'+et,initSOCText)

         #set initial SOC for short-term (st) storage as fixed initial SOC fraction
         for bNum in range(1,len(blockNamesChronoList)):
            blockName = createHourSubsetName(blockNamesChronoList[bNum])
            setInitSocSTSto = '''setInitSOC{b}{e}({e}).. vInitSOC{b}{t}({e}) =l= 
                                    pInitSOC{t}({e})'''.format(b=blockName,t=techLbl(et),e='st'+et)
            setInitSocSTSto = setInitSocSTSto + ('*vEneBuiltSto({e})'.format(e='st'+et) if 'tech' in et else '') + ';\n'                   
            eqns += setInitSocSTSto

   #Emission and cost equations
   eqns += '\n'
   eguSets = ['egu','tech']
   for v,eqn in zip(['vVarcost','vCO2ems'],['varCost','co2Ems']):
      blockText = ''
      for nB in blockNamesChronoList:
         blockText += ('\n\t+ ' if nB != blockNamesChronoList[0] else '') + 'pWeight' + createHourSubsetName(nB) + '*('
         for et in eguSets:
            setsText = createSetsText([et,createHourSubsetName(nB)])
            if v == 'vVarcost' and ceOps == 'UC': #add in turn on cost
               startCost = '+pStartupfixedcost{t}({e})*vTurnon{t}{s}'.format(t=techLbl(et),e=et,s=setsText)
            else:
               startCost = ''
            blockText += 'sum({s},{v}{t}{s}{sc}){p}'.format(s=setsText,v=v,t=techLbl(et),p='+' if et != eguSets[-1] else '',sc=startCost)
         blockText += '))' #close pWeight parens
         blockText = blockText[:-1] #drop trailing +
      eqns += '{0}.. {1}annual =e= {2};\n'.format(eqn,v,blockText)
   #Ramp ups
   eqns += '\n'
   for nB in blockNamesChronoList:
      for et in eguSets:
         setsText = createSetsText([et,createHourSubsetName(nB)])
         rhs = 'pRamprate{t}({e})'.format(t=techLbl(et),e=et)
         if ceOps == 'ED': 
            genPlusRes = getGenPlusReserves(et,setsText)
            genName = 'vGen'
            if et == 'tech': rhs += '*vN({e})'.format(e=et)
         else: 
            genPlusRes = getGenAboveMinPlusReserves(et,setsText)
            genName = 'vGenabovemin'
            if et == 'tech': rhs += '*vOnorofftech({e},{b}-1) + vTurnontech{s}*pCapactech({e})'.format(e=et,b=createHourSubsetName(nB),
                                                                                                      s=setsText)
         eqns += '''rampUp{b}{t}{s}$[ORD({b})>1].. {gr} - {g}{t}({e},{b}-1) =l= 
                  {r};\n'''.format(b=createHourSubsetName(nB),t=techLbl(et),
                  s=setsText,gr=genPlusRes,e=et,r=rhs,g=genName)
   #Commitments
   if ceOps == 'UC':
      eqns += '\n'
      for nB in blockNamesChronoList:
         for et in eguSets:
            setsText = createSetsText([et,createHourSubsetName(nB)])
            excludeHour1 = '$[ORD({b})>1]'.format(b=createHourSubsetName(nB)) if et == 'tech' else ''
            initOnOff = 'pOnoroffinit{b}({et})$[ORD({b})=1] +'.format(b=createHourSubsetName(nB),et=et) if et == 'egu' else ''
            eqns += '''commitment{b}{t}{s}{c} .. vOnoroff{t}{s} =e= {i} vOnoroff{t}({e},{b}-1)
                        + vTurnon{t}{s} - vTurnoff{t}{s};\n'''.format(t=techLbl(et),s=setsText,c=excludeHour1,i=initOnOff,
                        e=et,b=createHourSubsetName(nB))
   return eqns

