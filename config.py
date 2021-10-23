"""
Configuration file to hold user defined parameters
"""

""" File Paths """
BPWA_PATH = './data/bpwa/'
MEMORY_PATH = './data/memory/'
EVENTS_PATH = './data/events/'
OUTPUTS_PATH = './outputs/'

# Use None type if file does not exist
BPWA_FILENAME = '20210926_050000_ST00BP01.csv'
MEMORY_FILENAME = 'MC_562_I3_ST00BP01_Digital Data_26Sep-02Oct.las'
EVENTS_FILENAME = None
# No spaces or slashes allowed in output file
# Recommended format:WellName_DecimalHoleSize_Mem_RT_Data.html
OUTPUT_FILENAME = 'Isabela-3_12.25inBypassHS_Mem_RT_Data.html'

""" Plotting Preferences """
TITLE = 'Isabela-3 12-1/4in Bypass Hole Section - RT/MEM Data'
ESD_MARKER_SIZE = 10
MAX_PP_OH = 12.6 # Max pore pressure in open hole

""" Mnemonics """

# BPWA
RT_MNEMONICS = {
  'time': 'TIME',
  'bit_depth': 'GS_DBTM',
  'hole_depth': 'GS_DMEA', 
  'block_position': 'GS_BPOS',
  'hookload': 'GS_HKLDF',
  'rop': 'GS_INSROP', 
  'wob': 'GS_SWOBF', 
  'rpm': 'GS_RPM',
  'torque': 'GS_TDTRQ',
  'mfia': 'GS_TFLO', 
  'spp': 'GS_SPPA',
  'sbp': 'SK_SBP',
  'whp': '9274',
  'ecd_rt': 'ECD_RT',
  'esd_min': 'ESD_MIN',
  'esd_max': 'ESD_MAX',
  'esd_avg': 'ESD', 
  'gas': 'GS_TGOUT', 
  'mw_in': 'SK_P2DENSITY', 
  'mw_out': 'SK_FLDENSITY1', 
  'tva': 'GS_SUMACTTK', 
  'tt1': 'GS_TTV1', 
  'tt2': 'GS_TTV2', 
  'mwd_temp': 'ATMP_RT'
}

# Memory (LAS File)
MEM_MNEMONICS = {
  'time': 'TIME',
  'ecd_mem': 'ECD:1',
  'mwd_temp_mem': 'TEMP_DNI',
  # 'gamma_ray': 'GR_CAL'
}
