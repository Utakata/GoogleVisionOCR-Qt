# GoogleVisionOCR

高品質OCRアプリケーション - ScanSnapとKindleファイルの変換ツール

## 概要

GoogleVisionOCRは、スキャンされたPDFやKindleのEPUBファイルからテキストを抽出し、検索可能な形式に変換するデスクトップアプリケーションです。Google Cloud Vision APIを使用して高精度なOCR処理を行い、日本語の縦書きテキストにも対応しています。

## 機能

- ScanSnapから取り込んだPDFの高品質OCR処理
- KindleのEPUBファイルからのテキスト抽出
- 画質を維持したままのOCR処理
- 縦書きテキスト対応
- モダンなUI/UXデザイン

## スクリーンショット

![メイン画面](docs/images/screenshot-main.png)

## 技術スタック

- GUI: Qt6
- OCRエンジン: Google Cloud Vision API
- 開発言語: Python
- パッケージ管理: PIP / venv
- ビルドツール: PyInstaller

## インストール

### 必要条件

- Python 3.8以上
- Qt6
- Google Cloud Visionアカウントとキー（APIキーの取得方法は[Google Cloudのドキュメント](https://cloud.google.com/vision/docs/setup)を参照）

```bash
# 依存パッケージのインストール
pip install -r requirements.txt

# 実行
python -m src.main
```

## 使用方法

1. アプリケーションを起動
2. 「参照」ボタンからPDFまたはEPUBファイルを選択
3. OCR設定（縦書き/横書き、品質など）を調整
4. 「OCR処理を開始」ボタンをクリック
5. 処理完了後、「結果をエクスポート」ボタンで保存

## 設定

- **言語**: 日本語/英語/自動検出
- **テキスト方向**: 縦書き/横書き
- **品質**: 低/中/高（処理速度と精度のバランス）
- **出力形式**: 検索可能PDF/テキストファイル/HTMLファイル

## ライセンス

このプロジェクトはオープンソースで公開されています。

## 開発者

- Shohei (@Utakata)

## 謝辞

- [Google Cloud Vision API](https://cloud.google.com/vision)
- [Qt Project](https://www.qt.io/)
- [PyQt](https://riverbankcomputing.com/software/pyqt/)
