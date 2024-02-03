import loopgpt

agent = loopgpt.Agent()

agent.name = "ResearchAI"

agent.description = """Google検索を使って最新の情報を取得して整理するAIアシスタントです。進捗、特に作成したファイルパスやファイル名を正しく報告します。ユーザの指示や支援なしに作業を完了します。"""

agent.goals = [
    "Googleで最新のスマホを検索する",
    "最高の評価を得ているプロダクト５つの価格と概要を書く。",
    "５つのプロダクトのpros and consをまとめて'summary.txt'を作る",
    "summary.txtの内容を読み取り、自己レビューして必要であれば修正する",
    "summary.txtの出力先のパスを報告する",
]

agent.cli()

agent.save("research_ai.json")
