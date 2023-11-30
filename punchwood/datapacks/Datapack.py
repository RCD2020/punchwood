'''
Datapack Class used for generating datapacks for Minecraft (1.20)

Robert C Davis
November 27, 2023
(2023.11.27)
'''
import os
import shutil
import json

from punchwood.datapacks.filter import Filter


class Datapack:
    '''
    Used for generating the datapack.

    name : str -- name of datapack (default: 'test')
    thumbnail_path : str -- path of image for pack.png, must be a png \
    image and a square image (default: None)
    description : str -- description of datapack (default: 'test \
    datapack')
    filter : datapacks.Filter -- filters out files from other \
    datapacks (default: None)

    2023.11.27
    '''


    def __init__(
            self,
            name: str = 'test',
            thumbnail_path: str = None,
            description: str = 'test datapack',
            filter: Filter = None
        ) -> None:

        self.name = name
        # TODO: make class for raw json text format, can be used in desc
        self.desc = description
        self.filter = filter

        # check that thumbnail is a png image
        if thumbnail_path.split('.')[-1] != 'png':
            raise ValueError('thumbnail must be a png image')
        self.thumbnail = thumbnail_path

    
    def generate(self):
        '''
        Generates the datapack. 

        2023.11.27
        '''


        # Creates Directory for Datapack
        # --------------------------------------------------------------

        # reads names of folders
        subfolders = [f.path[2:] for f in os.scandir('.') if f.is_dir()]

        # get potential name of datapack directory
        folder = self.name

        # alter directory name to not match any existing directories
        if self.name in subfolders:
            number = 1
            while f'{self.name}({number})' in subfolders:
                number += 1
            folder = f'{self.name}({number})'
        
        # make datapack directory
        os.mkdir(folder)

        # copy pack.png into new directory
        shutil.copy(self.thumbnail, f'{folder}/pack.png')


        # Creates pack.mcmeta file
        # --------------------------------------------------------------
        # TODO: replace Filter class with mcmeta class

        # initialize mcmeta
        mcmeta = {
            'pack': {
                'pack_format': 15,
                'description': self.desc
            }
        }

        # add any filters
        if self.filter != None:
            mcmeta['filter'] = self.filter.get_filter()

        # write mcmeta
        with open(f'{folder}/pack.mcmeta', 'w') as file:
            file.write(json.dumps(mcmeta, indent=4))

        
        # Create data folder
        # --------------------------------------------------------------
        os.mkdir(f'{folder}/data')


        # Build Namespaces
        # --------------------------------------------------------------
        # TODO: any of this
