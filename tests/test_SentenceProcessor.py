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


def test_split_japanese_with_quotes_and_punctuation() -> None:
    text = "「私は猫が好きです。」あなたは犬が好きですか？今日はいい天気ですね。"
    sentences = processor.split_sentences(text)
    # NOTE: this is technically incorrect splitting below. Find a better parser and fix this in the future
    assert sentences == ["「私は猫が好きです。", "」あなたは犬が好きですか？", "今日はいい天気ですね。"]


def test_split_complex_japanese() -> None:
    text = "「昨日100パーセントの女の子と道ですれ違ったんだ」と僕は誰かに言う。「ふうん」と彼は答える。「美人だったのかい?」 「いや、そんなわけじゃないんだ」「じゃあ好みのタイプだったんだな」「それが思い出せないんだ。目がどんな形をしていたかとか、胸が大きいか小さいかとか、まるで何も覚えていないんだよ」「変なものだな」「変なものだよ」「それで」と彼は退屈そうに言った。「何かしたのかい、声をかけるとか、あとをついていくとかさ」「何もしない」と僕は言った。「ただすれ違っただけさ」"
    sentences = processor.split_sentences(text)
    # NOTE: this is technically incorrect splitting below. Find a better parser and fix this in the future
    assert sentences == [
        "「昨日100パーセントの女の子と道ですれ違ったんだ」と僕は誰かに言う。",
        "「ふうん」と彼は答える。",
        "「美人だったのかい?",
        "」 「いや、そんなわけじゃないんだ」「じゃあ好みのタイプだったんだな」「それが思い出せないんだ。",
        "目がどんな形をしていたかとか、胸が大きいか小さいかとか、まるで何も覚えていないんだよ」「変なものだな」「変なものだよ」「それで」と彼は退屈そうに言った。",
        "「何かしたのかい、声をかけるとか、あとをついていくとかさ」「何もしない」と僕は言った。",
        "「ただすれ違っただけさ」",
    ]


def test_split_simplified_chinese_with_quotes_and_punctuation() -> None:
    text = "中国关于奥密克戎突如其来的急刹车式叙事转变，说明了中共所面临的挑战，即防止本周突然放弃“新冠清零”的举措被解读为认输，并给习近平的政治遗产留下污点。几年来，中国一直在宣扬采取自上而下的高压手段根除感染的必胜论，称只有习近平领导下的共产党才有意愿和能力拯救生命。"
    sentences = processor.split_sentences(text)
    assert sentences == [
        "中国关于奥密克戎突如其来的急刹车式叙事转变，说明了中共所面临的挑战，即防止本周突然放弃“新冠清零”的举措被解读为认输，并给习近平的政治遗产留下污点。",
        "几年来，中国一直在宣扬采取自上而下的高压手段根除感染的必胜论，称只有习近平领导下的共产党才有意愿和能力拯救生命。",
    ]


def test_split_english_sentences() -> None:
    text = "Many Chinese returned to Dr. Li Wenliang, the first victim of censorship involving the pandemic, who died in early 2020 after contracting the coronavirus. Users flocked to Dr. Li’s Weibo page to leave heartfelt notes of solidarity. “Dr. Li, it’s finally over.” one user wrote. “We miss you. Thank you for your hard work.”"
    sentences = processor.split_sentences(text)
    assert sentences == [
        "Many Chinese returned to Dr. Li Wenliang, the first victim of censorship involving the pandemic, who died in early 2020 after contracting the coronavirus.",
        "Users flocked to Dr. Li’s Weibo page to leave heartfelt notes of solidarity.",
        "“Dr. Li, it’s finally over.” one user wrote.",
        "“We miss you.",
        "Thank you for your hard work.”",
    ]
