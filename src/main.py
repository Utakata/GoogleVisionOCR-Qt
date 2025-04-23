#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GoogleVisionOCR - メインアプリケーション
ScanSnap PDFやKindle EPUBファイルからのOCR処理アプリケーション
"""

import sys
import os
import argparse
from pathlib import Path

# プロジェクトルートをPythonパスに追加
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

# Qt関連のインポート
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import QTranslator, QLocale, QLibraryInfo

# 内部モジュールのインポート
from src.ui.main_window import MainWindow
from src.utils.config import Config
from src.utils.logger import setup_logger

def parse_arguments():
    """コマンドライン引数をパース"""
    parser = argparse.ArgumentParser(description='GoogleVisionOCR - PDF/EPUB OCRアプリケーション')
    parser.add_argument('file', nargs='?', help='OCR処理するファイルパス')
    parser.add_argument('--debug', action='store_true', help='デバッグモードを有効化')
    parser.add_argument('--version', action='store_true', help='バージョン情報を表示して終了')
    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
                        default='INFO', help='ログレベルを設定')
    
    return parser.parse_args()

def main():
    """アプリケーションのメインエントリポイント"""
    # コマンドライン引数をパース
    args = parse_arguments()
    
    # バージョン情報の表示
    if args.version:
        print("GoogleVisionOCR バージョン 1.0.0")
        return 0
    
    # ログレベルの設定
    import logging
    log_level = getattr(logging, args.log_level)
    
    # ロガーのセットアップ
    logger = setup_logger(log_level=log_level)
    logger.info("アプリケーションを起動しています...")
    
    # デバッグモードの設定
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("デバッグモードが有効化されました")
    
    # 設定の読み込み
    config = Config()
    config.load()
    
    # QApplication インスタンスの作成
    app = QApplication(sys.argv)
    app.setApplicationName("GoogleVisionOCR")
    app.setApplicationVersion("1.0.0")
    app.setOrganizationName("Shohei")
    app.setOrganizationDomain("shoheisoftware.com")
    
    # スタイルシートの設定（ファイルが存在する場合）
    style_path = os.path.join(project_root, "src", "ui", "resources", "style.qss")
    if os.path.exists(style_path):
        with open(style_path, "r", encoding="utf-8") as f:
            style_sheet = f.read()
            app.setStyleSheet(style_sheet)
    
    # 日本語翻訳ファイルの読み込み (存在する場合)
    translator = QTranslator()
    translations_path = QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    if translator.load(QLocale.system(), "qtbase", "_", translations_path):
        app.installTranslator(translator)
    
    # メインウィンドウの作成と表示
    main_window = MainWindow(config)
    
    # コマンドライン引数でファイルが指定されている場合は開く
    if args.file:
        file_path = Path(args.file).resolve()
        if file_path.exists():
            # ファイルを開く処理はMainWindowクラス内のメソッドを呼び出す
            main_window.open_file(str(file_path))
    
    main_window.show()
    
    # アプリケーションの実行
    exit_code = app.exec()
    
    # 設定の保存
    config.save()
    
    # 終了ログ
    logger.info(f"アプリケーションが終了しました。終了コード: {exit_code}")
    
    return exit_code

if __name__ == "__main__":
    sys.exit(main())
