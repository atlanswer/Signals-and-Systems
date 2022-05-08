audio = Sound[{SoundNote["G4", 0.5, "Violin"], 
   SoundNote["A4", 0.5, "Violin"], SoundNote["G4", 0.5, "Violin"], 
   SoundNote["F4", 0.5, "Violin"], SoundNote["E4", 0.5, "Violin"], 
   SoundNote["D4", 0.5, "Violin"], SoundNote["C4", 1.5, "Violin"], 
   SoundNote["G3", 1.5, "Violin"], SoundNote["C4", 0.5, "Violin"], 
   SoundNote["E4", 0.5, "Violin"], SoundNote["C5", 0.5, "Violin"], 
   SoundNote["B4", 0.5, "Violin"], SoundNote["A4", 0.75, "Violin"], 
   SoundNote["E4", 0.25, "Violin"], SoundNote["G4", 2, "Violin"]}]
Spectrogram[audio,  PlotRange -> {100, 1000}]
AudioPlot[audio]
