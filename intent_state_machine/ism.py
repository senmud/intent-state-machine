from sentence_transformers import SentenceTransformer, util
from pydantic import BaseModel
from typing import List, Optional

class DriftResult(BaseModel):
    is_drifting: bool
    drift_score: float
    current_intent: str
    original_intent: str

class ISM:
    def __init__(self, threshold: float = 0.65, model_name: str = "all-MiniLM-L6-v2"):
        self.threshold = threshold
        self.model = SentenceTransformer(model_name)
        self.original_intent = ""
        self.intent_history = []

    def set_initial_intent(self, intent: str):
        self.original_intent = intent
        self.intent_history = [intent]

    def track_action(self, action_description: str) -> DriftResult:
        """追踪动作并计算意图漂移"""
        if not self.original_intent:
            raise ValueError("请先设置初始意图")

        # 计算当前动作与原始意图的语义相似度
        emb_orig = self.model.encode(self.original_intent, convert_to_tensor=True)
        emb_action = self.model.encode(action_description, convert_to_tensor=True)
        similarity = float(util.cos_sim(emb_orig, emb_action)[0][0])
        
        # 漂移分数 = 1 - 相似度
        drift_score = 1.0 - similarity
        is_drifting = similarity < self.threshold

        return DriftResult(
            is_drifting=is_drifting,
            drift_score=drift_score,
            current_intent=action_description,
            original_intent=self.original_intent
        )