#!/usr/bin/env python3

def return_evens(num_list):
    return [i for i in num_list if not i%2]

def make_exclamation(sentence_list):
    return [i + '!' for i in sentence_list]