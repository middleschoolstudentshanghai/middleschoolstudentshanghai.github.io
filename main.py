from flask import Flask, request, jsonify
import os
import time

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads/'  # 指定上传文件的保存目录

# 确保上传目录存在
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return app.send_static_file('index.html')  # 假设index.html位于static文件夹内

@app.route('/upload', methods=['POST'])
def upload_audio():
    audio_file = request.files.get('audio')
    if audio_file:
        # 生成唯一文件名，例如使用时间戳和UUID
        unique_filename = f"{int(time.time())}.webm"
        filepath = os.path.join(UPLOAD_FOLDER, unique_filename)
        audio_file.save(filepath)
        return jsonify({'message': f'文件上传成功，保存为{unique_filename}'})
    else:
        return jsonify({'error': '未接收到音频文件'}), 400

if __name__ == '__main__':
    app.run(debug=True)
