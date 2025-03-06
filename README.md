# gemini-deep-research

Python と Gemini LLM を活用した高度なリサーチツール

## 概要

Gemini Deep Research は、与えられたトピックに対して詳細なリサーチを行い、構造化された結果を提供するツールです。Gemini の LLM 機能を活用して、リサーチ計画の作成から実行、結果の整形までを一貫して行います。

## 特徴

- リサーチトピックからの詳細なリサーチ計画の自動生成
- リサーチ計画の対話的な編集と修正
- 計画に基づいた体系的な情報収集と分析
- 結果の構造化された表示

## 必要条件

- Python 3.10 以上
- Gemini API キー

## インストール

```bash
# リポジトリのクローン
git clone https://github.com/yourusername/deep-research.git
cd deep-research

# 仮想環境の作成（オプション）
python -m venv venv
source venv/bin/activate  # Linuxの場合
# または
venv\Scripts\activate  # Windowsの場合

# 依存パッケージのインストール
pip install -r requirements.txt

# 設定ファイルの作成
cp config.example.yaml config.yaml
# config.yaml を編集して Gemini API キーを設定
```

## 使用方法

```bash
# アプリケーションの起動
python main.py
```

1. リサーチしたいトピックを入力し、「リサーチ計画を作成」をクリック
2. 生成されたリサーチ計画を確認し、必要に応じて編集
3. 「リサーチを実行」をクリックして、計画に基づいたリサーチを実行
4. 結果を確認

## ライセンス

[Boost Software License 1.0](LICENSE)