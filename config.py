import os
import yaml
from dotenv import load_dotenv

class Config:
    """Deep Research の設定管理クラス"""
    
    def __init__(self, config_file="config.yaml"):
        # 環境変数の読み込み
        load_dotenv()
        
        # デフォルト設定
        self.default_config = {
            "gemini_api_key": os.getenv("GEMINI_API_KEY", ""),
            "models": {
                "flash": "gemini-2.0-flash",
                "thinking": "gemini-2.0-flash-thinking"
            },
            "research": {
                "max_search_results": 10,
                "max_depth": 3,
                "max_tokens_per_request": 8000
            },
            "ui": {
                "font_size": 11,
                "theme": "system"
            }
        }
        
        # 設定ファイルからの読み込み
        self.config = self.default_config.copy()
        self.load_from_file(config_file)
    
    def load_from_file(self, config_file):
        """設定ファイルから読み込み"""
        try:
            if os.path.exists(config_file):
                with open(config_file, 'r', encoding='utf-8') as f:
                    file_config = yaml.safe_load(f)
                    if file_config:
                        self._update_nested_dict(self.config, file_config)
        except Exception as e:
            print(f"設定ファイルの読み込みに失敗しました: {str(e)}")
    
    def _update_nested_dict(self, d, u):
        """ネストされた辞書の更新"""
        for k, v in u.items():
            if isinstance(v, dict) and k in d and isinstance(d[k], dict):
                self._update_nested_dict(d[k], v)
            else:
                d[k] = v
    
    def get(self, key, default=None):
        """設定値の取得 (ドット記法対応)"""
        parts = key.split('.')
        current = self.config
        
        for part in parts:
            if part not in current:
                return default
            current = current[part]
        
        return current
    
    def set(self, key, value):
        """設定値の設定 (ドット記法対応)"""
        parts = key.split('.')
        current = self.config
        
        for i, part in enumerate(parts[:-1]):
            if part not in current:
                current[part] = {}
            current = current[part]
        
        current[parts[-1]] = value
    
    def save(self, config_file="config.yaml"):
        """設定ファイルへの保存"""
        try:
            with open(config_file, 'w', encoding='utf-8') as f:
                yaml.dump(self.config, f, default_flow_style=False)
                return True
        except Exception as e:
            print(f"設定ファイルの保存に失敗しました: {str(e)}")
            return False