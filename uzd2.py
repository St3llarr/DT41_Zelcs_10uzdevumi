from langdetect import detect, DetectorFactory
DetectorFactory.seed = 0

while True:
  teksts = input("Ievadiet tekstu: ")
  detected_language=detect(teksts)
  print("Teksta valoda: ", detected_language)
