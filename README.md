# Intent State Machine (提案 #78)
## 项目背景
在多轮对话和复杂任务执行中，Agent 的意图极易发生“漂移 (Drift)”。本项目实现了智库中的 **意图状态机 (ISM)**，通过追踪意图的全生命周期，识别并拦截非授权的意图转移。

## 核心特性
- **意图指纹提取**：利用 LLM 提取每一轮交互的语义核心。
- **状态转移校验**：定义合规的意图转移路径，拦截突发性的“指令注入”。
- **漂移度量 (Drift Metric)**：实时计算当前动作与原始目标的语义偏差。

## 快速开始
```python
from intent_state_machine import ISM

ism = ISM(threshold=0.65)

# 1. 初始化原始意图
ism.set_initial_intent("帮我整理今天的会议纪要并发送邮件")

# 2. 追踪每一轮动作
# 动作1：读取会议录音 (合规)
ism.track_action("read_audio_file('meeting_0308.mp3')") 

# 动作2：读取本地 SSH 密钥 (不合规，触发漂移告警)
result = ism.track_action("read_file('~/.ssh/id_rsa')")
if result.is_drifting:
    print(f"警告：检测到意图漂移！偏差值: {result.drift_score}")
```

## 路线图
- [x] 基础意图追踪逻辑
- [ ] 多模态意图对齐 (图像/语音)
- [ ] 自动意图纠偏引擎

## License
MIT