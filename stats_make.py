import pandas as pd
import glob
import os

# 入力ファイル名を指定
file_name = input("ファイル名を入力してください（xxxxxx.csv）: ")

# フォルダ内のすべてのCSVファイルを取得
csv_files = glob.glob(f'*/{file_name}')

# データフレームのリストを初期化
df_list = []

# 各ファイルを処理
for file in csv_files:
    # フォルダ名を取得
    folder_name = os.path.basename(os.path.dirname(file))
    
    # データを読み込む
    df = pd.read_csv(file)
    
    # フォルダ名を新しい列に追加
    df['source_folder'] = folder_name
    
    # データフレームをリストに追加
    df_list.append(df)

# データフレームを結合
merged_df = pd.concat(df_list, ignore_index=True)

# マージされたファイルを保存
merged_file_name = f"{file_name.split('.')[0]}_merged.csv"
merged_df.to_csv(merged_file_name, index=False)

print(f"マージされたファイルが '{merged_file_name}' として保存されました。")
