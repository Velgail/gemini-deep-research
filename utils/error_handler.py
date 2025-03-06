class ErrorHandler:
    """エラー処理管理クラス"""
    
    @staticmethod
    def handle_api_error(error, context=None):
        """
        APIエラーの処理
        
        Args:
            error: 発生したエラー
            context (str, optional): エラーが発生したコンテキスト
            
        Returns:
            str: エラーメッセージ
        """
        context_str = f" ({context})" if context else ""
        message = f"API接続エラー{context_str}: {str(error)}"
        print(message)
        return message
    
    @staticmethod
    def handle_plan_generation_error(error, topic=None):
        """
        計画生成エラーの処理
        
        Args:
            error: 発生したエラー
            topic (str, optional): 計画生成対象のトピック
            
        Returns:
            str: エラーメッセージ
        """
        topic_str = f"「{topic}」の" if topic else ""
        message = f"{topic_str}リサーチ計画生成中にエラーが発生しました: {str(error)}"
        print(message)
        return message
    
    @staticmethod
    def handle_execution_error(error, stage=None):
        """
        リサーチ実行エラーの処理
        
        Args:
            error: 発生したエラー
            stage (str, optional): エラーが発生したステージ
            
        Returns:
            str: エラーメッセージ
        """
        stage_str = f"「{stage}」ステージでの" if stage else ""
        message = f"リサーチ実行中に{stage_str}エラーが発生しました: {str(error)}"
        print(message)
        return message
    
    @staticmethod
    def log_error(error, file_path="error.log"):
        """
        エラーのログ記録
        
        Args:
            error: 記録するエラー
            file_path (str, optional): ログファイルのパス
        """
        import datetime
        import traceback
        
        try:
            with open(file_path, "a", encoding="utf-8") as f:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}] {str(error)}\n")
                f.write(traceback.format_exc())
                f.write("\n" + "-" * 50 + "\n")
        except Exception as e:
            print(f"ログの記録に失敗しました: {str(e)}")