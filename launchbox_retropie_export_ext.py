import glob
import io
import os
from PIL import Image
from shutil import copy
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Change the path to your launchbox folder.
lb_dir = r'X:\A3_Games\00_Resources\00_Launchbox\LaunchBox'

# Script output directory. (for Roms, images and xml files)
# Copy the gamelists to ~/.emulationstation/gamelists/
# Copy the roms and images to ~/RetroPie/roms/
output_dir = r'X:\output'

# Restrict export to only Launchbox favorites.
favorites_only=False
# Hide games which are listed as broken in Launchbox.
game_broken=True
# Hide games which are listed as hidden in Launchbox.
game_hide=True
	
# Choose platforms (comment/uncomment as needed).
# The first string in each pair is the Launchbox platform filename, the second is the RetroPie folder name.
# Arcade is disabled in this example.
platforms = dict()
#platforms["Arcade"] = "arcade"
platforms["Nintendo 64"] = "n64"
platforms["Nintendo Entertainment System"] = "nes"
platforms["Nintendo Game Boy Advance"] = "gba"
platforms["Nintendo Game Boy Color"] = "gbc"
platforms["Nintendo Game Boy"] = "gb"
platforms["Sega 32X"] = "sega32x"
platforms["Sega Game Gear"] = "gamegear"
platforms["Sega Genesis"] = "genesis"
platforms["Sega Master System"] = "mastersystem"
platforms["Sony Playstation"] = "psx"
platforms["Super Nintendo Entertainment System"] = "snes"

# Comment/uncomment to change content rating for kids.
# M - Mature, Not Rated and RP - Rating Pending disabled. The last two to be on the safe side.
kidrating = dict()
kidrating["E - Everyone"] = "true"
kidrating["EC - Early Childhood"] = "true"
kidrating["E10+ - Everyone 10+"] = "true"
kidrating["T - Teen"] = "true"
#kidrating["M - Mature"] = "true"
#kidrating["Not Rated"] = "true"
#kidrating["RP - Rating Pending"] = "true"

# Comment/uncomment to hide specific regions.
# Australia, Europe, Japan, Europe, Germany, etc. enabled in this example.
hideregion = dict()
hideregion["Asia"] = "true"
#hideregion["Australia"] = "true"
hideregion["Brazil"] = "true"
hideregion["China"] = "true"
#hideregion["Europe, Japan"] = "true"
#hideregion["Europe"] = "true"
hideregion["France"] = "true"
#hideregion["Germany"] = "true"
hideregion["Hong Kong"] = "true"
hideregion["Italy"] = "true"
hideregion["Japan"] = "true"
hideregion["Korea"] = "true"
#hideregion["North America, Europe"] = "true"
#hideregion["North America, Japan"] = "true"
#hideregion["North America"] = "true"
hideregion["Russia"] = "true"
hideregion["Spain"] = "true"
hideregion["The Netherlands"] = "true"
#hideregion["United Kingdom"] = "true"
#hideregion["World"] = "true"

###edits should not be required below here###
playercount = dict()
playercount["2-Player Alternating"] = "2"
playercount["2-Player Simultaneous"] = "2"
playercount["3-Player Simultaneous"] = "3"
playercount["4-Player Alternating / 2-Player Simultaneous"] = "4"
playercount["4-Player Alternating"] = "4"
playercount["4-Player Simultaneous"] = "4"
playercount["6-Player Simultaneous"] = "6"
playercount["8-Player Alternating / 2-Player Simultaneous"] = "8"
playercount["8-Player Simultaneous"] = "8"
playercount["Cooperative; Multiplayer"] = "1+"
playercount["Kooperativ; Multiplayer"] = "1+"
playercount["Multiplayer"] = "1+"
playercount["Single Player"] = "1"

for platform in platforms.keys():
    platform_lb=platform
    platform_rp=platforms[platform]
    lb_platform_xml = r'%s\Data\Platforms\%s.xml' % (lb_dir, platform_lb)
    lb_image_dir = r'%s\images\%s\Box - Front' % (lb_dir, platform_lb)
    output_roms = r'%s\roms' % output_dir
    output_roms_platform = r'%s\%s' % (output_roms, platform_rp)
    output_image_dir = r'%s\images' % output_roms_platform
    output_xml_dir = r'%s\gamelists' % output_dir
    output_xml_dir_platform = r'%s\%s' % (output_xml_dir, platform_rp)
    output_xml = r'%s\gamelist.xml' % output_xml_dir_platform

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
        
    if not os.path.isdir(output_roms):
        os.mkdir(output_roms)  
        
    if not os.path.isdir(output_roms_platform):
        os.mkdir(output_roms_platform)    

    if not os.path.isdir(output_image_dir):
        os.mkdir(output_image_dir)   
        
    if not os.path.isdir(output_xml_dir):
        os.mkdir(output_xml_dir)

    if not os.path.isdir(output_xml_dir_platform):
        os.mkdir(output_xml_dir_platform)      
       
    xmltree = ET.parse(lb_platform_xml)
    games_found = []
    images = []
    for fname in glob.glob(r'%s\**' % lb_image_dir, recursive=True):
        img_path = os.path.join(lb_image_dir, fname)
        if not os.path.isdir(img_path):
            images.append(img_path)

    def get_image(input):
        input = input.replace(":","_")
        input = input.replace("'","_")
        input = input.replace("/","_")
        for image_path in images:
            image_name = os.path.basename(r'%s' % image_path)
            if image_name.startswith(input + '-01.'):
                return [image_name, image_path]
    
    def save_image(original_path, output_dir):
        try:
            filename = os.path.basename(r'%s' % original_path)
            original_image = Image.open(r'%s' % original_path)
            original_image.load
            width = int(original_image.size[0])
            height = int(original_image.size[1])
            ratio = 0
            if (width > 500) and (width > height):
                ratio = width/500
            elif (height > 500) and (height > width):
                ratio = height/500
            if ratio > 0:
                width = width / ratio
                height = height / ratio
                size = (width, height)
                original_image.thumbnail(size)
                original_image.save(r'%s' % output_dir + r'\%s' % filename)
            else: 
                copy(r'%s' % original_path, r'%s' % output_dir)              
        except Exception as e:
            print(r'Couldnt resize image, copying as is: %s' % original_path)
            copy(r'%s' % original_path, r'%s' % output_dir)
            print(e)  
            
    for game in xmltree.getroot():
        try:
            this_game = dict()
			
            if (favorites_only == False) or (favorites_only == True and game.find("Favorite").text == 'true'):
			
                print("%s: %s" % (platform_lb, game.find("Title").text))
				
                rom_path = game.find("ApplicationPath").text        
                this_game["path"]="./" + os.path.basename(r'%s' % game.find("ApplicationPath").text)
				
                this_game["name"]=game.find("Title").text

                if not game.find("Notes") is None:
                    this_game["desc"]=game.find("Notes").text

                try:
                    image_info = get_image(this_game["name"])
                    image_file = image_info[0]
                    image_path = image_info[1]        
                    this_game["image"]="./images/" + image_file
                except:
                    this_game["image"]=""

                if not game.find("StarRating") is None:    
                    this_game["rating"]=(int(game.find("StarRating").text)*2/10)

                if not game.find("ReleaseDate") is None:
                    this_game["releasedate"]=game.find("ReleaseDate").text.replace("-","").split("T")[0] + "T000000"

                if not game.find("Developer") is None:
                    this_game["developer"]=game.find("Developer").text

                if not game.find("Publisher") is None: 
                    this_game["publisher"]=game.find("Publisher").text
  
                if not game.find("Genre") is None:
                    this_game["genre"]=game.find("Genre").text
    
                if not game.find("PlayMode") is None and game.find("PlayMode").text in playercount.keys():
                    this_game["players"]=playercount[game.find("PlayMode").text]
                else:
                    this_game["players"]="1?"

                if not game.find("Rating") is None and game.find("Rating").text in kidrating.keys():
                    this_game["kidgame"]=kidrating[game.find("Rating").text]
                else:
                    this_game["kidgame"]="false"
     
                if not game.find("Region") is None and game.find("Region").text in hideregion.keys():
                    this_game["hidden"]=hideregion[game.find("Region").text]
                elif not game.find("Hide") is None and game_hide == True:
                    this_game["hidden"]=game.find("Hide").text
                elif not game.find("Broken") is None and game_broken == True:
                    this_game["hidden"]=game.find("Broken").text
                else:
                    this_game["hidden"]="false"                					
					
                if not game.find("Favorite") is None:
                    this_game["favorite"]=game.find("Favorite").text
					
                games_found.append(this_game)

                save_image(image_path, output_image_dir)

                copy(rom_path, output_roms_platform)

        except Exception as e:
            print(e)
            
    top = ET.Element('gameList')
    for game in games_found:
        child = ET.SubElement(top, 'game')
        for key in game.keys():
            child_content = ET.SubElement(child, key)    
            child_content.text = game[key]

    try:
        xmlstr = minidom.parseString(ET.tostring(top)).toprettyxml(indent="    ")
        with io.open(output_xml, "w", encoding="utf-8") as f:
            f.write(xmlstr)
    except Exception as e:
            print(e)
