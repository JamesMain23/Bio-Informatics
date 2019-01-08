import os,glob,re
import numpy as np
import matplotlib.pyplot as plt
 

def main():  
    os.chdir(r"C:/Users/james/Downloads/jam23")
    # Cycle through all of the DNA files
    dna_Files_Processed = 0
    N50 =[]
    L50 =[]
    AvgL =[]
    for file_path in glob.glob(r"C:/Users/james/Downloads/jam23/*.fa"):
        print("Adding file " + file_path + " to array")
        baseDnaInfo = getDNAinfo(file_path)
        dna_Files_Processed += 1
        print("Amount of DNA files sorted: " + str(dna_Files_Processed))
        while True : 
            graph = input("Would you like to get Graphs of this data Y/N or Quit(Q) ?")
            if graph == "Y" or "y" :
                n50,avgL,l50 = exportGraph(baseDnaInfo)
                N50.append(n50)
                L50.append(l50)
                AvgL.append(avgL)
                break
            if graph == "N" or "n"  :  
                break
            if graph == "Q" or "q" :
                quit 
            else :
                print(graph, ' is not a valid response please try again')
    createGraphs(N50,AvgL,L50)
    print ('All Files in Folder complete')
    #exit()
def getDNAinfo(file_path):
    with open(file_path,'r') as myfile:
        contents = myfile.read()
    contigs = getContents(contents)
    genes = getGenes(contigs)
    dnaInfo = accurracy(contigs)
    filename_w_ext = os.path.basename(file_path)
    filename, file_extension= os.path.splitext(filename_w_ext)
    gFile = open(filename +'genes.txt', 'w+')
    print(genes, file = gFile)
    gFile.close
    dFile = open(filename + 'dnainfo.txt','w+')
    print(dnaInfo, file = dFile)
    dFile.close
    print("Saved")
    return dnaInfo

def getContents(contents):
   content_No_symbols_numbers = re.sub('[!@#$0123456789_>,\'"]','',contents)
   contigs = content_No_symbols_numbers.split("scaffold")
   contigs = [item.replace("scaffold",'') for item in contigs]
   return contigs 
def getGenes(contigs):
    x = 0
    genes = []
    introns =[]
    #startCodons = ["AUA","AUU","GUG","UUG","CUG","AUG"]
   # stopCodons = ["TAG","TAA","TGA"]
    #while x < len(contigs) :
     #   genes = contigs[contigs.index(startCodons) : contigs.index(stopCodons) + 1]
    #genes = [x for x in genes if x.length % 3 == 0]
    #introns = set([contigs]) - set([genes])
    return genes,introns

def accurracy(contigs):
    accurracy =[]
    error = errorReads(contigs)
    contigI = contigInfo(contigs)
    accurracy = error + contigI
    return accurracy

def errorReads(contigs):
    nsCount =''.join(contigs).count('N')
    if nsCount == 0:
        errors = 0
    elif nsCount > 0 :
        errors = (nsCount/sum(len(i)for i in contigs))*100
    errorPer = 'Percentage accuracy of error in the DNA : ' + str(errors) +' % ' + ' Amount of Ns present in sequence : ' + str(nsCount)
    return errorPer

def contigInfo(contigs): 
    lengths =[len(i) for i in contigs]
    avgSize = 0 if len(lengths) == 0 else (float(sum(lengths)) / len(lengths))
    noCon = len(contigs)
    n50 = contigs
    n50.sort(key = len)
    L50 = 0
    L50Num = 0
    half = (sum(len(i) for i in n50))/2
    lengths.sort(reverse = True)
    while L50 < half :
        cNum = lengths[L50Num]
        L50 = L50 + cNum
        L50Num = L50Num + 1
    L50Num + 1
    n50 = lengths[L50Num]
    gCount =''.join(contigs).count('G')
    cCount = ''.join(contigs).count('C')
    gcContent = ((gCount + cCount)/half*2)* 100 
    contigInfo = '  Average size : '+ str(avgSize) + '  Number of Contigs : ' + str(noCon) + ' N50 = ' + str(n50) + ' L50 = ' + str(L50Num) + ' Total length of contigs : ' + str(half *2) + 'GC Content of the contigs : ' + str(gcContent)  
    return contigInfo

def exportGraph(contigsInfo):
    figurs = re.findall(r"[-+]?\d*\.\d+|\d+", contigsInfo)
    n50 = []
    avgL = []
    L50 = []
    n50 = figurs[5]
    L50 = figurs[7]
    avgL= figurs[2]
    return n50,avgL,L50
    
    
def createGraphs(N50,avgL,L50):
   n= 6

   m1 = (0.10,0.12,0.10,0.11,0.14,0.10)
   m2=(0.21,0.21,0.20,0.22,0.20,0.21)
   m3=(0.29,0.27,0.28,0.24,0.23,0.23)
   m4=(0.41,0.39,0.35,0.37,0.41,0.40)
   x=[1,2,3,4,5,6]

   fig, ax = plt.subplots()

   index = np.arange(n)
   bar_width = 0.2
    
   opacity = 0.4
   error_config = {'ecolor': '0.3'}
   r1 = ax.bar(index, N50, bar_width,
                 alpha=opacity,
                 color='b',

                 error_kw=error_config)

   r2 = ax.bar(index + bar_width, m2, bar_width,
                 alpha=opacity,
                 color='r',

                 error_kw=error_config)

   r3 = ax.bar(index + bar_width+ bar_width, m3, bar_width,
                 alpha=opacity,
                 color='y',
                 error_kw=error_config)
   r4 = ax.bar(index + bar_width+ bar_width+ bar_width, m4, bar_width,
                 alpha=opacity,
                 color='c',
                 error_kw=error_config)                 
   plt.xlabel('D')
   plt.ylabel('Anz')
   plt.title('Th')

   f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')

   ax1.bar(x,m1, 0.2)
   ax2.bar(x,m2, 0.2)
   ax3.plot(x,m3)
   ax4.plot(x,m4)
    
   plt.tight_layout()
   plt.show()
 
main()
    