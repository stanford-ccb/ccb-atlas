#!/usr/env/python
# this script will read the _data/species/csv file and create new md files for each species that doesn't already exist

# base imports
import glob
import pandas as pd

# read the species data into memory
sp_list = pd.read_csv('../_data/species.csv')

# split the urls into genus and species
gn = list()
sp = list()
urls = sp_list['url'].tolist()
for url in urls:
    split = url.split('-')
    gn.append(split[0])
    sp.append(split[1])

# read the list of current md files and grab the species and genus names
mds = glob.glob('*.md')
mds.sort()
mdgn = list()
mdsp = list()
for md in mds:
    split = md[:-3].split('-')
    mdgn.append(split[-2])
    mdsp.append(split[-1])
    
# then reconstruct them here
psp = list()
for i in range(len(mdsp)):
    psp.append('-'.join([mdgn[i], mdsp[i]]))
    
# loop through the species list and create new pages for the species that do not have pages yet
for i in range(len(sp)):
    # concatenate the species name
    spname = '-'.join([gn[i], sp[i]]).lower()
    
    # create a new md page if it doesn't yet exist
    if spname not in psp:
        # capitalize the genus name
        caps = ' '.join([gn[i].capitalize(), sp[i]])
        #print(caps)
        # create the list of items to print in the new file
        lst = list()
        
        # add the front matter to the list
        lst.append('---')
        lst.append('layout: post')
        lst.append('author: maxwell')
        lst.append('title: {}'.format(caps))
        lst.append('description: ')
        lst.append('tags: []')
        lst.append('image: ')
        lst.append('  feature: ')
        lst.append('  credit: ')
        lst.append('  creditlink: ')
        lst.append('permalink: {}'.format(spname))
        lst.append('---')
        
        # join the list with newlines
        ost = '\n'.join(lst)
        
        # and write to the output file
        with open(spname + '.md', 'w') as f:
            f.write(ost)