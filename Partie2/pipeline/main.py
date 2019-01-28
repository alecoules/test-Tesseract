import image_preprocess as impp 
import sys
import json

with open('parameters_preproc.json') as f:
    parameters = json.load(f)

#Import de l'image d'input
image_input = impp.import_image(parameters['path_image'])

#Application du denoising
if 'algorithm_denoise' in parameters.keys():
	if parameters['algorithm_denoise'] == 'tv_chambolle':
		denoised_image = impp.denoise(image_input,
			algorithm_denoise=parameters['algorithm_denoise'],
			weight=parameters['weight'])
	elif parameters['algorithm_denoise'] == 'bilateral':
		denoised_image = impp.denoise(image_input,
			algorithm_denoise=parameters['algorithm_denoise'],
			sigma_color=parameters['sigma_color'],
			sigma_spatial=parameters['sigma_spatial'])
	elif parameters['algorithm_denoise'] == 'wavelet':
		denoised_image = impp.denoise(image_input,
			algorithm_denoise=parameters['algorithm_denoise'])
	else:
		#Dans ce cas là on n'applique pas de denoising
		#"Algorithme de denoising inconnu" 
		#s'affiche dans le terminal
		print('pas de denoising')
		denoised_image = impp.denoise(image_input)
else:
	#Dans ce cas là on n'applique pas de denoising
	denoised_image = image_input

#Application de la binarisation
if 'algorithm_binarisation' in parameters.keys():
	if parameters['algorithm_binarisation'] == 'otsu':
		binary_image = impp.binarisation(denoised_image,
			algorithm_binarisation=parameters['algorithm_binarisation'])
	elif parameters['algorithm_binarisation'] == 'niblack':
		binary_image = impp.binarisation(denoised_image,
			algorithm_binarisation=parameters['algorithm_binarisation'],
			window_size=parameters['window_size'],
			k=parameters['k'])
	elif parameters['algorithm_binarisation'] == 'sauvola':
		binary_image = impp.binarisation(denoised_image,
			algorithm_binarisation=parameters['algorithm_binarisation'],
			window_size=parameters['window_size'])
	else:
		#Dans ce cas là on n'applique pas de denoising
		#"Algorithme de binarisation inconnu" 
		#s'affiche dans le terminal
		print('pas de binarisation')
		binary_image = impp.binarisation(denoised_image)
else:
	#Dans ce cas là on n'applique pas de binarisation
	binary_image = denoised_image

#Export de l'image prétraitée
impp.export_result(binary_image, parameters['path_export'])
