class GeminiBase:
    """Gemini APIの基本ラッパークラス"""
    
    def __init__(self, config):
        """
        初期化
        
        Args:
            config: 設定オブジェクト
        """
        self.config = config
        self.api_key = config.get("gemini_api_key")
        self.client = None
    
    def _initialize_client(self):
        """
        Gemini APIクライアントの初期化
        
        Returns:
            API クライアントオブジェクト
        """
        # PR-2で実装予定
        pass
    
    def _validate_api_key(self):
        """
        APIキーの検証
        
        Returns:
            bool: APIキーが有効かどうか
        """
        if not self.api_key:
            print("APIキーが設定されていません。config.yamlまたは環境変数GEMINI_API_KEYを設定してください。")
            return False
        return True