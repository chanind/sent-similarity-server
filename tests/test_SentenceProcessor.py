from __future__ import annotations

from sent_similarity_server.SentenceProcessor import SentenceProcessor

processor = SentenceProcessor()


def test_split_japanese_sentence() -> None:
    text = "私は猫が好きです。あなたは犬が好きですか？今日はいい天気ですね。"
    sentences = processor.split_sentences(text)
    assert sentences == [
        "私は猫が好きです。",
        "あなたは犬が好きですか？",
        "今日はいい天気ですね。",
    ]


def test_split_english_sentences() -> None:
    text = "Many Chinese returned to Dr. Li Wenliang, the first victim of censorship involving the pandemic, who died in early 2020 after contracting the coronavirus. Users flocked to Dr. Li’s Weibo page to leave heartfelt notes of solidarity. “Dr. Li, it’s finally over.” one user wrote. “We miss you. Thank you for your hard work.”"
    sentences = processor.split_sentences(text)
    assert sentences == [
        "Many Chinese returned to Dr. Li Wenliang, the first victim of censorship involving the pandemic, who died in early 2020 after contracting the coronavirus.",
        "Users flocked to Dr. Li’s Weibo page to leave heartfelt notes of solidarity.",
        "“Dr. Li, it’s finally over.”",
        "one user wrote.",
        "“We miss you.",
        "Thank you for your hard work.”",
    ]
