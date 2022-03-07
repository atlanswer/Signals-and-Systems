########
代码片段
########

#. 不同角频率条件下的正余弦函数

   .. code-block::

      DiscretePlot[
         Cos[\[Pi]/8*n], {n, -10, 10}, 
         PlotLegends -> "Cos[\[Pi]/8*n]",
         ColorFunction -> "Rainbow", 
         PlotMarkers -> Style["\[Bullet]", FontSize -> 30]
      ]
      DiscretePlot[
         Cos[\[Pi]/4*n], {n, -10, 10}, 
         PlotLegends -> "Cos[\[Pi]/4*n]",
         ColorFunction -> "Rainbow", 
         PlotMarkers -> Style["\[Bullet]", FontSize -> 30]
      ]
      DiscretePlot[
         Cos[\[Pi]/2*n], {n, -10, 10}, 
         PlotLegends -> "Cos[\[Pi]/2*n]",
         ColorFunction -> "Rainbow", 
         PlotMarkers -> Style["\[Bullet]", FontSize -> 30]
      ]
      DiscretePlot[
         Cos[3*\[Pi]/2*n], {n, -10, 10}, 
         PlotLegends -> "Cos[3*\[Pi]/2*n]", 
         ColorFunction -> "Rainbow", 
         PlotMarkers -> Style["\[Bullet]", FontSize -> 30]
      ]
      DiscretePlot[
         Cos[\[Pi]*2*n], {n, -10, 10}, 
         PlotLegends -> "Cos[\[Pi]*2*n]",
         ColorFunction -> "Rainbow", 
         PlotMarkers -> Style["\[Bullet]", FontSize -> 30]
      ]
      DiscretePlot[
         Cos[\[Pi]*17/8*n], {n, -10, 10}, 
         PlotLegends -> "Cos[\[Pi]*17/8*n]",
         ColorFunction -> "Rainbow", 
         PlotMarkers -> Style["\[Bullet]", FontSize -> 30]
      ]

#. 广州天气预报

   .. code-block::

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
