import skia

width, height = 200, 200
stream = skia.FILEWStream('output.pdf')
with skia.PDF.MakeDocument(stream) as document:
    with document.page(width, height) as canvas:
        canvas.drawCircle(100, 100, 40, skia.Paint(Color=skia.ColorGREEN))
