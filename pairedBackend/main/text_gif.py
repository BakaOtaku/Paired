

import sys
import datetime
import imageio

# import PIL

VALID_EXTENSIONS = ('png', 'jpg')


def create_gif(filenames, duration):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    output_file = 'output.gif'
    imageio.mimsave(output_file, images, duration=duration)


if __name__ == "__main__":
    
    world='helloji'
    
    

    image=[]

    for i in world:
        charr=i.upper()
        st=f'signlanguagePic/{charr}.PNG'
        image.append(st)
    
   
    duration = float(0.25)

    
    

    create_gif(image, duration)

