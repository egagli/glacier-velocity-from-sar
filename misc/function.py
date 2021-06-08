from skimage.filters.rank import median
from skimage.morphology import disk
from skimage import img_as_ubyte
def denoising_im(im):
  """ 
  display denoise image

  This function remove noise on the input image 

  Parameters
  ----------
  im: float image
 

  Returns
  ----------
  none (display is the output)

  Examples
  ----------
   >>>denoising_im(muldrow)

  displays 4 set of images with plot size (22,7) with magnitude displayed by side

  >>>display_log(muldrow)

  displays log of image with default plot size (15,10) with no magnitude plot

  """

  noisy_image = img_as_ubyte(im)
  noise = np.random.random(noisy_image.shape)
  noisy_image = img_as_ubyte(im)
  noisy_image[noise > 0.99] = 255
  noisy_image[noise < 0.01] = 0
  fig, ax = plt.subplots(2, 2, figsize=(10, 7), sharex=True, sharey=True)
  ax1, ax2, ax3, ax4 = ax.ravel()

  ax1.imshow(noisy_image, vmin=0, vmax=255, cmap=plt.cm.gray)
  ax1.set_title('Noisy image')
  ax1.axis('off')


  ax2.imshow(median(noisy_image, disk(1)), vmin=0, vmax=255, cmap=plt.cm.gray)
  ax2.set_title('Median $r=1$')
  ax2.axis('off')


  ax3.imshow(median(noisy_image, disk(5)), vmin=0, vmax=255, cmap=plt.cm.gray)
  ax3.set_title('Median $r=5$')
  ax3.axis('off')



  ax4.imshow(median(noisy_image, disk(20)), vmin=0, vmax=255, cmap=plt.cm.gray)
  ax4.set_title('Median $r=20$')
  ax4.axis('off') 
    
    
  
