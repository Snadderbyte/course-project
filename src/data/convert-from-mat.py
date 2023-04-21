import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import os 

dir = '././data/raw/PLDM/test_gt/'
outDir = './data/interim/PLDM/labeled/'

# This function takes a .mat and converts it into a image file

def convert_data(indir = '', outdir = '', key = ''):
    for file in os.listdir(indir):
        if file != '.DS_Store':
            f_path = os.path.join(indir, file)
            mat = scipy.io.loadmat(f_path)
            arr = mat[key]
            arr = arr[0][0][0][0][0]
            # Since the data is represented in a matrix, 
            # we can check what the height by counting arrays 
            # and check the width by counting items in the first array
            height = len(arr)
            width = len(arr[0])
            print(f'Working on file: {file} it has pixel heigth of: {len(arr)} and width of {len(arr[0])}')
            if width < height:
                fig = plt.figure(frameon=False, dpi=100, figsize=(3.6, 5.4))
            else:
                fig = plt.figure(frameon=False, dpi=100, figsize=(5.4, 3.6))
            fig.figimage(arr, cmap='binary', xo=0, yo=0)
            plt.savefig(outdir + file.removesuffix('.mat') + '.jpg')

convert_data(dir, outDir, 'groundTruth')