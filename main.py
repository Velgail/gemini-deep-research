import sys
import asyncio
from config import Config
from core.controller import CoreController
from ui.main_window import DeepResearchUI
from PyQt6.QtWidgets import QApplication

def main():
    """アプリケーションのメインエントリーポイント"""
    # 設定の読み込み
    config = Config()
    
    # APIキーの検証
    if not config.get("gemini_api_key"):
        print("警告: Gemini APIキーが設定されていません。")
        print("config.yamlファイルまたは環境変数GEMINI_API_KEYを設定してください。")
    
    # コアコントローラーの初期化
    controller = CoreController(config)
    
    # UIの初期化と表示
    app = QApplication(sys.argv)
    window = DeepResearchUI(controller)
    window.show()
    
    # アプリケーションの実行
    sys.exit(app.exec())

if __name__ == "__main__":
    main()