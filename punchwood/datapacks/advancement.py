'''
Contains Advancement class for storing and writing advancements, as well
as helpful Enumeraters for populating an advancement

Robert C Davis
November 29, 2023
(2023.11.29)
'''
from typing import Union
from enum import Enum


class Frame(Enum):
    '''
    Types of advancement frames.
    
    TASK -- most basic frame, square frame
    GOAL -- straight sides and rounded top and bottom
    CHALLENGE -- rarest frame, plays sound effects when completed, \
    looks like four curly brackets touch end to end
    '''

    TASK = 'task'
    GOAL = 'goal'
    CHALLENGE = 'challenge'


class Criterion:
    '''
    Used for handling criteria.

    name : str -- Unique Name of Criterion

    2023.11.29
    '''

    def __init__(
            self,
            name: str,
            trigger
        ) -> None:

        self.name = name
        self.trigger = trigger


class Advancement:
    '''
    Used for generating advancements.

    DISPLAY ATTRIBUTES:
    title : bool | float | str | dict | list -- name of advancement, \
    JSON text component supported (default: 'test advancement')
    icon : str -- item id to represent advancement (default: \
    'minecraft:oak_wood')
    frame : Frame -- advancement frame (default: Frame.TASK)
    self.background : str -- location of texture in resource pack \
    (default: None)
    description : bool | float | str | dict | list -- description of \
    advancement, JSON text component supported (default: 'test \
    description')
    show_toast : bool -- if True, will have an on-screen popup when \
    achieved (default: True)
    announce_to_chat : bool -- if True, will announce to chat when \
    advancement is achieved (default: True)
    hidden : bool -- if True, advancement and children will be hidden \
    until completed (default: False)

    PARENT ATTRIBUTE:
    parent : str |  -- specifies parent advancement, if None, then it \
    will be the root advancement (default: None)

    2023.11.27
    '''

    def __init__(
            self,

            # display
            title: Union[
                bool, float, str, dict, list
            ] = 'test advancement',
            icon: str = 'minecraft:oak_wood',
            frame: Frame = Frame.TASK,
            background: str = None,
            description: Union[
                bool, float, str, dict, list
            ] = 'test description',
            show_toast: bool = True,
            announce_to_chat: bool = True,
            hidden: bool = False,

            # parent
            parent: str = None
        ) -> None:

        # display
        # --------------------------------------------------------------
        # TODO: support JSON text component for title
        self.title = title
        # TODO: support SNBT strings for icon
        self.icon = icon
        self.frame = frame
        self.background = background
        # TODO: support JSON text component
        self.description = description
        self.show_toast = show_toast
        self.announce_to_chat = announce_to_chat
        self.hidden = hidden
        
        # parent
        self.parent = parent


    def json(self) -> dict:
        '''
        Generates json representation of advancement in dictionary form.

        2023.11.29
        '''

        data =  {
            'display': {
                'icon': {
                    'item': self.icon
                    # TODO: support SNBT
                    # 'nbt': SNBT (str)
                },
                'title': self.title,
                'frame': self.frame.value,
                'description': self.description,
                'show_toast': self.show_toast,
                'announce_to_chat': self.announce_to_chat,
                'hidden': self.hidden
            }
        }

        if self.background:
            data['display']['background'] = self.background
        if self.parent:
            data['parent'] = self.parent

        return data
