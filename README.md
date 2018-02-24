# launchbox_retropie_export_ext

Python script to export your Launchbox game database to Retropie / Emulationstation format.

Based on [launchbox-retropie-export](https://forums.launchbox-app.com/files/file/860-launchbox-retropie-export/) by user [dingodan](https://forums.launchbox-app.com/profile/76087-dingodan/) from the launchbox forums. All credits for initial creation of this script go to him.

This extended version helps when using [Child-friendly-EmulationStation](https://github.com/RetroPie/RetroPie-Setup/wiki/Child-friendly-EmulationStation) as it parses the age ratings from the Launchbox database.

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
