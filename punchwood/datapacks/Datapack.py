'''
Datapack Class used for generating datapacks for Minecraft (1.20)

Robert C Davis
November 27, 2023
(2023.11.27)
'''
import os
import json
from punchwood.datapacks.filter import Filter


class Datapack:
    '''
    Used for generating the datapack

    2023.11.27
    '''


    def __init__(
            self,
            name: str = 'test',
            description: str = 'test datapack',
            filter: Filter = None
        ) -> None:
        
        self.name = name
        self.desc = description
        self.filter = filter

    
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
        



        
        
