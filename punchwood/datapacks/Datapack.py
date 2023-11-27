'''
Datapack Class used for generating datapacks for Minecraft (1.20)

Robert C Davis
November 27, 2023
(2023.11.27)
'''
import os
import json


class Datapack:
    def __init__(
            self,
            name: str = 'test',
            description: str = 'test datapack'
        ):
        self.name = name
        self.desc = description

    
    def generate(self):
        '''
        Generates the datapack. 

        2023.11.27
        '''


        # Creates Directory for Datapack
        # --------------------------------------------------------------
        subfolders = [f.path[2:] for f in os.scandir('.') if f.is_dir()]
        folder = self.name
        if self.name in subfolders:
            number = 1
            while f'{self.name}({number})' in subfolders:
                number += 1
            folder = f'{self.name}({number})'
        
        os.mkdir(folder)


        # Creates pack.mcmeta file
        # --------------------------------------------------------------
        mcmeta = {
            'pack': {
                'pack_format': 15,
                'description': self.desc
            }
        }

        # TODO: implement filters

        with open(f'{folder}/pack.mcmeta', 'w') as file:
            file.write(json.dumps(mcmeta, indent=4))

        
        # Creates data folder
        # --------------------------------------------------------------
        os.mkdir(f'{folder}/data')


        # Build Namespaces
        # --------------------------------------------------------------
        # TODO: any of this
        



        
        
