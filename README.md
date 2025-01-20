# Web Image Resizer
## Discription
The Web Image Resizer is a small Python project to simplify and speed up the resizing process of images used for websites.
## Background
Python was installed with homebrew and uses Pillow for image processing.
## Sizes
The sizes are taken from the standard media queries from [Tailwind CSS](https://tailwindcss.com/docs/responsive-design):

| Size | Width  |
|------|--------|
| sm   | 640px  |
| md   | 768px  |
| lg   | 1024px |
| xl   | 1280px |
| 2xl  | 1536px |

## Workflow
1. put the origin images into /input
2. run the Python code
```
python web-img-sizer.py
```
3. Resized images will be saved in /output