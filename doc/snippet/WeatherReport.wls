wd = Normal[WeatherForecastData["Temperature"]];
DateListPlot[wd, IntervalMarkers -> "Bands",
    Sequence[
    AxesLabel -> Automatic, ImageSize -> 450,
    PlotTheme -> "Detailed", FrameLabel -> Automatic,
    IntervalMarkersStyle -> {Thin, Gray}, 
    ColorFunction -> "TemperatureMap", 
    InterpolationOrder -> Automatic, 
    PlotRange -> All, PlotStyle -> Thickness[0.01],
    PlotLabel -> First[GeoNearest[Entity["City"], Here]],
    LabelStyle -> 16
    ]
]
