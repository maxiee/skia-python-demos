import skia

surface = skia.Surface(128, 128)

with surface as canvas:
    rect = skia.Rect(32, 32, 96, 96)
    paint = skia.Paint(
        Color=skia.ColorBLUE,
        Style=skia.Paint.kFill_Style
    )
    canvas.drawRect(rect, paint)

image = surface.makeImageSnapshot()
image.save('output.png', skia.kPNG)
