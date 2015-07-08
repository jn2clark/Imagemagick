# -*- coding: utf-8 -*-
"""
Created on Fri May  8 10:48:12 2015

some python wrapppers for imagemagick for cropping, appending, combining
requires imagemagick 
good for manipulating many images

@author: jesseclark
"""

import os
import glob


def imagemagick_crop(ddir=os.getcwd(), endswith='.png',width = [336,430], offset = [180,0],prefix = 'D' ):
    # crop files

    # use glob to get all files, ending in png
    listing = glob.glob(ddir+'/*'+endswith)

    nfiles = len(listing)

    count = 0.
    
    # now loop over files and create a string to crop
    for filename in listing:
    
        count += 1.       
        
        # get the path and filename
        split_names = os.path.split(filename)

        # create the save name
        save_name = split_names[0]+'/'+prefix+split_names[1]

        # make the system command
        cmd = 'convert '+filename+' -crop '+str(width[0])+'x'+str(width[1])+'+'+str(offset[0])+'+'+str(offset[1])+' '+save_name

        # execute the system copmmand
        os.system(cmd)
        
        #print(count/nfiles*100.0)
        print("{:.0f}".format(count/nfiles*100.0)+'%')

def imagemagick_annotate(ddir = os.getcwd(), endswith = '.jpg', prefix = 'test',save_prefix = 'A', an_text = 'iteration: ', text_size = 64, no_counter = False ):
    #annotate the images with text
    
    # use glob to get all files, ending in png
    listing = glob.glob(ddir+'/'+prefix+endswith)

    nfiles = len(listing)

    count = 0.
   
    print listing
    
    
   
    # now loop over files and create a string to annotate
    for filename in listing:
         
        count += 1.       
        
        # get the path and filename
        split_names = os.path.split(filename)

        # create the save name
        save_name = split_names[0]+'/'+save_prefix+split_names[1]

        # make the system comman  
        if no_counter:
            cmd='convert '+filename+' -font ''Arial'' -pointsize '+str(text_size)+' -gravity northwest -annotate +100+100 '+"'"+an_text+"'"+' '+save_name
        else:
            cmd='convert '+filename+' -font ''Arial'' -pointsize '+str(text_size)+' -gravity northwest -annotate +100+300 '+"'"+an_text+str(int(count))+"'"+' '+save_name
            
        # execute the system copmmand
        os.system(cmd)
        
        #print(count/nfiles*100.0)
        print("{:.0f}".format(count/nfiles*100.0)+'%')
        
        
def imagemagick_composite(ddir = os.getcwd(), endswith = '.png', prefixA = 'D' ,prefixB = 'E', prefixOut = 'C'):
    
    # sums two images
    # use glob to get all files, ending in png
    listingA = glob.glob(ddir+'/'+prefixA+'*'+endswith)

    # use glob to get all files, ending in png
    listingB = glob.glob(ddir+'/'+prefixB+'*'+endswith)

    # get number of images
    nfiles = len(listingA)

    # set a counter
    count = 0.
   
    # now loop over files and create a string to crop
    for filename in listingA:
    
        # get the path and filename
        split_names = os.path.split(filename)

        # create the save name
        save_name = split_names[0]+'/'+prefixOut+split_names[1]

        # make the system command
        cmd = 'convert -composite '+filename+' '+listingB[int(count)]+' '+save_name

        # execute the system copmmand
        os.system(cmd)
        
        count += 1.  

        #print(count/nfiles*100.0)
        print("{:.0f}".format(count/nfiles*100.0)+'%')

def imagemagick_append(ddir=os.getcwd(), endswith='.png', prefixA = 'D' ,prefixB = 'E', prefixOut = 'A'):
    # joins two images together (horizonatlly)
    
    # use glob to get all files, ending in png
    listingA = glob.glob(ddir+'/'+prefixA+'*'+endswith)

    # use glob to get all files, ending in png
    listingB = glob.glob(ddir+'/'+prefixB+'*'+endswith)

    # get number of images
    nfiles = len(listingA)

    # set a counter
    count = 0.
    
    # now loop over files and create a string to crop
    for filename in listingA:
    
        # get the path and filename
        split_names = os.path.split(filename)

        # create the save name
        save_name = ddir+'/'+prefixOut+split_names[1]

        # make the system command
        cmd = 'convert +append '+filename+' '+listingB[int(count)]+' '+save_name

        # execute the system copmmand
        os.system(cmd)
        #print cmd
        count += 1.  

        #print(count/nfiles*100.0)
        print("{:.0f}".format(count/nfiles*100.0)+'%')
        
if __name__ == "__main__":
    # testing
    #imagemagick_crop(width = [104,93],offset=[24,22],prefix='E')