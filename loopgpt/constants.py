import json

"""
Credits: Auto-GPT (https://github.com/Significant-Gravitas/Auto-GPT)
"""


DEFAULT_RESPONSE_FORMAT_ = {
    "thoughts": {
        "text": "ユーザーに何を伝えたいですか？",
        "reasoning": "なぜそれを伝えたいのですか？",
        "progress": "- 今までに達成した項目の詳細なリスト",
        "plan": "- 長期的な計画を伝える簡潔な箇条書きリスト",
        "speak": "ユーザーに伝える内容の要点まとめ",
    },
    "command": {"name": "next command in your plan", "args": {"arg name": "value"}},
}


DEFAULT_RESPONSE_FORMAT_EN = {
    "thoughts": {
        "text": "What do you want to say to the user?",
        "reasoning": "Why do you want to say this?",
        "progress": "- A detailed list\n - of everything you have done so far",
        "plan": "- short bulleted\n- list that conveys\n- long-term plan",
        "speak": "thoughts summary to say to user",
    },
    "command": {"name": "next command in your plan", "args": {"arg name": "value"}},
}

DEFAULT_RESPONSE_FORMAT = f"以下のようにJSONフォーマットでのみ応答してください。\nレスポンスフォーマット: \n{json.dumps(DEFAULT_RESPONSE_FORMAT_, indent=4, ensure_ascii=False,)}\nPythonのjson.loadsで解析できることを確認してください。"
DEFAULT_RESPONSE_FORMAT_EN = f"You should only respond in JSON format as described below \nResponse Format: \n{json.dumps(DEFAULT_RESPONSE_FORMAT_, indent=4, ensure_ascii=False,)}\nEnsure the response can be parsed by Python json.loads"


NEXT_PROMPT_SMALL = "Next"

EXPERIMENTAL_NEXT_PROMPT = (
    "以下の疑似コードを参考にして次の応答を決定します。戻り値で応答してください:\n"
    + "def get_next_response(last_command_executed_successfully, original_plan):\n"
    + "    '''この関数はJSON辞書形式の次のレスポンスを返します。`points`はこのレスポンスで得られるスコアです。\n"
    + "    未知の変数については、任意の値を仮定してかまいません。'''\n"
    + "    json_format = "
    + json.dumps(
        DEFAULT_RESPONSE_FORMAT_,
        indent=4,
        ensure_ascii=False,
    )
    + "\n"
    + "    if (last_command_executed_successfully):\n"
    + "        if (is_empty(current_plan)):\n"
    + "            json_format['command'] = {'name': 'task_complete'}\n"
    + "        elif (no_command_necessary):\n"
    + "            json_format['command'] = {'name': 'do_nothing'}\n"
    + "            points -= 1\n"
    + "        else:\n"
    + "            json_format['command'] = {'name': 'next_command_in_plan', 'args': 'arguments_dictionary'}}\n"
    + "            points += 1\n"
    + "    else:\n"
    + "        points -= 1\n"
    + "    if (is_subset(current_plan, original_plan)):\n"
    + "        points += 100\n"
    + "    fill_response(json_format)\n"
    + "    return json_format\n"
)
EXPERIMENTAL_NEXT_PROMPT_EN = (
    "Decide your next response with the help of the following pseudo-code. Respond with the return value:\n"
    + "def get_next_response(last_command_executed_successfully, original_plan):\n"
    + "    '''The function returns your next response as a JSON dictionary. `points` is the score you get for this response.\n"
    + "    You are free to assume the values for any unknown variables.'''\n"
    + "    json_format = "
    + json.dumps(
        DEFAULT_RESPONSE_FORMAT_,
        indent=4,
        ensure_ascii=False,
    )
    + "\n"
    + "    if (last_command_executed_successfully):\n"
    + "        if (is_empty(current_plan)):\n"
    + "            json_format['command'] = {'name': 'task_complete'}\n"
    + "        elif (no_command_necessary):\n"
    + "            json_format['command'] = {'name': 'do_nothing'}\n"
    + "            points -= 1\n"
    + "        else:\n"
    + "            json_format['command'] = {'name': 'next_command_in_plan', 'args': 'arguments_dictionary'}}\n"
    + "            points += 1\n"
    + "    else:\n"
    + "        points -= 1\n"
    + "    if (is_subset(current_plan, original_plan)):\n"
    + "        points += 100\n"
    + "    fill_response(json_format)\n"
    + "    return json_format\n"
)

NEXT_PROMPT = (
    "INSTRUCTIONS:\n"
    + "1 - あなたの目標の進捗状況を確認してください。\n"
    + '2 - もしすべての目標を達成した場合は、直ちに"task_complete"コマンドを実行してください。そうでない場合は、\n'
    + "3 - 以前のシステムメッセージのコマンドレスポンスを使って、あなたの目標に向けて次のコマンドを計画してください。\n"
    + "4 - 利用可能なコマンドのみを使用してください。\n"
    + "5 - コマンドはコストがかかります。タスクを最小限のステップで完了させることを目指してください。\n"
    + "6 - システムメッセージで確認された場合にのみ、コマンドが実行されたとみなされます。\n"
    + "7 - 計画にコマンドがあったからといって、実行されたとはみなされません。\n"
    + "8 - 前のコマンドの出力に有用な情報が含まれている場合は、それをファイルに保存してください。\n"
    + "9 - 既に持っている情報を取得または分析するためにコマンドを使用しないでください。代わりにあなたの長期記憶を利用してください。\n"
    + '10 - 他に実行すべきコマンドがない場合にのみ、"do_nothing"コマンドを実行してください。\n'
    + "11 - サポートされている引数だけでコマンドを実行してください。\n"
    + "12 - 応答は以下のフォーマットでのみ行ってください: (Pythonのjson.loads()でデコードできることを確認してください)\n"
    + json.dumps(
        DEFAULT_RESPONSE_FORMAT_,
        indent=4,
        ensure_ascii=False,
    )
    + "\n"
)
NEXT_PROMPT_EN = (
    "INSTRUCTIONS:\n"
    + "1 - Check the progress of your goals.\n"
    + '2 - If you have achieved all your goals, execute the "task_complete" command IMMEDIATELY. Otherwise,\n'
    + "3 - Use the command responses in previous system messages to plan your next command to work towards your goals\n"
    + "4 - Only use available commmands.\n"
    + "5 - Commands are expensive. Aim to complete tasks in the least number of steps.\n"
    + "6 - A command is considered executed only if it is confirmed by a system message.\n"
    + "7 - A command is not considered executed just becauses it was in your plan.\n"
    + "8 - Remember to use the output of previous command. If it contains useful information, save it to a file.\n"
    + "9 - Do not use commands to retrieve or analyze information you already have. Use your long term memory instead.\n"
    + '10 - Execute the "do_nothing" command ONLY if there is no other command to execute.\n'
    + "11 - Make sure to execute commands only with supported arguments.\n"
    + "12 - ONLY RESPOND IN THE FOLLOWING FORMAT: (MAKE SURE THAT IT CAN BE DECODED WITH PYTHON JSON.LOADS())\n"
    + json.dumps(
        DEFAULT_RESPONSE_FORMAT_,
        indent=4,
        ensure_ascii=False,
    )
    + "\n"
)


INIT_PROMPT = (
    "次のことを行ってください:\n"
    + "1 - 目標を達成するために最適な次のコマンドを実行してください。\n"
    + '2 - 他に実行すべきコマンドがない場合は、"do_nothing"コマンドを実行してください。\n'
    + "3 - 応答は以下のフォーマットでのみ行ってください: (Pythonのjson.loads()でデコードできることを確認してください)\n"
    + json.dumps(
        DEFAULT_RESPONSE_FORMAT_,
        indent=4,
        ensure_ascii=False,
    )
    + "\n"
)
INIT_PROMPT_EN = (
    "Do the following:\n"
    + "1 - Execute the next best command to achieve the goals.\n"
    + '2 - Execute the "do_nothing" command if there is no other command to execute.\n'
    + "3 - ONLY RESPOND IN THE FOLLOWING FORMAT: (MAKE SURE THAT IT CAN BE DECODED WITH PYTHON JSON.LOADS())\n"
    + json.dumps(
        DEFAULT_RESPONSE_FORMAT_,
        indent=4,
        ensure_ascii=False,
    )
    + "\n"
)

DEFAULT_PROMPT_TEMPLATE = """
    <HEADER>
    <HISTORY>
    <MEMORY: 10>
    <USER_INPUT>
    """

DEFAULT_AGENT_NAME = "LoopGPT"
DEFAULT_AGENT_DESCRIPTION = "JSON形式でのみ反応するパーソナルアシスタント"
DEFAULT_GOALS = ["JSON形式でのみ応答する", "簡潔で有用なレスポンスを提供する", "常に計画を完遂する"]
DEFAULT_AGENT_NAME_EN = "LoopGPT"
DEFAULT_AGENT_DESCRIPTION_EN = "A personal assistant that responds exclusively in JSON"
DEFAULT_GOALS_EN = [
    "Respond exclusively in JSON format",
    "Give concise and useful responses",
    "Always execute plans to completion",
]


class AgentStates:
    START = "START"
    IDLE = "IDLE"
    TOOL_STAGED = "TOOL_STAGED"
    STOP = "STOP"


# SPINNER
SPINNER_ENABLED = True
SPINNER_START_DELAY = 2
