#Author-
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback, re

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        title = 'Import Airfoil .dat file'
        if not design:
            ui.messageBox('No active Fusion design', title)
            return
        
        dlg = ui.createFileDialog()
        dlg.title = 'Open airfoil .dat or .txt File'
        dlg.filter = 'formatted airfoil profiles (*.dat;*.txt);;All Files (*.*)'
        if dlg.showOpen() != adsk.core.DialogResults.DialogOK :
            ui.messageBox('Program exited early', title)            
            return
                  
        points = adsk.core.ObjectCollection.create()
                
        filename = dlg.filename
        
        with open(filename) as lines:
            for i, line in enumerate(lines):
                if i >= 0:
                    matches = re.findall(r'\D([-]*\d[.]\d+)',line) #r'([-]*\d.\d+)'
                                        
                    if len(matches) > 0:
                        x_value = float(matches[0])
                        y_value = float(matches[1])
                        points.add(adsk.core.Point3D.create(x_value,y_value,0))
        
        if len(points) > 0:      
            if points[0].getData() == points[-1].getData():
                points[0].set(1,0.001,0)
                points[-1].set(1,-0.001,0)
        else:
                ui.messageBox('no valid points in dat file',title)
                return
                
                 # Get the root component of the active design.
        rootComp = design.rootComponent

        # Create a new sketch on the xy plane.
        sketches = rootComp.sketches
        xyPlane = rootComp.xYConstructionPlane
        sketch = sketches.add(xyPlane)

        initial_spline = sketch.sketchCurves.sketchFittedSplines.add(points)
        
        start_point = initial_spline.startSketchPoint
        end_point = initial_spline.endSketchPoint
        
        vector1 = adsk.core.Vector3D.create(0, -0.001, 0)
        vector2 = adsk.core.Vector3D.create(0, 0.001, 0)
        
        start_point.move(vector1)
        end_point.move(vector2)
        
        status_message = 'airfoil spline import unsuccessful, please try again'

        if initial_spline.isValid == True:
            status_message = 'airfoil spline import successful'
            
        ui.messageBox(status_message, title)
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
