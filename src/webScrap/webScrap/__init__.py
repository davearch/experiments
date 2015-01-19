"""
webScrap - Download images.

"""
__author__  = 'David Archuleta'
__version__ = '0.1.0'
__licence__ = 'BSD'

class treeflow:
    """TreeFlow specific constants."""
    BASE_URL = "http://www.treeflow.info"
    BAD      = ('#', '../')
    BASINS   = ('upco', 'loco', 'riogr',
                'ark', 'platte', 'upmo'
                'cali', 'pnw', 'grba',
                'midatl')
    DONT_WANT = ('http://treeflow.info/images/wwa_logo.jpg', 
                'http://treeflow.info/images/University-of-Colorado.jpg', 
                'http://treeflow.info/images/climas.png', 
                'http://treeflow.info/images/arizonalogo.gif')
