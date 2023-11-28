'''
Filter Class used for generating filters for the mcmeta file in
datapacks

Robert C Davis
November 27, 2023
(2023.11.27)
'''
from typing import Union


class Filter:
    '''
    Used for generating filters for the mcmeta file.

    2023.11.27
    '''

    def __init__(self, filters: Union[list, dict] = None) -> None:
        self.block = []
        
        if filters != None:
            ftype = type(filters)
            if ftype == list:
                self.block = filters
            elif ftype == dict:
                self.block.append(filters)
            else:
                raise TypeError('filters should be type list or dict')


    def get_filter(self) -> dict:
        '''
        Generates a dictionary populated with the filters, to be saved
        to 'filter' in mcmeta.

        2023.11.27
        '''

        return { 'block': self.block }
    

    def add_filter(self, path: str, namespace: str = None) -> None:
        '''
        Adds a filter. Path can use regular expressions.
        If there is no namespace, then it will apply to all loaded files
        named {path}. If there is no path specified, then it will apply
        to all files in {namespace}.

        2023.11.27
        '''

        newfilt = {}

        if path == None and namespace == None:
            raise ValueError('path and namespace cannot both be None')

        if path != None:
            newfilt['path'] = path
        if namespace != None:
            newfilt['namespace'] = namespace
        
        self.block.append(newfilt)
