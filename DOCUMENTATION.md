# Documentation

## Python

`to_head(project_path: str)` - loads the latex style files, always goes first

`to_cor()` - defines latex colors, usually comes second

`to_begin()` - starts the tikz picture, is required before all subsequent commands!

`to_input(pathfile: str, to: tuple, width: int, height: int, name: str)` - draws an image as the first layer to
represent the input

`to_end()` - always comes at the end!

`to_generate(arch : List[str], pathname : str)` - generates latex code for the defined latex architecture

`to_connection(from: str, to: str)` - draws an arrow between two layers (given by their name/tag)

`to_skip(from : str, to: str)` - draws a skip connection (U shaped arrow going upwards)

Most layer functions are as follows:

`to_xxx(name: str, s_filer : int, n_filer: Tuple[int, int], offset: str, to: str, width: int, height: int, depth: int, caption: str)`

Available:

- ConvConvRelu
- Pool
- UnPool
- ConvRes
- ConvSoftMax
- SoftMax
- Sum
  Furthermore (these need to be included using spread operator):
- 2ConvPool
- UnConv
- Res

## Latex

<https://github.com/carhartt21/PlotNeuralNet> has added some more latex layers and examples.

Colors:

- Conv
- ConvRelu
- Pool
- UnPool
- Fc
- FcRelu
- Softmax

Shapes:

- Ball (for elementwise or reduction operations)
- Block (simple cube with custom colors. Used for conv, fc, etc.)
- RightBandedBox (simple cube with colored stripe on the right. Used for layer + activation function)

## Export as SVG

Just run the stuff above then convert pdf to svg.

```bash
inkscape --without-gui --file=input.pdf --export-plain-svg=output.svg
```