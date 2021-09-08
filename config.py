"""
Configuration file to hold user defined parameters
"""

BPWA_FILENAME = '20210716_060000_ST00BP00_dm.csv'
MEMORY_DATA_FILENAME = 'MC_562_I3_ST00BP00_Digital Data_15JulAM-19JulAM.las'
EVENTS_FILENAME = 'events.csv'
TITLE = 'Isabela-3 18-1/8in x 21in Hole Section - RT/MEM Data'
ESD_MARKER_SIZE = 10

# No spaces or slashes permitted in output file.
# Recommended format:WellName_DecimalHoleSize_Mem_RT_Data.html
OUTPUT_FILENAME = 'Isabela-3_18.125x21HS_Mem_RT_Data.html'

RT_MNEMONICS = {
  'time': 'TIME',
  'bit_depth': 'GS_DBTM',
  'block_position': 'GS_BPOS',
  'hookload': 'GS_HKLDF',
  'spp': 'GS_SPPA',
  'ecd_rt': 'ECD_RT',
  'esd_min': 'ESD_MIN',
  'esd_max': 'ESD_MAX',
  'esd_avg': 'ESD'
}

MEM_MNEMONICS = {
  'time': 'time',
  'ecd': 'ECD'
}
