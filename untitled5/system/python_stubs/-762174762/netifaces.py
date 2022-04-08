# encoding: utf-8
# module netifaces
# from C:\Python27\lib\site-packages\netifaces.pyd
# by generator 1.146
# no doc
# no imports

# Variables with simple values

AF_12844 = 25
AF_APPLETALK = 16
AF_ATM = 22
AF_BAN = 21
AF_CCITT = 10
AF_CHAOS = 5
AF_CLUSTER = 24
AF_DATAKIT = 9
AF_DECnet = 12
AF_DLI = 13
AF_ECMA = 8
AF_FIREFOX = 19
AF_HYLINK = 15
AF_IMPLINK = 3
AF_INET = 2
AF_INET6 = 23
AF_IPX = 6
AF_IRDA = 26
AF_ISO = 7
AF_LAT = 14
AF_LINK = -1000
AF_NETBIOS = 17
AF_NETDES = 28
AF_NS = 6
AF_PUP = 4
AF_SNA = 11
AF_UNIX = 1
AF_UNKNOWN1 = 20
AF_UNSPEC = 0
AF_VOICEVIEW = 18

version = '0.10.6'

# functions

def gateways(*args, **kwargs): # real signature unknown
    """
    Obtain a list of the gateways on this machine.
    
    Returns a dict whose keys are equal to the address family constants,
    e.g. netifaces.AF_INET, and whose values are a list of tuples of the
    format (<address>, <interface>, <is_default>).
    
    There is also a special entry with the key 'default', which you can use
    to quickly obtain the default gateway for a particular address family.
    
    There may in general be multiple gateways; different address
    families may have different gateway settings (e.g. AF_INET vs AF_INET6)
    and on some systems it's also possible to have interface-specific
    default gateways.
    """
    pass

def ifaddresses(*args, **kwargs): # real signature unknown
    """
    Obtain information about the specified network interface.
    
    Returns a dict whose keys are equal to the address family constants,
    e.g. netifaces.AF_INET, and whose values are a list of addresses in
    that family that are attached to the network interface.
    """
    pass

def interfaces(*args, **kwargs): # real signature unknown
    """ Obtain a list of the interfaces available on this machine. """
    pass

# no classes
# variables with complex values

address_families = {
    -1000: u'AF_LINK',
    0: u'AF_UNSPEC',
    1: u'AF_UNIX',
    2: u'AF_INET',
    3: u'AF_IMPLINK',
    4: u'AF_PUP',
    5: u'AF_CHAOS',
    6: u'AF_IPX',
    7: u'AF_ISO',
    8: u'AF_ECMA',
    9: u'AF_DATAKIT',
    10: u'AF_CCITT',
    11: u'AF_SNA',
    12: u'AF_DECnet',
    13: u'AF_DLI',
    14: u'AF_LAT',
    15: u'AF_HYLINK',
    16: u'AF_APPLETALK',
    17: u'AF_NETBIOS',
    18: u'AF_VOICEVIEW',
    19: u'AF_FIREFOX',
    20: u'AF_UNKNOWN1',
    21: u'AF_BAN',
    22: u'AF_ATM',
    23: u'AF_INET6',
    24: u'AF_CLUSTER',
    25: u'AF_12844',
    26: u'AF_IRDA',
    28: u'AF_NETDES',
}

