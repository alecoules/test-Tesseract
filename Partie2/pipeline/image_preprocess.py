import os
from PIL import Image
import cv2
from skimage.filters import (threshold_otsu, threshold_niblack,
                             threshold_sauvola)
from skimage.restoration import (denoise_tv_chambolle, denoise_bilateral,
                                 denoise_wavelet)
from skimage import io
from skimage.color import rgb2gray
from skimage import img_as_uint
from skimage.exposure import equalize_adapthist

def import_image(path_image):

	image = rgb2gray(io.imread(path_image))
	return(image)

def contrast(image):

	image_CLAHE = equalize_adapthist(image)
	return(image_CLAHE)

def denoise(image, algorithm_denoise=None, weight=0.1, sigma_color=0.1, sigma_spatial=15):

	if algorithm_denoise == 'tv_chambolle':
		denoised = denoise_tv_chambolle(image, weight = weight)
		return(denoised)

	elif algorithm_denoise == 'bilateral':
		denoised = denoise_bilateral(image, sigma_color = sigma_color,
								 sigma_spatial = sigma_spatial)
		return(denoised)

	elif algorithm_denoise == 'wavelet':
		denoised = denoise_wavelet(image)
		return(denoised)

	else :
		print("Algorithme de denoising inconnu")
		return(image)

def binarisation(image, algorithm_binarisation=None, window_size=25, k=0.8):

	if algorithm_binarisation == 'otsu':
		binary = image > threshold_otsu(image)
		return(binary)

	elif algorithm_binarisation == 'niblack':
		thresh_niblack = threshold_niblack(image, window_size=window_size,
							 k=k)
		binary = image > thresh_niblack
		return(binary)

	elif algorithm_binarisation == 'sauvola':
		thresh_sauvola = threshold_sauvola(image, window_size=window_size)
		binary = image > thresh_sauvola
		return(binary)

	else :
		print("Algorithme de binarisation inconnu")
		return(image)

def export_result(image, path_export):

	io.imsave(path_export, img_as_uint(image))