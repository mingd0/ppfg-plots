"""
Configuration file to hold user defined parameters
"""

""" File Paths """
BPWA_PATH = './data/bpwa/'
MEMORY_PATH = './data/memory/'
EVENTS_PATH = './data/events/'
OUTPUTS_PATH = './outputs/'

# Use None type if file does not exist
BPWA_FILENAME = '20210908_060000_ST00BP00.csv'
MEMORY_FILENAME = None
EVENTS_FILENAME = None
# No spaces or slashes allowed in output file
# Recommended format:WellName_DecimalHoleSize_Mem_RT_Data.html
OUTPUT_FILENAME = 'Isabela-3_12.25inHS_Mem_RT_Data.html'

""" Plotting Preferences """
TITLE = 'Isabela-3 12-1/4in Hole Section - RT/MEM Data'
ESD_MARKER_SIZE = 10

""" Mnemonics """

# BPWA
RT_MNEMONICS = {
  'time': 'TIME',
  'bit_depth': 'GS_DBTM',
  'block_position': 'GS_BPOS',
  'rpm': 'GS_RPM',
  'torque': 'GS_TQA',
  'hookload': 'GS_HKLDF',
  'spp': 'GS_SPPA',
  'whp': '9274', 
  'ecd_rt': 'ECD_RT',
  'esd_min': 'ESD_MIN',
  'esd_max': 'ESD_MAX',
  'esd_avg': 'ESD'
}

# Memory (LAS File)
MEM_MNEMONICS = {
  'time': 'time',
  'ecd': 'ECD'
}
