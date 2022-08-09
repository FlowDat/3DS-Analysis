from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()
foamfoam = OpenFOAMReader(FileName='/project/k1093/x_usamasm/scalartrans/default/regular/foam.foam')
#foamfoam.CaseType = 'Decomposed Case'

plotOverLine1 = PlotOverLine(Input=foamfoam, Source='High Resolution Line Source')
plotOverLine1.Tolerance = 2.2e-16
plotOverLine1.Source.Point1 = [0.0, 57.6, 57.6]
plotOverLine1.Source.Point2 = [460.8, 57.6, 57.6]
plotOverLine1.Source.Resolution = 500
SaveData('/project/k1093/x_usamasm/production/validate/postProcessing/x57.csv', proxy=plotOverLine1, WriteAllTimeSteps=1)


plotOverLine4 = PlotOverLine(Input=foamfoam, Source='High Resolution Line Source')
plotOverLine4.Tolerance = 2.2e-16
plotOverLine4.Source.Point1 = [0.0, 86.4, 86.4 ]
plotOverLine4.Source.Point2 = [460.8, 86.4, 86.4]
plotOverLine4.Source.Resolution = 500
SaveData('/project/k1093/x_usamasm/production/validate/postProcessing/x86.csv', proxy=plotOverLine4, WriteAllTimeSteps=1)

plotOverLine6 = PlotOverLine(Input=foamfoam, Source='High Resolution Line Source')
plotOverLine6.Tolerance = 2.2e-16
plotOverLine6.Source.Point1 = [0.0, 100.8, 100.8]
plotOverLine6.Source.Point2 = [460.8, 100.8, 100.8]
plotOverLine6.Source.Resolution = 500
SaveData('/project/k1093/x_usamasm/production/validate/postProcessing/x100.csv', proxy=plotOverLine6, WriteAllTimeSteps=1)

plotOverLine5 = PlotOverLine(Input=foamfoam, Source='High Resolution Line Source')
plotOverLine5.Tolerance = 2.2e-16
plotOverLine5.Source.Point1 = [0.0, 57.6, 108]
plotOverLine5.Source.Point2 = [460.8, 57.6, 108]
plotOverLine5.Source.Resolution = 500
SaveData('/project/k1093/x_usamasm/production/validate/postProcessing/x57108.csv', proxy=plotOverLine5, WriteAllTimeSteps=1)


plotOverLine2 = PlotOverLine(Input=foamfoam, Source='High Resolution Line Source')
plotOverLine2.Tolerance = 2.2e-16
plotOverLine2.Source.Point1 = [0.0, 57.6, 86.4]
plotOverLine2.Source.Point2 = [460.8, 57.6, 86.4]
plotOverLine2.Source.Resolution = 500
SaveData('/project/k1093/x_usamasm/production/validate/postProcessing/x5786.csv', proxy=plotOverLine2, WriteAllTimeSteps=1)


plotOverLine3 = PlotOverLine(Input=foamfoam, Source='High Resolution Line Source')
plotOverLine3.Tolerance = 2.2e-16
plotOverLine3.Source.Point1 = [0.0, 57.6, 100.8]
plotOverLine3.Source.Point2 = [460.8, 57.6, 100.8]
plotOverLine3.Source.Resolution = 500
SaveData('/project/k1093/x_usamasm/production/validate/postProcessing/x57100.csv', proxy=plotOverLine2, WriteAllTimeSteps=1)

