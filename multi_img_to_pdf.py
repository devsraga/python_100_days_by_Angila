import os
from PIL import Image
from fpdf import FPDF
import pathlib
import glob

pdf = FPDF()
sdir = "E:\\notes_dev\\Gate_notes\\temp\\"
print(sdir)
w,h = 0,0

jpg_files = glob.glob("E:\\notes_dev\Gate_notes\\temp\*.jpg")
# jpg_files = os.listdir(sdir)  # also may use for all files

print(jpg_files)

for i in range(0, len(jpg_files)):

    # fname = sdir + jpg_files[i]
    fname = jpg_files[i]
    if os.path.exists(fname):
        if i == 0:
            cover = Image.open(fname)
            w,h = cover.size
            pdf = FPDF(unit = "pt", format = [w,h])
        image = fname
        pdf.add_page()
        pdf.image(image,0,0,w,h)
    else:
        print("File not found:", fname)
    print("processed %d" % i)
pdf.output("E:\\notes_dev\\Gate_notes\\temp\\output2.pdf", "F")
print("done")



