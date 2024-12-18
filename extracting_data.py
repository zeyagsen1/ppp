import fitz  # PyMuPDF
import os
import cv2
from paddleocr import PaddleOCR
import numpy as np
from PIL import Image
'''
# Path to your PDF file

pdf_path = 'TheoryOfComputation.pdf'  # Replace with the actual path

# Define output folders
image_folder = 'extracted_images'
vector_folder = 'vector_graphics'
text_free_folder = 'text_free_images'
shape_folder = 'shapes'

# Create output folders if they don't exist
os.makedirs(image_folder, exist_ok=True)
os.makedirs(vector_folder, exist_ok=True)
os.makedirs(text_free_folder, exist_ok=True)
os.makedirs(shape_folder, exist_ok=True)

# Open the PDF
pdf = fitz.open(pdf_path)

# Iterate through all pages in the PDF
for page_number in range(len(pdf)):
    page = pdf.load_page(page_number)

    # Extract raster images (JPEG, PNG)
    images_on_page = page.get_images(full=True)

    if images_on_page:
        for image_index, image in enumerate(images_on_page):
            img_reference = image[0]
            base_image = pdf.extract_image(img_reference)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            image_filename = f"page_{page_number + 1}_image_{image_index + 1}.{image_ext}"
            image_path = os.path.join(image_folder, image_filename)

            with open(image_path, "wb",encoding='utf-8') as image_file:
                image_file.write(image_bytes)
            print(f"Image saved: {image_path}")
    else:
        # Save the page as a full-page image (rasterized)
        pix = page.get_pixmap()
        image_filename = f"page_{page_number + 1}_full_page.png"
        image_path = os.path.join(image_folder, image_filename)
        pix.save(image_path)
        print(f"Full page image saved: {image_path}")

    # Extract vector graphics (SVG format)
    vector_text = page.get_text("svg")
    if vector_text:
        vector_filename = f"page_{page_number + 1}_vector.svg"
        vector_path = os.path.join(vector_folder, vector_filename)

        with open(vector_path, 'w',encoding='utf-8') as vector_file:
            vector_file.write(vector_text)
        print(f"Vector content saved: {vector_path}")

# Close the PDF file
pdf.close()

# OCR and Text Masking
ocr = PaddleOCR()
for image_name in os.listdir(image_folder):
    img_path = os.path.join(image_folder, image_name)
    img = cv2.imread(img_path)

    results = ocr.ocr(img_path)

    for line in results[0]:
        box = line[0]
        box = [(int(x), int(y)) for x, y in box]
        cv2.fillPoly(img, [np.array(box, dtype=np.int32)], (255, 255, 255))

    output_path = os.path.join(text_free_folder, image_name)
    cv2.imwrite(output_path, img)
    print(f"Image without text saved as '{output_path}'")

# Shape Extraction
text_free_folder = 'extracted_images'
shape_folder = 'shapee'
os.makedirs(shape_folder, exist_ok=True)

for image_name in os.listdir(text_free_folder):
    img_path = os.path.join(text_free_folder, image_name)
    image = cv2.imread(img_path)

    # Convert to grayscale and threshold
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 230, 255, cv2.THRESH_BINARY_INV)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on area (to exclude noise)
    filtered_contours = [c for c in contours if cv2.contourArea(c) > 500]  # Adjust area threshold as needed

    # Sort contours by position to maintain figure order
    sorted_contours = sorted(filtered_contours, key=lambda c: cv2.boundingRect(c)[1])  # Sort by Y coordinate

    for i, contour in enumerate(sorted_contours):
        # Get bounding box for each contour
        x, y, w, h = cv2.boundingRect(contour)

        # Extract and save each figure
        cropped_shape = image[y:y+h, x:x+w]

        # Optional: Add padding around the extracted shape
        padding = 10
        cropped_shape = cv2.copyMakeBorder(
            cropped_shape,
            top=padding,
            bottom=padding,
            left=padding,
            right=padding,
            borderType=cv2.BORDER_CONSTANT,
            value=(255, 255, 255)  # White padding
        )

        output_path = os.path.join(shape_folder, f"{os.path.splitext(image_name)[0]}_shape_{i+1}.png")
        cv2.imwrite(output_path, cropped_shape)
        print(f"Shape {i+1} extracted and saved to: {output_path}")

folder_path_to_delete='C:/Users/ibrah/Masaüstü/data_Extraction/shapes'
delete_images=[]
counter=0
for image_name in os.listdir(folder_path_to_delete):
 img_path=os.path.join(folder_path_to_delete,image_name)  
 im_width,img_height=Image.open(img_path).size 
 if  im_width and img_height<10 :
    print (f" image {img_path} {counter}")
    counter=counter+1
  

pdf_path = 'TheoryOfComputation.pdf' 
file_name='C:/Users/ibrah/Masaüstü/data_Extraction/yaz'

# get texts on each page
pdf = fitz.open(pdf_path)

for page_number in range(len(pdf)):
    page = pdf.load_page(page_number)
    text_on_page=page.get_text("text")
    file_name = f"{page_number+1}_full_page.txt"
    
      # Write the text to the file
    with open(file_name, "w", encoding="utf-8") as f:
     f.write(text_on_page)

#delete text files that aren't necessary cause there is no image in some pages.
numbers=[]
for name in os.listdir('shapee'):
    ar =name.split('_')
    numbers.append(ar[1])

c='C:/Users/ibrah/Masaüstü/data_Extraction/extracted_texts'

for name in os.listdir(c):
    print(name)
    ar =name.split('_')
    if not ar[0] in numbers:
        k= os.path.join(c,name)
        if(os.path.exists(k)): 
         os.remove(k)
'''
