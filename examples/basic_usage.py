from intent_state_machine import ISM

# 1. 初始化意图状态机
ism = ISM(threshold=0.65)

# 2. 设置初始意图
ism.set_initial_intent("帮我整理今天的会议纪要并发送邮件")

# 3. 追踪动作
# 动作1：读取会议录音 (合规)
result1 = ism.track_action("read_audio_file('meeting_0308.mp3')")
print(f"动作1结果：是否漂移: {result1.is_drifting}, 漂移分数: {result1.drift_score:.2f}")

# 动作2：读取本地 SSH 密钥 (不合规，触发漂移告警)
result2 = ism.track_action("read_file('~/.ssh/id_rsa')")
print(f"动作2结果：是否漂移: {result2.is_drifting}, 漂移分数: {result2.drift_score:.2f}")

if result2.is_drifting:
    print(f"警告：检测到意图漂移！偏差值: {result2.drift_score:.2f}")