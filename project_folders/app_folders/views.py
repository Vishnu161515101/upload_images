from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def upload_image(request):
    if request.method == 'POST' and 'images' in request.FILES:
        images = request.FILES.getlist('images')  # Use getlist() to handle multiple file uploads
        for image in images:
            # Handle each image file as needed (e.g., save to disk)
            destination_path = 'media/images/' + image.name  # Adjust path as needed
            with open(destination_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)
        # After successful upload, render the template with a success message or redirect to another URL
        return render(request, 'upload_images.html')
    
    # If not a POST request or no files uploaded, render the empty form template
    return render(request, 'upload_images.html')
