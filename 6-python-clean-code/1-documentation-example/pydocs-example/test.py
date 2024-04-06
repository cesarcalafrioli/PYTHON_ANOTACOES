"""
Para gerar a documentação das funções abaixo, digite no prompt:
python -m pydoc -w test

Código feito seguindo o video tutorial: https://www.youtube.com/watch?v=qFBTVMJRTT0
"""

import random

def remove_num(text):
    """
    Params: text as string format
    Return: a text without numbers 1,2,3 in it
    """
    return ''.join(char for char in text if char not in ['1','2','3'])

def remove_punct(text):
    """
    Params: text as string format
    Return: a text without . ? !
    """
    return ''.join(char for char in text if char not in ['.','?', '!'])
