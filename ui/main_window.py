from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QGroupBox, QTextEdit, QPushButton, QHBoxLayout, QStatusBar, QMessageBox, QInputDialog

class DeepResearchUI(QMainWindow):
    """Deep Researchのメインユーザーインターフェース"""
    
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()
        
    def init_ui(self):
        """UIの初期化"""
        # ウィンドウタイトル、サイズ設定
        self.setWindowTitle('Deep Research')
        self.setGeometry(100, 100, 1200, 800)
        
        # 中央ウィジェット
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # メインレイアウト
        main_layout = QVBoxLayout(central_widget)
        
        # トピック入力エリア
        topic_group = QGroupBox("リサーチトピック")
        topic_layout = QVBoxLayout(topic_group)
        
        self.topic_input = QTextEdit()
        self.topic_input.setPlaceholderText("リサーチしたいトピックを入力してください...")
        
        self.submit_topic_btn = QPushButton("リサーチ計画を作成")
        self.submit_topic_btn.clicked.connect(self.on_submit_topic)
        
        topic_layout.addWidget(self.topic_input)
        topic_layout.addWidget(self.submit_topic_btn)
        
        # 計画表示・編集エリア
        plan_group = QGroupBox("リサーチ計画")
        plan_layout = QVBoxLayout(plan_group)
        
        self.plan_editor = QTextEdit()
        self.plan_editor.setReadOnly(False)
        
        btn_layout = QHBoxLayout()
        self.revise_plan_btn = QPushButton("計画を修正")
        self.revise_plan_btn.clicked.connect(self.on_revise_plan)
        
        self.execute_research_btn = QPushButton("リサーチを実行")
        self.execute_research_btn.clicked.connect(self.on_execute_research)
        
        btn_layout.addWidget(self.revise_plan_btn)
        btn_layout.addWidget(self.execute_research_btn)
        
        plan_layout.addWidget(self.plan_editor)
        plan_layout.addLayout(btn_layout)
        
        # 結果表示エリア
        results_group = QGroupBox("リサーチ結果")
        results_layout = QVBoxLayout(results_group)
        
        self.results_display = QTextEdit()
        self.results_display.setReadOnly(True)
        
        results_layout.addWidget(self.results_display)
        
        # 状態表示エリア
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        
        # レイアウトの組み立て
        main_layout.addWidget(topic_group, 1)
        main_layout.addWidget(plan_group, 2)
        main_layout.addWidget(results_group, 3)
        
        # 初期状態設定
        self.plan_editor.setEnabled(False)
        self.revise_plan_btn.setEnabled(False)
        self.execute_research_btn.setEnabled(False)
    
    def on_submit_topic(self):
        """トピック送信時の処理"""
        topic = self.topic_input.toPlainText().strip()
        if not topic:
            QMessageBox.warning(self, "入力エラー", "リサーチトピックを入力してください。")
            return
            
        self.status_bar.showMessage("リサーチ計画を生成中...")
        # 非同期処理
        # 完了したら self.display_research_plan(plan) を呼び出す
        
    def display_research_plan(self, plan):
        """リサーチ計画の表示"""
        self.plan_editor.setPlainText(plan)
        self.plan_editor.setEnabled(True)
        self.revise_plan_btn.setEnabled(True)
        self.execute_research_btn.setEnabled(True)
        self.status_bar.showMessage("リサーチ計画が生成されました。編集または実行できます。")
        
    def on_revise_plan(self):
        """計画修正ボタン押下時の処理"""
        # ユーザーが編集した計画を取得
        revised_plan = self.plan_editor.toPlainText()
        
        # 修正理由の入力ダイアログ（オプション）
        reason, ok = QInputDialog.getText(
            self, "計画修正", "修正の理由や指示があれば入力してください（任意）:"
        )
        
        if ok:  # キャンセルされなかった場合
            self.status_bar.showMessage("計画を再評価中...")
            # 非同期処理で計画の修正を実行
            # 完了したら self.display_research_plan(refined_plan) を呼び出す
        
    def on_execute_research(self):
        """リサーチ実行ボタン押下時の処理"""
        approved_plan = self.plan_editor.toPlainText()
        
        self.status_bar.showMessage("リサーチを実行中...")
        # 非同期処理でリサーチを実行
        # 完了したら self.display_research_results(results) を呼び出す
        
    def display_research_results(self, results):
        """リサーチ結果の表示"""
        self.results_display.setPlainText(results)
        self.status_bar.showMessage("リサーチが完了しました。")