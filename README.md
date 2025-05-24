# Cloudinary Uploader

A secure and flexible Python tool to upload images, videos, and documents to [Cloudinary](https://cloudinary.com/) with:

- **Automatic file type detection** based on file extension  
- **Support for images, videos, and raw files** (e.g., PDFs, docs)  
- **Signed URL generation** for private/raw assets to ensure secure access  
- **Environment variable configuration** for credentials using `.env` files  

---

## Features

- Automatically detects file type and uploads accordingly (`image`, `video`, or `raw`).  
- Generates secure URLs for public assets and signed URLs for private/raw assets.  
- Simple to configure with environment variables for API key, secret, and cloud name.  
- Easy to extend or integrate into existing Python projects.

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/nileshyadav12/cloudinary_uploader.git
   cd cloudinary_uploader
