# Analyze Endpoint

URL:
POST /analyze

Accepted Formats:
- JPG
- JPEG
- PNG

Success Response:

{
  "success": true,
  "prediction": "Fake",
  "confidence": 91.23
}

Error Response:

{
  "success": false,
  "error": "Invalid image format"
}