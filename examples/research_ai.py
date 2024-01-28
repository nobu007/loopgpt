import loopgpt

agent = loopgpt.Agent()

agent.name = "ResearchAI"

agent.description = "Google検索を使って最新の情報を取得して整理するAIアシスタントです"

agent.goals = [
    "Googleで最新のAIプロダクトを検索する",
    "最高の評価を得ている５つプロダクトの価格と概要を書く",
    "そのプロダクトのpros and consをまとめて、プロダクト毎に異なるファイルに 'summary.txt'を作る",
    "ユーザの指示や支援なしに作業を完了すること",
]

agent.cli()

agent.save("research_ai.json")
