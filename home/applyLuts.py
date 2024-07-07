from PIL import Image, ImageFilter
import os

listofLuts = os.listdir('home/LUTS')

class ApplyLuts():
    listofpaths=[]
    def __init__(self, image):
        self.unfilteredimage = Image.open(image)

    #listofLuts = os.listdir('home/LUTS')
    def saveFilteredImage(self,path):
        lut_table = []
        luts_size=None
        
        with open('home/LUTS/'+path,'r') as cube:
            for line in cube:
                line=line.strip()
                if not line or line.startswith('#') or line.startswith('TITLE'):
                    continue
                if line.startswith('LUT_3D_SIZE'):
                    parts=line.split()
                    if len(parts)==2:
                        luts_size=int(parts[1])
                    else:
                        raise ValueError(" Luts Size is not defined properly")
                elif luts_size is not None:
                    lut_table.append((line))
            row2val = lambda row: tuple([float(val) for val in row])
            lutTable =[row2val(row.split(" ")) for row in lut_table]
            filter = ImageFilter.Color3DLUT(luts_size,lutTable)
            filtetredImage = self.unfilteredimage.filter(filter)
            filtetredImage.save('media/output/'+path+'.jpeg')
            self.listofpaths.append('/media/output/'+path+'.jpeg')
        
    
    def ShowImages(self):
        
        for luts in listofLuts:
            self.saveFilteredImage(luts)
        
        return self.listofpaths