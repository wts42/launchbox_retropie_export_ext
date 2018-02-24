# launchbox_retropie_export_ext
  Python script to export your Launchbox game database to Retropie / Emulationstation format.
  Based on [launchbox-retropie-export](https://forums.launchbox-app.com/files/file/860-launchbox-retropie-export/) by user
  [dingodan](https://forums.launchbox-app.com/profile/76087-dingodan/) from the launchbox forums,
  all credits for initial creation of this script go to him. This extended version helps when using [Child-friendly-EmulationStation](https://github.com/RetroPie/RetroPie-Setup/wiki/Child-friendly-EmulationStation) as it parses the age ratings from the Launchbox database.

## Step by step instructions for using the extended version and creating a nearly kids safe Retropie
1. Prerequisites:
   * Get Python from the [Python download page](https://www.python.org/downloads/), install for all users and add it to the path. (I used python-3.6.3.exe)
   * You need an installation of [Launchbox](https://www.launchbox-app.com) with a populated database of your games so the script can extract content rating and other information.
2. Install Pillow image library by opening a cmd shell and type:
   ```cmd
   pip install Pillow
   ```
3. Download the launchbox_retropie_export_ext.py file and open it in a texteditor to edit the configuration:
   ```python
   # Change the path to your launchbox folder.
   lb_dir = r'X:\A3_Games\00_Resources\00_Launchbox\LaunchBox'
   ```

   ```python
   # Script output directory. (for Roms, images and xml files)
   # Copy the gamelists to ~/.emulationstation/gamelists/
   # Copy the roms and images to ~/RetroPie/roms/
   output_dir = r'X:\output'
   ```

   ```python
   # Restrict export to only Launchbox favorites.
   favorites_only=False
   # Hide games which are listed as broken in Launchbox.
   game_broken=True
   # Hide games which are listed as hidden in Launchbox.
   game_hide=True
   ```

   ```python
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
   ```
   
   ```python
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
   ```
   
   ```python
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
   ```   
4. Copy the Python script to your Launchbox directory and start it via following command line:
   ```cmd
   python launchbox_retropie_export_ext.py
   ```
   
5. Transfer the files to the Retropie and copy them to the correct directories.

     Copy the gamelists to ~/.emulationstation/gamelists/
     
     Copy the roms and images to ~/RetroPie/roms/

6. Enable [Child-friendly-EmulationStation](https://github.com/RetroPie/RetroPie-Setup/wiki/Child-friendly-EmulationStation) according to the wiki page.

7. Disable the rom launch menu: Retropie Menu -> Retropie Setup -> Configuration/Tools -> runcommand -> And disable Launch menu here


## Original installation instructions from [launchbox-retropie-export](https://forums.launchbox-app.com/files/file/860-launchbox-retropie-export/)
>### How to Install:
>1. Download and install Python
>2. Choose All Users and add it to your Path
>3. Open cmd, and type 'pip install Pillow'
>4. Download the attached file and edit it accordingly (specify your LaunchBox folder, desired output folder and platforms)
>5. Run 'python launchbox_retropie_export.py'
>6. Transfer the files to your Pi using WinSCP or similar
>7. Copy the gamelists to /opt/retropie/configs/all/emulationstation/gamelists
>8. Copy the roms and images to /home/pi/RetroPie/roms
>9. Enable the 'Parse Gamelists Only' option in EmulationStation
