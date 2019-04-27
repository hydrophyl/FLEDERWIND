.TL
How PNG works
.AU
Duy Nguyen
.AI
HAW-Hamburg
FLEDERWIND-Projekt
.NH
General
.PP
PNG: Portable Network Graphics
.NH 2
Understanding the Compression
.PP
PNG's compression process is entirely lossless, meaning that the compressed file can reconstruct
the source image exactly. Done in two stages: prediction (aka filtering) and then compression.

.NH 2
Filtering (prediction)
.PP
Basic idea of delta encoding: represent any value as a difference from the previous value, so:

[2,3,4,5,6,7,8] can become [2,1,1,1,1,1,1], where

[2,3-2,4-3,5-4,6-5,7-6,8-7]

PNG make use of delta encoding in a format "Filtering". For each scan-line of pixels, a current pixel is
encoded in some relation to the pixel to the left, the pixel above, and the pixel above-left.

https://medium.com/@duhroach/how-png-works-f1174e3cc7b7

http://www.libpng.org/pub/png/book/chapter09.html

.NH 2
Compression (DEFLATE)
.PP
Huffman coding
LZ77 compression: just like compression RAW-data to Zip file.

https://www.zlib.net/feldspar.html

For images:

BMP 256: Raw color data RGB (for each Red, Green, Blue parameter 8 bit [0 ... 255])

PNG 256: compressed images RGB (for each Red, Green, Blue parameter 8 bit [0 ... 255])

PNG 256 Grayscale: compressed images in grayscale (for just Grayscale value 8 bit [0 ... 255])


.NH
Radar images calculations
.NH 2
Frame grabber
.PP
2,5s per pictures. -> 17280 pics per day (12 hours of taking pictures on radar per day)

BMP 256: 3,8MB/pic -> 64,125GB per day

PNG 256: 251KB/pic -> 4,13GB per day

PNG 256 GS: 138KB/pic -> 2,274GB per day

.NH 2
Conclusions
.PP
Grayscale is not good enough for men to work with, so in the future with better computer algorithms (motion tracking, machine learning, ...) is grayscale also a good choice due to its compressed sizes.
.PP
PNG 256 RGB simple calculations:

Theory: 10TB Hard drive disk ->
.B "12,3 years"
(PNG 256 RGB) of taking radar pictures.

In comparison to: BMP 256 ->
.B "159,7 days"
of taking radar pictures.
