# AidemyのYOLO講座を通じてローカル環境に実行環境を作成するプロジェクトです。

## 物体検出とは？
![alt text](image.png)

## 導入までの流れ
1. Aidemyからデータセットを入手。カスタムデータセットならアノテーションする: https://dev-partner.i-pro.com/space/TPFAQ/1007060562/%E3%82%A2%E3%83%8E%E3%83%86%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E3%83%84%E3%83%BC%E3%83%AB%E3%80%8ElabelImg%E3%80%8F%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9FAI%E3%83%A2%E3%83%87%E3%83%AB%E4%BD%9C%E6%88%90
2. 仮想環境を作成
   ### ポイント！torchのインストール上手くいかないと次のステップにすすめない。
   1. importする際にosエラーdllファイルが見つからない。バージョン変更で解決(python3.12)
```
# 一度アンインストール
pip uninstall torch torchvision torchaudio

# バージョンを指定してインストール
pip install torch==2.3.1 torchvision==0.18.1 torchaudio==2.3.1

```
これも必要かもC++のやつ: https://learn.microsoft.com/ja-jp/cpp/windows/latest-supported-vc-redist?view=msvc-170
3. config.ipynbでコンフィグデータを作成
4. yolov8,ipynbで学習
5. 
