"""
stopword-remover - Remove stopwords from text

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import StopwordRemover, remove, process, main

__all__ = ["StopwordRemover", "remove", "process", "main"]
