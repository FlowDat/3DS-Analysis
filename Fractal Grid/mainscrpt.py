#### To postprocess big data output of DNS simulation########

from paraview.simple import *
paraview.simple._DisableFirstRenderCameraReset()

renderView1 = GetActiveViewOrCreate('RenderView')
Delete(renderView1)
del renderView1

LoadState('/project/sate1.pvsm')

#foamfoam = OpenFOAMReader(FileName='/home/foam.foam')

#foamfoam.Createcelltopointfiltereddata = 0
renderView1 = GetActiveViewOrCreate('RenderView')
#foamfoamDisplay = Show(foamfoam, renderView1)
#ColorBy(foamfoamDisplay, ('CELLS', 'U'))
#uLUT = GetColorTransferFunction('U')
#uLUT.VectorMode = 'Magnitude'
#uLUT.VectorMode = 'Component'
#uLUT.VectorComponent = 0
#uLUT.RescaleTransferFunction(1, 2)
WriteAnimation('//default/regular/x1.jpg')
