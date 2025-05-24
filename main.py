import os
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from dotenv import load_dotenv

# 🔐 Load environment variables from .env file
load_dotenv()

class CloudinaryUploader:
    def __init__(self):
        self.configure()

    def configure(self):
        """
        Configures Cloudinary using environment variables for security.
        """
        cloudinary.config(
            cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
            api_key=os.getenv("CLOUDINARY_API_KEY"),
            api_secret=os.getenv("CLOUDINARY_API_SECRET"),
            secure=True
        )

    def detect_file_type(self, file_path):
        """
        Detects and returns the appropriate Cloudinary resource_type based on file extension.
        """
        ext = os.path.splitext(file_path)[1].lower()
        if ext in ['.jpg', '.jpeg', '.png', '.webp']:
            return "image"
        elif ext in ['.mp4', '.mov', '.avi', '.mkv', '.wav', '.mp3']:
            return "video"
        elif ext in ['.pdf', '.docx', '.txt', '.csv', '.zip']:
            return "raw"
        else:
            return "auto"

    def upload_file(self, file_path):
        """
        Uploads a file to Cloudinary and returns a secure or signed URL.
        """
        if not os.path.exists(file_path):
            print("❌ File not found.")
            return None

        resource_type = self.detect_file_type(file_path)

        try:
            response = cloudinary.uploader.upload(file_path, resource_type=resource_type)
            public_id = response.get("public_id")

            if resource_type == "raw":
                # Generate signed URL for secure access
                signed_url, _ = cloudinary_url(
                    public_id,
                    resource_type="raw",
                    type="upload",
                    sign_url=True
                )
                print(f"✅ Uploaded (raw/pdf): {signed_url}")
                return signed_url
            else:
                secure_url = response.get("secure_url")
                print(f"✅ Uploaded ({resource_type}): {secure_url}")
                return secure_url

        except Exception as e:
            print(f"❌ Upload failed: {str(e)}")
            return None


# 🎯 Example usage
if __name__ == "__main__":
    uploader = CloudinaryUploader()
    file_path = r"C:\Users\Deepak\Desktop\changes\Cv__nilesh.pdf"
    uploader.upload_file(file_path)


