# airfoil_toolkit_fusion360
Add-in scripts for importing and processing airfoils in Autodesk Fusion 360

‘Airfoil Toolkit’ is an ambitious name for what is currently a very simple add-in script I wrote in python for Autodesk Fusion 360™. The script allows you to import commonly available airfoil coordinate data files.

Once imported into Autodesk Fusion 360™ airfoil files can be used in the design of wings, aircraft, turbine blades, sails, hydrofoils etc.

I’m hoping to add a lot more functionality to the code in future to allow for more complex operations to import, scale, rotate and translate sets of airfoils for use in wing + blade designs.

To install the script you’ll need to save the ‘*.py’ file it in it’s own folder and then add the script via the ‘add-ins’ button on the command ribbon of Fusion 360

Compatibility

 ‘Selig’ format airfoil ‘.dat’ files such as those that can be downloaded from websites such as www.airfoiltools.com or exported from tools such as XFOIL http://web.mit.edu/drela/Public/web/xfoil/ or XFLR5 www.xflr5.com
The ordering of the points should be anti-clockwise from the trailing edge  off the upper/suction surface to the leading edge, then back to the trailing edge of the lower/pressure surface
The script can handle airfoils with sharp (closed) and blunt (open) trailing edges

About this version:

This is version 0.1


General usage instructions:

Add/install the script to your installation of Autodesk Fusion 360™
Download or generate a suitable airfoil format and ensure the file extension is either *.dat or *.txt
Run the script from the command ribbon ‘Add-Ins’
A dialog box will pop-up when the airfoil has been successfully imported
The airfoil will appear as a spline on a new sketch on the x-y plane

The script only includes extremely basic error handling, and a dialog box will pop up if the spline import was unsuccessful, or if the script was quit before an airfoil file was selected.
