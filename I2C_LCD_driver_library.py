# -*- coding: utf-8 -*-
# Original code found at:
# https://gist.github.com/DenisFromHR/cc863375a6e19dce359d

"""
Compiled, mashed and generally mutilated 2014-2015 by Denis Pleic
Made available under GNU GENERAL PUBLIC LICENSE

# Modified Python I2C library for Raspberry Pi
# as found on http://www.recantha.co.uk/blog/?p=4849
# Joined existing 'i2c_lib.py' and 'lcddriver.py' into a single library
# added bits and pieces from various sources
# By DenisFromHR (Denis Pleic)
# 2015-02-10, ver 0.1

"""
#IMPORTATION OF NECESSARY LIBRARIES

import smbus # imports the System Management Bus (SMBus) module for I2C communication
from time import sleep # imports "sleep" function from "time" module to introduce delays in the program

# i2c bus (0 -- original Pi, 1 -- Rev 2 Pi)

I2CBUS = 1 # specifies the I2C bus to use. ON Newer models of raspberry pi, it is 1 but for older ones, it's 0

# LCD Address
ADDRESS = 0x27 # specifies the I2C address of the LCD display. 0x27 was the address for the Raspberry Pi 4b 



class i2c_device:

   # Initializes I2C device with its address and I2C bus port
   def __init__(self, addr, port=I2CBUS):
      self.addr = addr # stoses the I2C address of the device in the "addr" attribute
      self.bus = smbus.SMBus(port) # creates a SMBus object for communication using the specifies I2C bus port

# Write a single command
   def write_cmd(self, cmd):
      self.bus.write_byte(self.addr, cmd) # writes a single byte command to the device at the specifies I2C address
      sleep(0.0001) # waits briefly to allow the device to process the command

# Write a command and argument
   def write_cmd_arg(self, cmd, data):
      self.bus.write_byte_data(self.addr, cmd, data) # writes a byte of data - "data" to the register - "cmd" of the device
      sleep(0.0001) # waits briefly to allow the device to process the command

# Write a block of data
   def write_block_data(self, cmd, data):
      self.bus.write_block_data(self.addr, cmd, data) # writes a block of dara to the I2C device
      sleep(0.0001) # waits briefly to allow the device to process the command

# Read a single byte
   def read(self):
      return self.bus.read_byte(self.addr) # returns the byte of data read from the register 

# Read
   def read_data(self, cmd):
      return self.bus.read_byte_data(self.addr, cmd) # returns the byte of data read from the register of the I2C device

# Read a block of data
   def read_block_data(self, cmd):
      return self.bus.read_block_data(self.addr, cmd) # returns a block of data read from the register


# COMMANDS FOR LCD CONTROL
 
LCD_CLEARDISPLAY = 0x01 # clears the display screen
LCD_RETURNHOME = 0x02 # sets the curso to the home position
LCD_ENTRYMODESET = 0x04 # sets the entry mode for moving the  cursor/display
LCD_DISPLAYCONTROL = 0x08 # controls the display settings (ON/OGG, cursor, blink)
LCD_CURSORSHIFT = 0x10 # moves the cursor or shifts the display
LCD_FUNCTIONSET = 0x20 # sets the LCD function (e.g 4 bit or 8 bit mode)
LCD_SETCGRAMADDR = 0x40 # sets the address of the CGRAM (for custom characters)
LCD_SETDDRAMADDR = 0x80 # sets the address of the DDRAM (for standard cahracters)

# FLAGS FOR ENTRY MODE
 
LCD_ENTRYRIGHT = 0x00 # text moves from left to right
LCD_ENTRYLEFT = 0x02 # text moves from right to left
LCD_ENTRYSHIFTINCREMENT = 0x01 # shifts the display when a character is entered
LCD_ENTRYSHIFTDECREMENT = 0x00 # does not shift the display

# FLAGS FOR DISPLAY CONTROL

LCD_DISPLAYON = 0x04 # turns the display ON
LCD_DISPLAYOFF = 0x00 # turns the display OFF
LCD_CURSORON = 0x02 # displays the cursor
LCD_CURSOROFF = 0x00 # hides the cursor
LCD_BLINKON = 0x01 # makes the cursor blink
LCD_BLINKOFF = 0x00 # moves the cursor/display to the left

# FLAGS FOR CURSOR/DISPLAY SHIFT

LCD_DISPLAYMOVE = 0x08 # shifts the entire display
LCD_CURSORMOVE = 0x00 # moves only the cursor
LCD_MOVERIGHT = 0x04 # moves the cursor/display to the right
LCD_MOVELEFT = 0x00 # moves the cursor/display to the left

# FLAGS FOR FUNCTION SET

LCD_8BITMODE = 0x10 # enables 8-bit mode
LCD_4BITMODE = 0x00 # enables 4-bit mode
LCD_2LINE = 0x08 # enables a 2 -line display
LCD_1LINE = 0x00 # enables a 1-line display
LCD_5x10DOTS = 0x04 # enables 5x10 dot font
LCD_5x8DOTS = 0x00 # enables 5x8 dot font

# FLAGS FOR BACKLIGHT CONTROL

LCD_BACKLIGHT = 0x08 # enables the LCD backlight
LCD_NOBACKLIGHT = 0x00 # disables the LCD backlight

En = 0b00000100 # Enable bit (used t atch data to the LCD)
Rw = 0b00000010 # Read/Write bit (used to set read/write mode)
Rs = 0b00000001 # Register select bit (used to select data/command mode)

class lcd:
   #initializes objects and lcd
   def __init__(self):
      self.lcd_device = i2c_device(ADDRESS) # creates an I2C device object for communcication with the LCD.

      # INITIALIZATION SEQUENCE FOR THE LCD IN 4-bit MODE

      self.lcd_write(0x03)
      self.lcd_write(0x03)
      self.lcd_write(0x03)
      self.lcd_write(0x02)

      self.lcd_write(LCD_FUNCTIONSET | LCD_2LINE | LCD_5x8DOTS | LCD_4BITMODE) # sets 4-bit mode, 2-line display, and 5x8 dot font.
      self.lcd_write(LCD_DISPLAYCONTROL | LCD_DISPLAYON) # tunrs on display
      self.lcd_write(LCD_CLEARDISPLAY) # clears the display
      self.lcd_write(LCD_ENTRYMODESET | LCD_ENTRYLEFT) # sets textt to move from right to left
      sleep(0.2) # waits briefly to allow the device to process the command


 # CLOCKS EN TO LATCH COMMAND

   def lcd_strobe(self, data):
      self.lcd_device.write_cmd(data | En | LCD_BACKLIGHT) # sends the enable signal with backligh on.
      sleep(.0005) # waits briefly to allow the device to process the command
      self.lcd_device.write_cmd(((data & ~En) | LCD_BACKLIGHT)) # turns OFF the enable signal.
      sleep(.0001) # waits briefly to allow the device to process the command

   def lcd_write_four_bits(self, data):
      self.lcd_device.write_cmd(data | LCD_BACKLIGHT) # sends data with the backligh ON.
      self.lcd_strobe(data) # latches the data to the LCD.

   # write a command to lcd
   def lcd_write(self, cmd, mode=0):
      self.lcd_write_four_bits(mode | (cmd & 0xF0)) # sends the upper nibble (4 bits) of the command
      self.lcd_write_four_bits(mode | ((cmd << 4) & 0xF0)) # sends the lower nibble (4 bits) of the command.

   # write a character to lcd (or character rom) 0x09: backlight | RS=DR<
   # works!
   def lcd_write_char(self, charvalue, mode=1):
      self.lcd_write_four_bits(mode | (charvalue & 0xF0)) # sends the upper nibble (4 bits) of the character.
      self.lcd_write_four_bits(mode | ((charvalue << 4) & 0xF0)) # sends the lower nibble (4 bits) of the character.
  
   # put string function with optional char positioning
   def lcd_display_string(self, string, line=1, pos=0):
    if line == 1:
      pos_new = pos
    elif line == 2:
      pos_new = 0x40 + pos
    elif line == 3:
      pos_new = 0x14 + pos
    elif line == 4:
      pos_new = 0x54 + pos

    self.lcd_write(0x80 + pos_new) # sets the DDRAM address to the starting position.

    for char in string: # writes each character of the string to the LCD.
      self.lcd_write(ord(char), Rs)

   # clear lcd and resets the cursor to the hone position
   def lcd_clear(self):
      self.lcd_write(LCD_CLEARDISPLAY) # clears display
      self.lcd_write(LCD_RETURNHOME) # resets the cursor to the home position

   # define backlight on/off (lcd.backlight(1); off= lcd.backlight(0)
   def backlight(self, state): # for state, 1 = on, 0 = off
      if state == 1:
         self.lcd_device.write_cmd(LCD_BACKLIGHT) # turns backlight ON if state 1
      elif state == 0:
         self.lcd_device.write_cmd(LCD_NOBACKLIGHT) # turns backlight OFF if state is 0

   # add custom characters (0 - 7)
   def lcd_load_custom_chars(self, fontdata):
      self.lcd_write(0x40) # sets the CGRAM address to the start.
      for char in fontdata: # iterates through each custom character
         for line in char: # writes each line of the character pattern to CGRAM
            self.lcd_write_char(line) 