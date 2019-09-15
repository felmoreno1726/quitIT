from google_images_download import google_images_download  

response = google_images_download.googleimagesdownload() 

arguments = {"keywords":"image of man smoking in public, patio, public ashtrays ","limit":15,"print_urls":True}   #creating list of arguments
paths = response.download(arguments)   #passing the arguments to the function
print(paths)   #printing absolute paths of the downloaded images