import speech_recognition as sr
import re

# 语义连贯性评估框架(没有一行代码是可靠的~)
def analyze_coherence(speech_file_path:str):
    # 初始化识别器
    recognizer = sr.Recognizer()

    # 读取语音文件
    with sr.AudioFile(speech_file_path) as source:
        audio_data = recognizer.record(source)
    
    try:
        # 识别语音
        text = recognizer.recognize_google(audio_data)
        print("识别的文本: " + text)
        
        # 简单的连贯性评估规则：
        # 1. 检查是否有完整的句子结构（主语+谓语）
        # 2. 检查是否有常见的连接词
        # 3. 检查是否有重复的词汇或短语
        # 这些规则是非常基础的，实际应用中需要更复杂的模型和算法

        # 检查句子结构
        sentences = re.split(r'(?<=[.!?]) +', text)
        has_complete_structure = all(re.search(r'\b(?:[A-Z][a-z]*\b) [^.!?]* [.!?]', sentence) for sentence in sentences)
        
        # 检查连接词
        conjunctions = ['and', 'but', 'or', 'so', 'for', 'nor', 'yet', 'after', 'although', 'since', 'if', 'because', 'as', 'until']
        has_conjunctions = any(conj in text.lower() for conj in conjunctions)
        
        # 检查重复词汇
        words = text.lower().split()
        has_repetition = len(words) != len(set(words))
        
        # 根据规则计算连贯性评分
        coherence_score = 1  # 基础分
        if has_complete_structure:
            coherence_score += 0.5
        if has_conjunctions:
            coherence_score += 0.3
        if not has_repetition:
            coherence_score += 0.2
        
        return coherence_score
    
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None

# 示例：分析一个语音文件
speech_file_path = 'your_speech_file.wav'
coherence_score = analyze_coherence(speech_file_path)
print(f"连贯性评分: {coherence_score}")