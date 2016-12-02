#!/usr/bin/python
#
# glitchutils.py: part of simpleglitch.py, world's crappiest and slowest file
# format fuzzer used to generate image files that can hopefully be considered
# glitch art.
#
# by Julio Cesar Fort - julio@whatever.io

import os
import random
import string

global glitch_factor

class mutators:
    def __init__(self, seed):
        self.seed = seed
        random.seed(seed)

    def swap_bytes(self, left, right):
        new_left = right
        new_right = left
        return (new_left, new_right)
    
    def append_bytes(self, orig_bytes, n_bytes):
        return orig_bytes + self._not_random_string(n_bytes)
    
    def append_random_character(self, orig_bytes):
        return orig_bytes + self._random_character()
    
    def append_random_byte(self, orig_bytes):
        return orig_bytes + self._random_byte()
    
    def append_random_string(self, orig_bytes, n_bytes):
        return orig_bytes + self._random_string(n_bytes)
        
    def add_byte_random_location(self, orig_bytes):
        for i in xrange(len(orig_bytes)):
            orig_bytes[random.choice(range(len(orig_bytes)))] = self._random_byte()
        return orig_bytes
    
    def add_character_random_location(self, orig_bytes):
        for i in xrange(len(orig_bytes)):
            orig_bytes[random.choice(range(len(orig_bytes)))] = self._random_character()
        return orig_bytes  

    def add_string_random_location(self, orig_bytes):
        for i in xrange(len(orig_bytes)):
            return
    
    def delete_last_bytes(self, orig_bytes, n_bytes):
        for i in xrange(n_bytes):
            orig_bytes.pop()
        return orig_bytes
    
    def delete_random_bytes(self, orig_bytes, n_bytes):
        for i in xrange(n_bytes):
            orig_bytes.remove(orig_bytes[random.choice(range(len(orig_bytes)))])
        return orig_bytes

    # shuffler probably messes images up very very badly
    def shuffler(self, orig_bytes):
        return random.shuffle(orig_bytes)
    
    '''
    These are support functions that are not called directly.
    Used to generate fixed and random characters, bytes, strings.
    '''
    def _random_character(self):
        return list(random.choice(string.printable))
    
    def _random_byte(self):
        return list(os.urandom(1))
    
    def _random_string(self, n_bytes):
        ret_string = ""
        string_list = []
        
        if n_bytes > 0:
            for i in xrange(n_bytes):
                string_list.append(random.choice(string.printable))
        
        return string_list
    
    def _not_random_string(self, character, n_bytes):
        ret_string = ""
        
        if n_bytes > 0:
            for i in xrange(n_bytes):
                ret_string += character
        
        return list(ret_string)