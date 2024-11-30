import tkinter as tk
from tkinter import font
import time
import random


# add check to make sure objective is completed
# add redo
# fix colors

# OLZ

states = ["Z", "L", "O", "ON"]
result = None
on = False 
ent_button = False
screen_value = 0
selected_value = 0
max_value = 1
preset_number = 5
sleep_time = 3000
text_offset = 25
selected_function = None
deletable_widgets = []
preset_string = "05"
preset_names = ["SNGRS02", "SNGRS03", "SNGRS04", "SNGRS05", "SNGRS06", "SNGRS07", "SNGRS08", "SNGRS09", "SNGRS10", "SNGRS11", "SNGRS12", "SNGRS13"]
preset_id = [430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441]
chosen_hopset = "0000"

chosen_crypto_mode = ""
chosen_opmode = ""
chosen_crypto_key = ""
chosen_power_level = ""
chosen_traffic_mode = ""
chosen_hopset_compartment = "0000"
chosen_sc_squelch_type = ""

chosen_copy_hopset_from = "0000"
chosen_copy_hopset_to = "0000"
chosen_hopset_id = "0000"
chosen_sincgars_gtod = "000000"
chosen_handset_profile = ""
chosen_radio_speaker = ""
chosen_member = False


temp_chosen_hopset = "0000"

temp_chosen_crypto_mode = ""
temp_chosen_opmode = ""
temp_chosen_crypto_key = ""
temp_chosen_power_level = ""
temp_chosen_traffic_mode = ""
temp_chosen_hopset_compartment = "0000"
temp_chosen_sc_squelch_type = ""
temp_chosen_sincgars_radio_type = ""
temp_chosen_copy_hopset_from = "0000"
temp_chosen_copy_hopset_to = "0000"
temp_chosen_hopset_id = "0000"
temp_chosen_sincgars_gtod = "0000"
temp_chosen_handset_profile = ""
temp_chosen_radio_speaker = ""
temp_chosen_member = False







chosen_waveform = ""
temp_chosen_waveform = ""

ct_override_enabled = False
temp_ct_override_enabled = False





def one_press():
  print("one")
  
def program_rt1():
  global selected_value
  global selected_function 
  selected_function = program_rt1

  delete_widgets()
    
  create_options(text = ["GENERAL CONFIG", "SYSTEM PRESETS", "SATURN CONFIG", "IW CONFIG", "VULOS CONFIG", "HAVEQUICKII CONFIG", "P25T CONFIG", "SINCGARS CONFIG", "ANW2C CONFIG"], title = "PGM:RT1", new_screen_value = 4)
  
def pgm_rt1_gen():
  global selected_value
  global selected_function 
  selected_function = pgm_rt1_gen

  delete_widgets()
    
  create_options(text = ["CT OVERRIDE CONFIG", "EXTERNAL DEVICE", "MIXER BYPASS CONFIG"], title = "PGM:RT1:GENERAL", new_screen_value = 5)
  
def options_scroll(text, title, new_screen_value):
    global max_value
    global screen_value
    screen.itemconfig(screen_text, text = title)
    
   
    max_value = len(text) - 1
    screen.coords(screen_text, screen_height/2, screen_width/4)
    
   
    
    for i in range(len(text)):
      coords = screen.coords(screen_text)
      if selected_value == i:
        
        widget = screen.create_text(coords[0], coords[1] + (text_offset), text = text[i], font = bold_font)
        deletable_widgets.append(widget)
        
     
        
      
      screen_value = new_screen_value
    widget1 = screen.create_text(coords[0], coords[1] + (text_offset * 2), text = "\u2191 \u2193 to scroll \ ENT TO EXIT", font = small_font)
    deletable_widgets.append(widget1)

def pgm_rt1_gen_ct():
    global selected_value
    global selected_function 
    global temp_ct_override_enabled
    selected_function = pgm_rt1_gen_ct

    delete_widgets()
    if selected_value == 0:
      temp_ct_override_enabled = True
    else: 
      temp_ct_override_enabled = False
    options_scroll(text = ["ENABLED", "DISABLED"], title = "CT OVERRIDE", new_screen_value = 6)
def ent_press():
  global screen_value
  global selected_value
  global preset_id
  
  
  global chosen_hopset
  global chosen_compartment 
  global chosen_crypto_mode 
  global chosen_opmode 
  global chosen_crypto_key
  global chosen_power_level 
  global chosen_traffic_mode 
  global chosen_hopset_compartment 
  global chosen_sc_squelch_type
  global chosen_sincgars_radio_type
  global chosen_copy_hopset_from 
  global chosen_copy_hopset_to
  global chosen_hopset_id 
  global chosen_sincgars_gtod 
  global chosen_handset_profile 
  global chosen_radio_speaker
  global chosen_member
  global chosen_waveform
  global ct_override_enabled


  global temp_chosen_hopset
  global temp_chosen_compartment
  global temp_chosen_crypto_mode 
  global temp_chosen_opmode
  global temp_chosen_crypto_key
  global temp_chosen_power_level
  global temp_chosen_traffic_mode 
  global temp_chosen_hopset_compartment
  global temp_chosen_sc_squelch_type
  global temp_chosen_sincgars_radio_type
  global temp_chosen_copy_hopset_from 
  global temp_chosen_copy_hopset_to
  global temp_chosen_hopset_id
  global temp_chosen_sincgars_gtod 
  global temp_chosen_handset_profile
  global temp_chosen_radio_speaker
  global temp_chosen_member
  global temp_chosen_waveform
  global temp_ct_override_enabled








  
  
  
  print(screen_value)
  
  if screen_value == 1:
    print("balls 2")
    open_screen()
  elif screen_value == 3 and selected_value == 1: #selected rt1 on program
    selected_value = 0
    program_rt1()
  elif screen_value == 4 and selected_value == 0: # # selecting general config in pgm:rt1
    selected_value = 0
    pgm_rt1_gen()
  elif screen_value == 5 and selected_value == 0: # selecting ct override config in pgm:rt1:genconfig
    selected_value = 0
    pgm_rt1_gen_ct()
  elif screen_value == 6: # selecting enabled for ct override
    # use marker to indicate correct thing done
    ct_override_enabled = temp_ct_override_enabled
    print("ct override")
    print(ct_override_enabled)

    selected_value = 0
    clr_press()
  elif screen_value == 4 and selected_value == 1: # selecting system presets in pgm:rt1
    selected_value = 0
    pgm_rt1_syspreset()
  elif screen_value == 7 and selected_value == 0: # selecting system preset config in pgm:rt1:sys presets
    selected_value = 0
    pgm_syspreset_config()
  elif screen_value == 8: # selected system preset number
    print("entering description")
    # save preset number!
    chosen_hopset = temp_chosen_hopset
    selected_value = 0
    preset_description()
  elif screen_value == 9: # confirmed description for preset number
    selected_value = 0
    chosen_waveform = temp_chosen_waveform
    preset_waveform()
  elif screen_value == 10: # go to opmode
    chosen_opmode = temp_chosen_opmode
    chosen_waveform = temp_chosen_waveform
    print("chosen waveform")
    print(chosen_waveform)
    selected_value = 0
    opmode()
  elif screen_value == 11: # go to preset name
    chosen_opmode = temp_chosen_opmode
    selected_value = 0
    preset_name()
  elif screen_value == 12: # go to crypto mode
    chosen_crypto_mode = temp_chosen_crypto_mode
    selected_value = 0
    crypto_mode()
  elif screen_value == 13: # go to crypto key
    chosen_crypto_key = temp_chosen_crypto_key
    chosen_crypto_mode = temp_chosen_crypto_mode
    selected_value = 0
    crypto_key()
  elif screen_value == 14: # go to tx power level
    chosen_power_level = temp_chosen_power_level
    chosen_crypto_key = temp_chosen_crypto_key
    selected_value = 0
    tx_power_level()
  elif screen_value == 15: # go to traffic mode
    chosen_traffic_mode = temp_chosen_traffic_mode
    chosen_power_level = temp_chosen_power_level
    print("power level")
    print(chosen_power_level)
    selected_value = 0
    traffic_mode()
  elif screen_value == 16: # go to hopset compartment
    chosen_hopset_compartment = temp_chosen_hopset_compartment
    chosen_traffic_mode = temp_chosen_traffic_mode
    selected_value = 0
    hopset_compartment()
  elif screen_value == 17: # go to sc frequency
    chosen_hopset_compartment = temp_chosen_hopset_compartment
    selected_value = 0
    sc_frequency()
  elif screen_value == 18: # go to sc squelch type
    chosen_sc_squelch_type = temp_chosen_sc_squelch_type
    selected_value = 0
    sc_squelch_type()
  elif screen_value == 19: # finished config for preset so go to pgm:rt1:syspreset: config
    chosen_sc_squelch_type = temp_chosen_sc_squelch_type
    selected_value = 0
    pgm_rt1_syspreset()
  elif screen_value == 4 and selected_value == 7: #selecting sincgars config in pgm:rt1
    selected_value = 0
    print("enter sincgars config")
    sincgars_config()
  elif screen_value == 20 and selected_value == 0: # selecting master/member in pgm:rt1:sincgars config
    
    selected_value = 0
    sincgars_radio_type()
  elif screen_value == 21: #selecting option in master/member in pgm:rt1:sincgars config:master/member
    selected_value = 0
    chosen_member = temp_chosen_member
    sincgars_config()
  elif screen_value == 20 and selected_value == 3: # selecting copy hopset in pgm:rt1:sincgars config
    selected_value = 0
    chosen_member = temp_chosen_member
    copy_hopset_from()
  elif screen_value == 22: # selecting a from value in copy hopset 
    chosen_copy_hopset_from = temp_chosen_copy_hopset_from[0:2]
    selected_value = 0
    copy_hopset_to()
  elif screen_value == 23: # selecting a to value in copy hopset
    chosen_copy_hopset_to = temp_chosen_copy_hopset_to[0:2] 
    chosen_copy_hopset_from = temp_chosen_copy_hopset_from[0:2]
    selected_value = 0
    new_hopset_id()
  elif screen_value == 24: # chose the hopset id now go back to pgm:rt1:sincgars config
    chosen_hopset_id = temp_chosen_hopset_id
    chosen_copy_hopset_to = temp_chosen_copy_hopset_to[0:2] 
    
    id = int(chosen_hopset_id[1:])
    to = int(chosen_copy_hopset_to)
    preset_id[to - 1] = id
    print("check here")
    print(id)
    print(to)
    selected_value = 0
    sincgars_config()
  elif screen_value == 25 and selected_value == 1: # chose rt1 in opt
    selected_value = 0
    rt1_options()
  elif screen_value == 26 and selected_value == 3: # chose sincgars in opt:rt1
    selected_value = 0
    opt_sincgars()
  elif screen_value == 27 and selected_value == 1: # chose sincgars gtod in opt:rt1:sincgars
    selected_value = 0
    sincgars_gtod()
  elif screen_value == 28 and selected_value == 0: # chose user entry in opt:rt1:sincgars options:sincgars gtod
    selected_value = 0
    global_time_of_day()
  elif screen_value == 29: # confirmed time in gtod
    chosen_sincgars_gtod = temp_chosen_sincgars_gtod
    selected_value = 0
    sincgars_gtod()
  elif screen_value == 25 and selected_value == 0: # chose system in opt
    selected_value = 0
    option_system()
  elif screen_value == 30 and selected_value == 0: # chose audio options in opt:system
    selected_value = 0
    audio_options()
  elif screen_value == 31 and selected_value == 0: # chose handset profile in opt:system:audio options
    selected_value = 0
    handset_profile()
  elif screen_value == 31 and selected_value == 1: # chose radio speaker in opt:system: audio options
    selected_value = 0
    radio_speaker()
  elif screen_value == 32: # selected the handset profile
    chosen_handset_profile = temp_chosen_handset_profile
    selected_value = 0
    audio_options()
  elif screen_value == 33: #selected radio speaker
    chosen_radio_speaker = temp_chosen_radio_speaker
    selected_value = 0
    audio_options()
    
    
    
    
def preset_description():
   global selected_value
   global selected_function 
   selected_function = preset_description

   delete_widgets()
   create_options(text = ["DEFAULT"], title = "PRESET DESCRIPTION", new_screen_value = 9)
   
    
def preset_waveform():
   global selected_value
   global selected_function 
   global temp_chosen_waveform
   selected_function = preset_waveform

   delete_widgets()
   
   if selected_value == 0:
     temp_chosen_waveform = "SINCGARS"
   else: 
     temp_chosen_waveform = ""
     
   options_scroll(text = ["SINCGARS", "NONE"], title = "PRESET WAVEFORM", new_screen_value = 10)
   
def opmode():
   global selected_value
   global selected_function 
   global temp_chosen_opmode
   selected_function = opmode

   delete_widgets()
   
   if selected_value == 0: 
     temp_chosen_opmode = "FREQUENCY HOPPING"
   else: 
     temp_chosen_opmode = ""
   options_scroll(text = ["FREQUENCY HOPPING", "NONE"], title = "PRESET OPMODE", new_screen_value = 11)
   
def preset_name():
   global selected_value
   global selected_function 
   
   selected_function = preset_name

   delete_widgets()
   create_options(text = ["SNGRS02"], title = "PRESET NAME", new_screen_value = 12)

def crypto_mode():
   global selected_value
   global selected_function 
   global temp_chosen_crypto_mode
   selected_function = crypto_mode

   delete_widgets()
   if selected_value == 0:  
     temp_chosen_crypto_mode = "VINSON"
   else: 
     temp_chosen_crypto_mode = ""
   options_scroll(text = ["VINSON", "NONE"], title = "CRYPTO MODE", new_screen_value = 13)
   
def crypto_key():
   global selected_value
   global selected_function 
   global temp_chosen_crypto_key
   selected_function = crypto_key

   delete_widgets()
   if selected_value == 0:  
     temp_chosen_crypto_key = "TEK01"
   else: 
     temp_chosen_crypto_key = ""
   
   options_scroll(text = ["TEK01", "NONE"], title = "CRYPTO KEY", new_screen_value = 14)
   
def tx_power_level():
   global selected_value
   global selected_function 
   global temp_chosen_power_level
   selected_function = tx_power_level
   values = ["LOW", "MEDIUM", "HIGH", "USER"]
   
   temp_chosen_power_level = values[selected_value]

   delete_widgets()
   options_scroll(text = values, title = "TX POWER LEVEL", new_screen_value = 15)
   
def traffic_mode():
   global selected_value
   global selected_function 
   global temp_chosen_traffic_mode
   selected_function = traffic_mode

   delete_widgets()
   
   if selected_value == 0:
     temp_chosen_traffic_mode = "VOICE"
   else: 
     temp_chosen_traffic_mode = ""
   options_scroll(text = ["VOICE", "NONE"], title = "TRAFFIC MODE", new_screen_value = 16)
   
def hopset_compartment():
   global selected_value
   global selected_function 
   global temp_chosen_hopset_compartment
   selected_function = hopset_compartment
   
   options = []
   for i in range(12):
      if i < 10: 
        options.append("0" + str(i + 1) + " [F" + str(preset_id[i]) + "]")
      else: 
        options.append(str(i + 1) + " [F" + str(preset_id[i]) + "]")

   delete_widgets()
   temp_chosen_hopset_compartment = options[selected_value]
   options_scroll(text = options, title = "HOPSET COMPARTMENT", new_screen_value = 17)
   
def sc_frequency():
   global selected_value
   global selected_function 
   
   selected_function = sc_frequency
   
   options = []
   for i in range(30,81):
        options.append(str(i) + ".0000 MHZ")


   delete_widgets()
   options_scroll(text = options, title = "SC FREQUENCY", new_screen_value = 18)
   
def sc_squelch_type():
   global selected_value
   global selected_function 
   global temp_chosen_sc_squelch_type
   selected_function = sc_squelch_type
   
   if selected_value == 0:
     temp_chosen_sc_squelch_type = "TONE"
   else: 
     temp_chosen_sc_squelch_type = ""

   delete_widgets()
   options_scroll(text = ["TONE", "NONE"], title = "SC SQUELCH TYPE", new_screen_value = 19)
      
def pgm_syspreset_config():
   global selected_value
   global selected_function 
   global temp_chosen_hopset
   selected_function = pgm_syspreset_config
   options = ["01", "12", "11", "10", "09", "08", "07", "06", "05", "04", "03", "02"]
   temp_chosen_hopset = options[selected_value]
   delete_widgets()
   options_scroll(text = ["01", "12", "11", "10", "09", "08", "07", "06", "05", "04", "03", "02"], title = "SYSTEM PRESET NUMBER", new_screen_value = 8)
   
def sincgars_config():
    global selected_value
    global selected_function 
    selected_function = sincgars_config

    delete_widgets()
    create_options(text = ["MASTER/MEMBER", "CUE CONFIGURATION", "HOPSET/LOCKOUT", "COPY HOPSET", "VIEW HOPSET", "VIEW LOCKOUTS"], title = "PGM-SINCGARS", new_screen_value = 20)
  

def sincgars_radio_type():
   global selected_value
   global selected_function 
   global temp_chosen_member
   selected_function = sincgars_radio_type
   if selected_value == 0:
    temp_chosen_member = True
   else: 
     temp_chosen_member = False
   delete_widgets()
   options_scroll(text = ["MEMBER", "MASTER"], title = "SINCGARS RADIO TYPE", new_screen_value = 21)
   
def copy_hopset_from():
   global selected_value
   global selected_function 
   global temp_chosen_copy_hopset_from
   selected_function = copy_hopset_from

   options = []
   for i in range(12):
      if i < 10: 
        options.append("0" + str(i + 1) + " [F" + str(preset_id[i]) + "]")
      else: 
        options.append(str(i + 1) + " [F" + str(preset_id[i]) + "]")
   delete_widgets()
   
   temp_chosen_copy_hopset_from = options[selected_value]
   options_scroll(text = options, title = "COPY HOPSET FROM", new_screen_value = 22)

def copy_hopset_to():
   global selected_value
   global selected_function 
   global temp_chosen_copy_hopset_to
   selected_function = copy_hopset_to
   
   options = []
   for i in range(12):
      if i < 10: 
        options.append("0" + str(i + 1) + " [F" + str(preset_id[i]) + "]")
      else: 
        options.append(str(i + 1) + " [F" + str(preset_id[i]) + "]")
   temp_chosen_copy_hopset_to = options[selected_value]
   delete_widgets()
   options_scroll(text = options, title = "COPY HOPSET TO", new_screen_value = 23)

def new_hopset_id():
   global selected_value
   global selected_function 
   global temp_chosen_hopset_id
   selected_function = new_hopset_id
   
   options = []
   for i in range(450,461):
        options.append("F" + str(i))

   temp_chosen_hopset_id = options[selected_value]
   delete_widgets()
   options_scroll(text = options, title = "NEW HOPSET ID", new_screen_value = 24)
   
def exit_program():
  global screen_value
  delete_widgets()
  
  screen.itemconfig(screen_text, text = "EXITING\nPROGRAM MODE")
  timer = m.after(sleep_time, open_screen)
  

  
def option_menu():
    global selected_value
    global selected_function 
    selected_function = option_menu

    delete_widgets()
    create_options(text = ["SYSTEM", "RT1", "RT2"], title = "OPTION MENU", new_screen_value = 25)

def rt1_options():
    global selected_value
    global selected_function 
    selected_function = rt1_options

    delete_widgets()
    create_options(text = ["MIXER BYPASS CONFIG", "OTAM", "SA OPTIONS", "SINCGARS OPTIONS", "TEST OPTIONS", "TX POWER CONFIG"], title = "OPT:RT1", new_screen_value = 26)
  
def opt_sincgars():
    global selected_value
    global selected_function 
    selected_function = opt_sincgars

    delete_widgets()
    create_options(text = ["COMSEC", "SINCGARS GTOD", "MASTER/MEMBER"], title = "OPT:RT1", new_screen_value = 27)
  
def sincgars_gtod():
    global selected_value
    global selected_function 
    selected_function = sincgars_gtod

    delete_widgets()
    create_options(text = ["USER ENTRY", "GPS SYNCHRONIZATION"], title = "OPT:RT1", new_screen_value = 28)
    
def global_time_of_day():
    global selected_value
    global selected_function 
    global temp_chosen_sincgars_gtod
    selected_function = global_time_of_day

    delete_widgets()
    
    options = []
    for i in range(100):
      if i < 10: 
        options.append("01D 20:00:0" + str(i))
      else: 
        options.append("01d 20:00:" + str(i))
    temp_chosen_sincgars_gtod = options[i]
    options_scroll(text = options, title = "GLOBAL TIME OF DAY", new_screen_value = 29)
  
   
def option_system():
    global selected_value
    global selected_function 
    selected_function = option_system

    delete_widgets()
    create_options(text = ["AUDIO OPTIONS", "GPS OPTIONS", "LOCK"], title = "OPT:SYS", new_screen_value = 30)
    
def audio_options():
    global selected_value
    global selected_function 
    selected_function = audio_options

    delete_widgets()
    create_options(text = ["HANDSET PROFILE", "RADIO SPEAKER", "RADIO SIDE PTT"], title = "OPT:SYS", new_screen_value = 31)
  
def handset_profile():
    global selected_value
    global selected_function 
    global temp_chosen_handset_profile
    selected_function = handset_profile
    
    options = ["NONE", "CASL", "PELTOR", "H-250", "LEGACY LAPEL MIC", "2 CHANNEL LAPEL MIC"]
    
    temp_chosen_handset_profile = options[selected_value]

    delete_widgets()
    options_scroll(text = options, title = "HANDSET PROFILE", new_screen_value = 32)

def radio_speaker():
    global selected_value
    global selected_function 
    global temp_chosen_radio_speaker
    selected_function = radio_speaker

    if selected_value == 1:
      temp_chosen_radio_speaker = "ENABLED"
    else: 
      temp_chosen_radio_speaker = "DISABLED"
    delete_widgets()
    options_scroll(text = ["DISABLED", "ENABLED"], title = "RADIO SPEAKER", new_screen_value = 33)


def open_screen():
      global screen_value
      global preset_string
      delete_widgets()
      screen.itemconfig(screen_text, text = preset_string + "-" + preset_names[preset_number - 1] + "\nVOC ----     " + str(preset_id[preset_number - 1]) + "  TEK01\n TRF DATA  NETID KEY")
      screen_value = 2
  
def clr_press():
  global screen_value
  global selected_value
  
  if screen_value == 1:
      open_screen()
  elif screen_value == 4: # go back to program screen
    screen_value -= 1
    in_program()  
  elif screen_value == 3: # exit program screen to main menu
    screen_value = 1
    exit_program()
    
    
  elif screen_value == 5: # go back to rt1
    screen_value -= 1
    program_rt1()
  elif screen_value == 6: # go back to general
    screen_value -= 1
    pgm_rt1_gen()
 
  elif screen_value == 7: # go back to rt1
    screen_value = 4
    program_rt1()
  elif screen_value == 8: # go back to pgm: sys presets
    screen_value = 7
    pgm_rt1_syspreset()
  elif screen_value == 9: ## go back to selecting preset number 
    screen_value = 8
    pgm_syspreset_config()
  elif screen_value == 10: # go back to preset description
    screen_value = 9
    preset_description()
  elif screen_value == 11: # go back to preset waveform
    screen_value = 10
    preset_waveform()
  elif screen_value == 12: # go back to opmode
    screen_value = 11
    opmode()
  elif screen_value == 13: # go back to preset name
    screen_value -= 1
    preset_name()
  elif screen_value == 14: # back to crypto mode
    screen_value -= 1
    crypto_mode()
  elif screen_value == 15: #  back to crypto key
    screen_value -= 1
    crypto_key()
  elif screen_value == 16: # back to tx power level
    screen_value -= 1
    tx_power_level()
  elif screen_value == 17: # traffic mode
    screen_value -= 1
    traffic_mode()
  elif screen_value == 18: # hopset compartment
    screen_value -= 1
    hopset_compartment()
  elif screen_value == 19: # back to sc frequency
    screen_value -= 1
    sc_frequency()
  elif screen_value == 20: # back to pgm: rt1 from sincgars
    screen_value = 4
    program_rt1()
  elif screen_value == 21: # back to pgm: rt1: sincgars from master/member
    screen_value = 20
    sincgars_config()
  elif screen_value == 22: # back to pgm rt1 sincgars from hopset compartment copy
    screen_value = 20
    sincgars_config()
  elif screen_value == 23: # back to copy from in pgm:rt1:sincgars:copy
    screen_value = 22
    copy_hopset_from()
  elif screen_value == 24: # back to copy to in pgm:rt1:sincgars:copy
    screen_value = 23
    copy_hopset_to()
  elif screen_value == 25: # back to open screen from opt
    screen_value = 2
    open_screen()
  elif screen_value == 26: # back to options from rt1
    screen_value = 25
    option_menu()
  elif screen_value == 27: # back to opt:rt1 from sincgars options
    screen_value = 26
    rt1_options()
  elif screen_value == 28: # back to opt:rt1: sincgars options from sincgars gtod
    screen_value = 27
    opt_sincgars()
  elif screen_value == 29: # back to opt:rt1:sincgars options:sincgars gtod from user entry
    screen_value = 28
    sincgars_gtod()
  elif screen_value == 30: # go back to opt from system options
    screen_value = 25
    option_menu()
  elif screen_value == 31: # go back to system options
    screen_value = 30
    option_system()
  elif screen_value == 32: # go back to audio options from handset profile
    screen_value = 31
    audio_options()
  elif screen_value == 33: # go back to audio options from radio speaker
    screen_value = 31
    audio_options
  
  
  
  selected_value = 0
  
  


def pgm_rt1_syspreset() :
    global selected_value
    global selected_function 
    selected_function = pgm_rt1_syspreset

    delete_widgets()
    create_options(text = ["SYSTEM PRESET CONFIG", "RESET SYSTEM PRESET", "SYSTEM SCAN CONFIG"], title = "PGM-SYS PRESETS", new_screen_value = 7)
    
def delete_widgets():
  global deletable_widgets
  for i in range(len(deletable_widgets)):
    screen.delete(deletable_widgets[i])
def up():
  global selected_value
  global selected_function
  global deletable_widgets
  global max_value
  if selected_function != None:
    if selected_value > 0:
      selected_value -= 1
    else:
      selected_value = max_value
    delete_widgets()
    selected_function()
    
def down():
  global selected_value
  global selected_function
  global deletable_widgets
  global max_value

  if selected_function != None:
    if selected_value < max_value:
      selected_value += 1
    else:
      selected_value = 0
    delete_widgets()
    selected_function()
    
def create_options(text, title, new_screen_value):
    global screen_value
    global selected_function
    global deletable_widgets
    global max_value
    global selected_value
    
    screen.itemconfig(screen_text, text = title)
    
   
    max_value = len(text) - 1
    screen.coords(screen_text, screen_height/2, screen_width/4)
    
    offset = 0
    # use offset if greater than 3
    if len(text) > 3 :
      offset = int(selected_value / 3)
      offset *= 3
       
    count = 0
    
    for i in range(len(text)):
      
      coords = screen.coords(screen_text)
      if selected_value == i:
        
        widget = screen.create_text(coords[0], coords[1] + (text_offset * (count + 1)), text = text[i], font = bold_font)
        deletable_widgets.append(widget)
        count += 1
        
      else:
        if i >= offset and i < offset + 3:
          widget = screen.create_text(coords[0], coords[1] + (text_offset * (count + 1)), text = text[i])
          deletable_widgets.append(widget)
          count += 1
     
      screen_value = new_screen_value
  
    
def in_program():
   global selected_function
   selected_function = in_program
   delete_widgets()
   create_options(text = ["SYSTEM", "RT1", "RT2"], title = "PROGRAM MODE", new_screen_value = 3)
  
    
def program_press():
  global screen_value
  delete_widgets()
  if screen_value == 2:
     screen.itemconfig(screen_text, text = "ENTERING\nPROGRAM MODE")
     timer = m.after(sleep_time, in_program )
     
    
    

    
  
  
  
  
def powered_on():
   global screen_value
   screen.itemconfig(screen_text, text = "WARNING: NO GPS\nCVs LOADED\nPRESS CLR/ENT TO EXIT")
   screen_value = 1
   
  
     
    
def update_preset(value):
  global preset_number
  global preset_names
  global sleep_time
  global preset_string
  if on:
    screen.itemconfig(screen_text, text = "CHANGING PRESET\n" + value + " - " + preset_names[int(value) - 1])
    timer = m.after(sleep_time,open_screen )
    preset_number = int(value) 
    if preset_number < 10 :
      preset_string = "0" + str(preset_number)
    else: 
      preset_string = str(preset_number)
  
  
  
   

def update_state(value):
  global on
  state.config(text=states[int(value)])
  
  if states[int(value)] == "ON":
    on = True
    screen.itemconfig(screen_text, text = "POWERING ON...", justify = 'center')
    timer = m.after(sleep_time, powered_on )
  
screen_height = 200
screen_width = 200
  

m = tk.Tk()
m.geometry("800x400")
m.configure(background = '#2b9c5d')
m.title("PRC-163")
bold_font = font.Font(weight = "bold")
small_font = font.Font(size = 12)

scale = tk.Scale(m, from_= 0, to=3, command = update_state, showvalue = 0, orient = tk.HORIZONTAL, background = "#2b9c5d")
scale.set(2)
scale.grid(row = 0, column = 0)
state = tk.Label(m, text = states[0], highlightbackground = "#2b9c5d", background = "#2b9c5d")
state.grid(row = 1, column = 0)

# preset scale
presets = tk.Scale(m, from_ = 1, to=12, command = update_preset, orient = tk.HORIZONTAL, background = "#2b9c5d" )
presets.set(5)
presets.grid(row = 0, column = 3 )
preset_label = tk.Label(m, text = "PRESET #", highlightbackground = "#2b9c5d", background = "#2b9c5d")
preset_label.grid(row = 1, column = 3)


screen = tk.Canvas(m, height = screen_height, width = screen_width, background = '#0de66c'  )
screen.grid(row = 2, column = 0, columnspan = 4)


random_preset = random.randint(1,12)
random_id = random.randint(450, 460)
random_gtod = random.randint(0,20)
random_mic = random.randint(0,1)
mic_text = ""
if random_mic == 0:
  mic_text = "\nand NO lapel mic"
else:
  mic_text = "\nand w/ 2 channel lapel mic"
objective_text =  "Objective:\n Program Preset " + str(random_preset) + " \nw/ GTOD 01D 20:00:" + str(random_gtod) + "\nand net id of " + str(random_id) + mic_text
objective = tk.Label(m, text =objective_text, highlightbackground = "#2b9c5d", background = "#2b9c5d")

objective.grid(row = 2, column = 4)


def checker():
  global chosen_hopset
 
  global chosen_crypto_mode 
  global chosen_opmode 
  global chosen_crypto_key
  global chosen_power_level 
  global chosen_traffic_mode 
  global chosen_hopset_compartment 
  global chosen_sc_squelch_type

  global chosen_copy_hopset_from 
  global chosen_copy_hopset_to
  global chosen_hopset_id 
  global chosen_sincgars_gtod 
  global chosen_handset_profile 
  global chosen_radio_speaker
  global chosen_member
  global chosen_waveform
  global ct_override_enabled
  global preset_number
  global preset_id
  global random_preset
  global random_id
  global random_gtod
  global random_mic
  global result
  

  output_text = ""
  
  if random_mic == 1:
    if int(chosen_hopset) == 1 and int(chosen_hopset_compartment[0:2]) == 1 and chosen_waveform == "SINCGARS" and chosen_opmode == "FREQUENCY HOPPING" and chosen_crypto_mode == "VINSON" and chosen_crypto_key == "TEK01" and chosen_power_level == "HIGH" and chosen_traffic_mode == "VOICE" and chosen_sc_squelch_type == "TONE" and chosen_member and ct_override_enabled and int(chosen_copy_hopset_from[0:2]) == 1 and int(chosen_copy_hopset_to[0:2]) == random_preset  and chosen_handset_profile == "2 CHANNEL LAPEL MIC" and chosen_radio_speaker == "DISABLED" and preset_id[random_preset - 1] == random_id and preset_number == random_preset:
      output_text = "SUCCESS!"
    else:
      if int(chosen_hopset) != 1:
        output_text += "wrong chosen hopset, should pick 01\n"
        print("wrong chosen hopset, should pick 01")
      if int(chosen_hopset_compartment[0:2]) != 1:
        output_text += "wrong chosen hopset compartment, should pick 01\n"
        print("wrong chosen hopset compartment, should pick 01")
      if chosen_waveform != "SINCGARS":
        output_text += "did not choose sincgars\n"
        print("did not choose sincgars")
      if chosen_opmode != "FREQUENCY HOPPING":
        output_text += "did not choose frequency hopping\n"
        print("did not choose frequency hopping")
      if chosen_crypto_mode != "VINSON":
        output_text += "did not choose vinson\n"
        print("did not choose vinson")
      if chosen_crypto_key != "TEK01":
        output_text += "did not choose tek01\n"
        print("did not choose tek01")
      if chosen_power_level != "HIGH":
        output_text += "not high power level\n"
        print("not high power level")
      if chosen_traffic_mode != "VOICE":
        output_text += "did not select voice\n"
        print("did not select voice")
      if chosen_sc_squelch_type != "TONE":
        output_text += "did not select tone\n"
        print("did not select tone")
      if not(chosen_member):
        output_text += "did not choose member\n"
        print("did not choose member")
      if not(ct_override_enabled):
        output_text += "ct override disabled\n"
        print("ct override disabled")
      if int(chosen_copy_hopset_from[0:2]) != 1:
        output_text += "did not copy from hopset 01\n"
        print("did not copy from hopset 01")
      if int(chosen_copy_hopset_to[0:2]) != random_preset:
        output_text += "did not copy to hopset " + str(random_id) + "\n"
        print("did not copy to hopset " + str(random_id))
      if chosen_handset_profile != "2 CHANNEL LAPEL MIC":
        output_text += "did not choose 2 channel lapel mic\n"
        print("did not choose 2 channel lapel mic")
      if chosen_radio_speaker != "DISABLED":
        output_text += "radio speaker enabled\n"
        print("radio speaker enabled") 
      if preset_id[random_preset - 1] != random_id:
        output_text += "preset " + str(random_preset) + " should have net id " + str(random_id) + "\n"
        print("preset " + str(random_preset) + " should have net id " + str(random_id))
      if preset_number != random_preset: 
        output_text += "prc should be on preset " + str(random_preset) + "\n"
        print("prc should be on preset " + str(random_preset))

  else:
     if int(chosen_hopset) == 1 and int(chosen_hopset_compartment[0:2]) == 1 and chosen_waveform == "SINCGARS" and chosen_opmode == "FREQUENCY HOPPING" and chosen_crypto_mode == "VINSON" and chosen_crypto_key == "TEK01" and chosen_power_level == "HIGH" and chosen_traffic_mode == "VOICE" and chosen_sc_squelch_type == "TONE" and chosen_member and ct_override_enabled and int(chosen_copy_hopset_from[0:2]) == 1 and int(chosen_copy_hopset_to[0:2]) == random_preset and chosen_handset_profile == "NONE" and chosen_radio_speaker == "ENABLED" and preset_id[random_preset - 1] == random_id and preset_number == random_preset:
      output_text = "SUCCESS!"
     else: 
      if int(chosen_hopset) != 1:
        output_text += "wrong chosen hopset, should pick 01\n"
        print("wrong chosen hopset, should pick 01")
      if int(chosen_hopset_compartment[0:2]) != 1:
        output_text += "wrong chosen hopset compartment, should pick 01\n"
        print("wrong chosen hopset compartment, should pick 01")
      if chosen_waveform != "SINCGARS":
        output_text += "did not choose sincgars\n"
        print("did not choose sincgars")
      if chosen_opmode != "FREQUENCY HOPPING":
        output_text += "did not choose frequency hopping\n"
        print("did not choose frequency hopping")
      if chosen_crypto_mode != "VINSON":
        output_text += "did not choose vinson\n"
        print("did not choose vinson")
      if chosen_crypto_key != "TEK01":
        output_text += "did not choose tek01\n"
        print("did not choose tek01")
      if chosen_power_level != "HIGH":
        output_text += "not high power level\n"
        print("not high power level")
      if chosen_traffic_mode != "VOICE":
        output_text += "did not select voice\n"
        print("did not select voice")
      if chosen_sc_squelch_type != "TONE":
        output_text += "did not select tone\n"
        print("did not select tone")
      if not(chosen_member):
        output_text += "did not choose member\n"
        print("did not choose member")
      if not(ct_override_enabled):
        output_text += "ct override disabled\n"
        print("ct override disabled")
      if int(chosen_copy_hopset_from[0:2]) != 1:
        output_text += "did not copy from hopset 01\n"
        print("did not copy from hopset 01")
      if int(chosen_copy_hopset_to[0:2]) != random_preset:
        output_text += "did not copy to hopset " + str(random_id) + "\n"
        print("did not copy to hopset " + str(random_id))
      if chosen_handset_profile != "NONE":
        output_text += "did not none for handset profile\n"
        print("did not none for handset profile")
      if chosen_radio_speaker != "DISABLED":
        output_text += "radio speaker disabled\n"
        print("radio speaker disabled") 
      if preset_id[random_preset - 1] != random_id:
        output_text += "preset " + str(random_preset) + " should have net id " + str(random_id) + "\n"
        print("preset " + str(random_preset) + " should have net id " + str(random_id))
      if preset_number != random_preset: 
        output_text += "prc should be on preset " + str(random_preset) + "\n"
        print("prc should be on preset " + str(random_preset))

  
  if output_text != "SUCCESS!":
    output_text_label = tk.Label(m, text = output_text, fg = "red", font = small_font , highlightbackground = "#2b9c5d", background = "#2b9c5d")
  else:
    output_text_label = tk.Label(m, text = output_text, font = bold_font, highlightbackground = "#2b9c5d" , background = "#2b9c5d")
  output_text_label.grid(row = 2, column = 5)
  result = output_text_label
  

def restarter():
  global screen_value
  global selected_value
  global preset_id
  
  
  global chosen_hopset
  global chosen_compartment 
  global chosen_crypto_mode 
  global chosen_opmode 
  global chosen_crypto_key
  global chosen_power_level 
  global chosen_traffic_mode 
  global chosen_hopset_compartment 
  global chosen_sc_squelch_type
  global chosen_sincgars_radio_type
  global chosen_copy_hopset_from 
  global chosen_copy_hopset_to
  global chosen_hopset_id 
  global chosen_sincgars_gtod 
  global chosen_handset_profile 
  global chosen_radio_speaker
  global chosen_member
  global chosen_waveform
  global ct_override_enabled


  global temp_chosen_hopset
  global temp_chosen_compartment
  global temp_chosen_crypto_mode 
  global temp_chosen_opmode
  global temp_chosen_crypto_key
  global temp_chosen_power_level
  global temp_chosen_traffic_mode 
  global temp_chosen_hopset_compartment
  global temp_chosen_sc_squelch_type
  global temp_chosen_sincgars_radio_type
  global temp_chosen_copy_hopset_from 
  global temp_chosen_copy_hopset_to
  global temp_chosen_hopset_id
  global temp_chosen_sincgars_gtod 
  global temp_chosen_handset_profile
  global temp_chosen_radio_speaker
  global temp_chosen_member
  global temp_chosen_waveform
  global temp_ct_override_enabled
  
  global on
  global ent_button
  global max_value
  global preset_number
  global selected_function
  global deletable_widgets
  global preset_string
  global preset_id
  global random_preset
  global random_id
  global random_gtod
  global random_mic
  global result
  delete_widgets()
  presets.set(5)
  scale.set(2)
  screen.itemconfig(screen_text, text = "OFF")
  on = False 
  ent_button = False
  screen_value = 0
  selected_value = 0
  max_value = 1
  preset_number = 5
  sleep_time = 1000
  text_offset = 25
  selected_function = None
  deletable_widgets = []
  preset_string = "05"
  preset_names = ["SNGRS02", "SNGRS03", "SNGRS04", "SNGRS05", "SNGRS06", "SNGRS07", "SNGRS08", "SNGRS09", "SNGRS10", "SNGRS11", "SNGRS12", "SNGRS13"]
  preset_id = [430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441]
  chosen_hopset = "0000"

  chosen_crypto_mode = ""
  chosen_opmode = ""
  chosen_crypto_key = ""
  chosen_power_level = ""
  chosen_traffic_mode = ""
  chosen_hopset_compartment = "0000"
  chosen_sc_squelch_type = ""

  chosen_copy_hopset_from = "0000"
  chosen_copy_hopset_to = "0000"
  chosen_hopset_id = "0000"
  chosen_sincgars_gtod = "000000"
  chosen_handset_profile = ""
  chosen_radio_speaker = ""
  chosen_member = False


  temp_chosen_hopset = "0000"

  temp_chosen_crypto_mode = ""
  temp_chosen_opmode = ""
  temp_chosen_crypto_key = ""
  temp_chosen_power_level = ""
  temp_chosen_traffic_mode = ""
  temp_chosen_hopset_compartment = "0000"
  temp_chosen_sc_squelch_type = ""
  temp_chosen_sincgars_radio_type = ""
  temp_chosen_copy_hopset_from = "0000"
  temp_chosen_copy_hopset_to = "0000"
  temp_chosen_hopset_id = "0000"
  temp_chosen_sincgars_gtod = "0000"
  temp_chosen_handset_profile = ""
  temp_chosen_radio_speaker = ""
  temp_chosen_member = False
  
  random_preset = random.randint(1,12)
  random_id = random.randint(450, 460)
  random_gtod = random.randint(0,20)
  random_mic = random.randint(0,1)
  mic_text = ""
  if random_mic == 0:
    mic_text = "\nand NO lapel mic"
  else:
    mic_text = "\nand w/ 2 channel lapel mic"
  objective_text =  "Objective:\n Program Preset " + str(random_preset) + " \nw/ GTOD 01D 20:00:" + str(random_gtod) + "\nand net id of " + str(random_id) + mic_text
  objective.config(text =objective_text)
  if result != None:
    result.destroy()
    result = None









chosen_waveform = ""
temp_chosen_waveform = ""

ct_override_enabled = False
temp_ct_override_enabled = False
  
  
finished = tk.Button(m, text = "FINISH", command = checker, highlightbackground = "#2b9c5d")
finished.grid(row = 3, column = 4)

restart = tk.Button(m, text = "RESTART", command = restarter, highlightbackground = "#2b9c5d")
restart.grid(row = 4, column=4)
screen_text = screen.create_text(screen_width/2,screen_height/2, text = "OFF")
buttons_start_row = 3

one = tk.Button(m, text = "1/CALL", command = one_press, highlightbackground = "#2b9c5d")
one.grid(row = buttons_start_row, column = 0)
two = tk.Button(m, text = "2/LT", highlightbackground = "#2b9c5d")
two.grid(row = buttons_start_row, column = 1)
three = tk.Button(m, text = "3/MODE", highlightbackground = "#2b9c5d")
three.grid(row = buttons_start_row, column = 2)
clear = tk.Button(m, text = "CLR", command = clr_press, highlightbackground = "#2b9c5d")
clear.grid(row = buttons_start_row, column = 3)
four = tk.Button(m, text = "4/SQL", highlightbackground = "#2b9c5d")
four.grid(row = buttons_start_row + 1, column = 0)
five = tk.Button(m, text = "5/ZERO", highlightbackground = "#2b9c5d")
five.grid(row = buttons_start_row + 1, column = 1)
six = tk.Button(m, text = "6/\u2191", command = up, highlightbackground = "#2b9c5d") # up arrow
six.grid(row = buttons_start_row + 1, column = 2)
ent = tk.Button(m, text = "ENT", command = ent_press, highlightbackground = "#2b9c5d")
ent.grid(row = buttons_start_row + 1, column = 3)
seven = tk.Button(m, text = "7/OPT", command = option_menu, highlightbackground = "#2b9c5d")
seven.grid(row = buttons_start_row + 2, column = 0)
eight = tk.Button(m, text = "8/PGM", command = program_press, highlightbackground = "#2b9c5d")
eight.grid(row = buttons_start_row + 2, column = 1)
nine = tk.Button(m, text = '9/\u2193', command = down, highlightbackground = "#2b9c5d") # down arrow
nine.grid(row = buttons_start_row + 2, column = 2)
pre_add = tk.Button(m, text = "Pre +", highlightbackground = "#2b9c5d")
pre_add.grid(row = buttons_start_row + 2, column = 3)
zero = tk.Button(m, text = "0/\u27f3", highlightbackground = "#2b9c5d")
zero.grid(row = buttons_start_row + 3, column = 0)
left = tk.Button (m, text = "\u2190", highlightbackground = "#2b9c5d")
left.grid(row = buttons_start_row + 3, column = 1)
right = tk.Button (m, text = "\u2192", highlightbackground = "#2b9c5d")
right.grid(row = buttons_start_row + 3, column = 2)
pre_minus = tk.Button(m, text = "Pre -", highlightbackground = "#2b9c5d")
pre_minus.grid(row = buttons_start_row + 3, column = 3)



  
    










m.mainloop()
