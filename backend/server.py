from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import yt_dlp
import os

app = Flask(__name__)
CORS(app)

@app.route('/download', methods=['POST'])
def download_video():
    data = request.get_json()
    url = data.get('url')
    format = data.get('format', 'mp4')
    quality = data.get('quality', 'best')

    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    # Set options for yt-dlp
    ydl_opts = {
        'format': quality,
        'outtmpl': 'downloads/video.%(ext)s',  # Save to a temporary location
        'quiet': True  # Suppress output
    }

    try:
        # Download the video using yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_filename = ydl.prepare_filename(info_dict)

            # Serve the file as a downloadable response
            return send_file(
                video_filename, 
                as_attachment=True, 
                download_name=f"video.{format}", 
                mimetype='video/mp4'
            )
    except Exception as e:
        return jsonify({'error': f'Failed to download video: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
