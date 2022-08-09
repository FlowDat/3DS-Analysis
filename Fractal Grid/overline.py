from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()
foamfoam = OpenFOAMReader(FileName='/project/k1093/x_usamasm/rooh_2dfract/foam.foam')
foamfoam.CaseType = 'Decomposed Case'
plotOverLine1 = PlotOverLine(Input=foamfoam, Source='High Resolution Line Source')
plotOverLine1.Tolerance = 2.2e-16
plotOverLine1.Source.Point1 = [0.0, 57.6, 57.6]
plotOverLine1.Source.Point2 = [460.8, 57.6, 57.6]
plotOverLine1.Source.Resolution = 500
SaveData('/project/k1093/x_usamasm/rooh_2dfract/postProcessing/centerline.csv', proxy=plotOverLine1, WriteAllTimeSteps=1)
