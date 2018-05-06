import PIL 
import PIL.ImageDraw
import matplotlib.pyplot as plt
import os
 
if __name__ == "__main__":
    directory = None
    if directory == None:
        directory = os.getcwd()
    image_list = []
    file_list = []
    directory_list = os.listdir(directory)
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass
    
    new_image_filename = os.path.join(absolute_filename + '.png')
    width, height = image.size

    rounded_mask1 = PIL.Image.new('RGBA', (width, height), (127,0,0,255))
    drawing_layer1 = PIL.ImageDraw.Draw(rounded_mask1)
    
    drawing_layer1.polygon([(0,height),(50,height),(50,0),(0,0)],fill=(80,80,176,0))
    drawing_layer1.polygon([(width, 50),(width,0),(0,0),(0,50)],fill=(80,80,176,0))
    drawing_layer1.polygon([(0,height),(width,height),(width,height-50),(0,height-50)],fill=(80,80,176,0))
    drawing_layer1.polygon([(width-50,height),(width,height),(width,0),(width-50,0)],fill=(80,80,176,0))
    
    result1 = PIL.Image.new('RGBA', (width, height), (0,0,0,255))
    result1.paste(image, (0,0), mask=rounded_mask1)
    result1.save(new_image_filename)
    

    fig, ax = plt.subplots(1, 1)
    ax.imshow(result1)
    fig.show()      
    