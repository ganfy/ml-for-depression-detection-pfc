import csv

def preprocess_csv(csv_file):
  """
  Preprocesa un archivo CSV con líneas en el formato especificado.

  Args:
    csv_file: El nombre del archivo CSV a preprocesar.

  Returns:
    Un archivo TXT con el texto de los diálogos solamente, quitando timestamps y otros.
  """

  with open(csv_file, "r") as f:
    reader = csv.reader(f, delimiter="\t")

    dialogues = []
    for row in reader:
      dialogue = []
      for item in row:
        if item != "timestamp":
          dialogue.append(item)
      dialogues.append(" ".join(dialogue))

  with open("dialogues.txt", "w") as f:
    for dialogue in dialogues:
      f.write(dialogue + "\n")


csv_file = "test/300/300_TRANSCRIPT.csv"
preprocess_csv(csv_file)
