import openai
import os

# APIキーの設定
openai.api_key = os.environ["OPENAI_API_KEY"]

input_text = input("チェックしたい文章を入力してください。")

# GPTによる応答生成
prompt = f"以下の入力文を評価の上、必要であれば改善・訂正した文章とともに出力せよ。入力文：{input_text}"
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k-0613",
    messages=[
        {"role": "system", "content": "文法的且つ意味的に正しいかを点数で評価、最高は100点で最低は0点"},
        {"role": "system", "content": "もし訂正点または改善点がある場合は、訂正・改善済みの文章も併せて出力"},
        {"role": "system", "content": "『点数：「訂正・改善文」とするとより良いでしょう』この形式で出力"},
        {"role": "user", "content": prompt},
    ],
    temperature=0,
)

# 応答の表示
text = response["choices"][0]["message"]["content"]
print(text)