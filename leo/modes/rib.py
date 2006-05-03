# Leo colorizer control file for rib mode.

# Properties for rib mode.
properties = {
	"doubleBracketIndent": "false",
	"indentNextLines": "Begin|WorldBegin|FrameBegin|TransformBegin|AttributeBegin|SolidBegin|ObjectBegin|MotionBegin",
	"lineComment": "#",
	"lineUpClosingBracket": "true",
}

# Keywords dict for rib_main ruleset.
rib_main_keywords_dict = {
	"ArchiveRecord": "keyword4",
	"AreaLightSource": "keyword2",
	"Atmosphere": "keyword2",
	"Attribute": "keyword2",
	"AttributeBegin": "keyword2",
	"AttributeEnd": "keyword2",
	"Basis": "keyword3",
	"Begin": "keyword2",
	"Blobby": "keyword3",
	"Bound": "keyword2",
	"Clipping": "keyword2",
	"ClippingPlane": "keyword2",
	"Color": "keyword2",
	"ColorSamples": "keyword2",
	"ConcatTransform": "keyword2",
	"Cone": "keyword3",
	"Context": "keyword2",
	"ContextHandle": "keyword2",
	"CoordSysTransform": "keyword2",
	"CoordinateSystem": "keyword2",
	"CropWindow": "keyword2",
	"Curves": "keyword3",
	"Cylinder": "keyword3",
	"Declare": "keyword2",
	"Deformation": "keyword4",
	"DelayedReadArchive": "keyword3",
	"DepthOfField": "keyword2",
	"Detail": "keyword2",
	"DetailRange": "keyword2",
	"Disk": "keyword3",
	"Displacement": "keyword2",
	"Display": "keyword2",
	"DynamicLoad": "keyword3",
	"End": "keyword2",
	"ErrorHandler": "keyword4",
	"Exposure": "keyword2",
	"Exterior": "keyword2",
	"Format": "keyword2",
	"FrameAspectRatio": "keyword2",
	"FrameBegin": "keyword2",
	"FrameEnd": "keyword2",
	"GeneralPolygon": "keyword3",
	"GeometricApproximation": "keyword2",
	"Geometry": "keyword3",
	"Hider": "keyword2",
	"Hyperboloid": "keyword3",
	"Identity": "keyword2",
	"Illuminate": "keyword2",
	"Imager": "keyword2",
	"Interior": "keyword2",
	"LightSource": "keyword2",
	"MakeBump": "keyword4",
	"MakeCubeFaceEnvironment": "keyword4",
	"MakeLatLongEnvironment": "keyword4",
	"MakeShadow": "keyword4",
	"MakeTexture": "keyword4",
	"Matte": "keyword2",
	"MotionBegin": "keyword2",
	"MotionEnd": "keyword2",
	"NuPatch": "keyword3",
	"ObjectBegin": "keyword3",
	"ObjectEnd": "keyword3",
	"ObjectInstance": "keyword3",
	"Opacity": "keyword2",
	"Option": "keyword2",
	"Orientation": "keyword2",
	"Paraboloid": "keyword3",
	"Patch": "keyword3",
	"PatchMesh": "keyword3",
	"Perspective": "keyword2",
	"PixelFilter": "keyword2",
	"PixelSamples": "keyword2",
	"PixelVariance": "keyword2",
	"Points": "keyword3",
	"PointsGeneralPolygons": "keyword3",
	"PointsPolygons": "keyword3",
	"Polygon": "keyword3",
	"Procedural": "keyword3",
	"Projection": "keyword2",
	"Quantize": "keyword2",
	"ReadArchive": "keyword4",
	"RelativeDetail": "keyword2",
	"ReverseOrientation": "keyword2",
	"Rotate": "keyword2",
	"RtContextHandle": "keyword2",
	"RtLightHandle": "keyword2",
	"RtObjectHandle": "keyword3",
	"RunProgram": "keyword3",
	"Scale": "keyword2",
	"ScreenWindow": "keyword2",
	"ShadingInterpolation": "keyword2",
	"ShadingRate": "keyword2",
	"Shutter": "keyword2",
	"Sides": "keyword2",
	"Skew": "keyword2",
	"SolidBegin": "keyword3",
	"SolidEnd": "keyword3",
	"Sphere": "keyword3",
	"SubdivisionMesh": "keyword3",
	"Surface": "keyword2",
	"TextureCoordinates": "keyword2",
	"Torus": "keyword3",
	"Transform": "keyword2",
	"TransformBegin": "keyword2",
	"TransformEnd": "keyword2",
	"TransformPoints": "keyword2",
	"Translate": "keyword2",
	"TrimCurve": "keyword3",
	"WorldBegin": "keyword2",
	"WorldEnd": "keyword2",
	"color": "keyword1",
	"extern": "keyword1",
	"float": "keyword1",
	"matrix": "keyword1",
	"normal": "keyword1",
	"output": "keyword1",
	"point": "keyword1",
	"string": "keyword1",
	"uniform": "keyword1",
	"varying": "keyword1",
	"vector": "keyword1",
	"void": "keyword1",
}

# Keywords dict for rib_literals ruleset.
rib_literals_keywords_dict = {
	"Cs": "literal2",
	"N": "literal2",
	"NDC": "literal2",
	"Os": "literal2",
	"P": "literal2",
	"Pw": "literal2",
	"Pz": "literal2",
	"RI_INFINITY": "literal2",
	"RI_NULL": "literal2",
	"b-spline": "literal2",
	"bezier": "literal2",
	"bicubic": "literal2",
	"bilinear": "literal2",
	"box": "literal2",
	"camera": "literal2",
	"catmull-clark": "literal2",
	"catmull-rom": "literal2",
	"color": "keyword1",
	"constant": "literal2",
	"corner": "literal2",
	"crease": "literal2",
	"extern": "keyword1",
	"float": "keyword1",
	"gaussian": "literal2",
	"hermite": "literal2",
	"hidden": "literal2",
	"hole": "literal2",
	"inside": "literal2",
	"interpolateboundary": "literal2",
	"lh": "literal2",
	"matrix": "keyword1",
	"nonperiodic": "literal2",
	"normal": "keyword1",
	"null": "literal2",
	"object": "literal2",
	"orthographic": "literal2",
	"output": "keyword1",
	"outside": "literal2",
	"periodic": "literal2",
	"perspective": "literal2",
	"point": "keyword1",
	"power": "literal2",
	"raster": "literal2",
	"rh": "literal2",
	"screen": "literal2",
	"sinc": "literal2",
	"smooth": "literal2",
	"string": "keyword1",
	"triangle": "literal2",
	"uniform": "keyword1",
	"varying": "keyword1",
	"vector": "keyword1",
	"void": "keyword1",
	"world": "literal2",
}

# Rules for rib_main ruleset.

def rule0(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment1"', seq="#",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule1(colorer, s, i):
    return colorer.match_eol_span(s, i, kind='"comment2"', seq="#",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="", exclude_match=False)

def rule2(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="-",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule3(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="+",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule4(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="[",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule5(colorer, s, i):
    return colorer.match_seq(s, i, kind="operator", seq="]",
        at_line_start=False, at_line_end=False, at_word_start=False, delegate="")

def rule6(colorer, s, i):
    return colorer.match_span(s, i, kind='"literal1"', begin="\"", end="\"",
        at_line_start=False, at_line_end=False, at_word_start=False,
        delegate="LITERALS",exclude_match=False,
        no_escape=False, no_line_break=True, no_word_break=False)

def rule7(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for rib_main ruleset.
rib_main_rules = [
	rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule7, ]

# Rules for rib_literals ruleset.

def rule8(colorer, s, i):
    return colorer.match_keywords(s, i)

# Rules list for rib_literals ruleset.
rib_literals_rules = [
	rule8, ]

# Rules dict for rib mode.
rulesDict = {
	"rib_literals": rib_literals_rules,
	"rib_main": rib_main_rules,
}

# Import dict for rib mode.
importDict = {}

