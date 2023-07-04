import os

def replace_string_in_html_files(folder_path, old_string, new_string, encodings):
    # フォルダ内の全てのファイルを走査
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                # 各エンコーディングでファイルを試す
                for encoding in encodings:
                    try:
                        with open(file_path, 'r', encoding=encoding) as f:
                            content = f.read()
                        content = content.replace(old_string, new_string)
                        with open(file_path, 'w', encoding=encoding) as f:
                            f.write(content)
                        print(f'Replaced in: {file_path}')
                        break  # 正常に処理された場合はループを終了
                    except UnicodeDecodeError:
                        continue
                    except Exception as e:
                        print(f'Error processing file: {file_path} ({e})')

# 使用例
folder_path = 'C:/Users/joly1/Downloads/新しいフォルダー/tp_haken1_i_orange'  # 対象のフォルダのパスを指定
old_string = '<body>'      # 置換前の文字列を指定
new_string = '<body>\nVVVVVV'      # 置換後の文字列を指定

# 使用するエンコーディングのリストを指定
encodings = ['utf-8', 'latin-1', 'shift-jis']

replace_string_in_html_files(folder_path, old_string, new_string, encodings)
