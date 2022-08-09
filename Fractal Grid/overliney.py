from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()
foamfoam = OpenFOAMReader(FileName='/project/k1093/x_usamasm/scalartrans/default/regular/foam.foam')
#foamfoam.CaseType = 'Decomposed Case'
plotOverLine1 = PlotOverLine(Input=foamfoam, Source='High Resolution Line Source')
plotOverLine1.Tolerance = 2.2e-16
plotOverLine1.Source.Point1 = [150, 0, 57.6]
plotOverLine1.Source.Point2 = [150, 115.2, 57.6]
plotOverLine1.Source.Resolution = 500
SaveData('/project/k1093/x_usamasm/production/validate/postProcessing/150y.csv', proxy=plotOverLine1, WriteAllTimeSteps=1)


plotOverLine2 = PlotOverLine(Input=foamfoam, Source='High Resolution Line Source')
plotOverLine2.Tolerance = 2.2e-16
plotOverLine2.Source.Point1 = [225, 0, 57.6]
plotOverLine2.Source.Point2 = [225, 115.2, 57.6]
plotOverLine2.Source.Resolution = 500
SaveData('/project/k1093/x_usamasm/production/validate/postProcessing/225y.csv', proxy=plotOverLine2, WriteAllTimeSteps=1)

plotOverLine3 = PlotOverLine(Input=foamfoam, Source='High Resolution Line Source')
plotOverLine3.Tolerance = 2.2e-16
plotOverLine3.Source.Point1 = [300, 0, 57.6]
plotOverLine3.Source.Point2 = [300, 115.2, 57.6]
plotOverLine3.Source.Resolution = 500
SaveData('/project/k1093/x_usamasm/production/validate/postProcessing/300y.csv', proxy=plotOverLine3, WriteAllTimeSteps=1)

plotOverLine4 = PlotOverLine(Input=foamfoam, Source='High Resolution Line Source')
plotOverLine4.Tolerance = 2.2e-16
plotOverLine4.Source.Point1 = [375, 0, 57.6]
plotOverLine4.Source.Point2 = [375, 115.2, 57.6]
plotOverLine4.Source.Resolution = 500
SaveData('/project/k1093/x_usamasm/production/validate/postProcessing/375y.csv', proxy=plotOverLine4, WriteAllTimeSteps=1)

plotOverLine5 = PlotOverLine(Input=foamfoam, Source='High Resolution Line Source')
plotOverLine5.Tolerance = 2.2e-16
plotOverLine5.Source.Point1 = [450, 0, 57.6]
plotOverLine5.Source.Point2 = [450, 115.2, 57.6]
plotOverLine5.Source.Resolution = 500
SaveData('/project/k1093/x_usamasm/production/validate/postProcessing/450y.csv', proxy=plotOverLine5, WriteAllTimeSteps=1)

