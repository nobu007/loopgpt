from loopgpt.tools.agent_manager import (
    CreateAgent,
    DeleteAgent,
    ListAgents,
    MessageAgent,
)
from loopgpt.tools.base_tool import BaseTool
from loopgpt.tools.browser import Browser
from loopgpt.tools.code import ExecutePythonFile, ImproveCode, ReviewCode, WriteTests
from loopgpt.tools.filesystem import (
    AppendToFile,
    CheckIfFileExists,
    DeleteFile,
    FileSystemTools,
    GetCWD,
    ListFiles,
    MakeDirectory,
    ReadFromFile,
    WriteToFile,
)
from loopgpt.tools.google_search import GoogleSearch
from loopgpt.tools.math import EvaluateMath
from loopgpt.tools.memory_manager import AddToMemory
from loopgpt.tools.shell import Shell
from loopgpt.tools.user_manager import AskUser

user_tools = {}


def register_tool_type(tool):
    if isinstance(tool, BaseTool):
        tool = tool.__class__
    if not isinstance(tool, type):
        raise TypeError(f"{tool} is not a class")
    if not issubclass(tool, BaseTool):
        raise TypeError(f"{tool} does not inherit from BaseTool")
    user_tools[tool.__name__] = tool


def from_config(config) -> BaseTool:
    class_name = config["class"]
    clss = user_tools.get(class_name) or globals()[class_name]
    return clss.from_config(config)


def builtin_tools():
    return [
        GoogleSearch,
        Browser,
        CreateAgent,
        MessageAgent,
        ListAgents,
        DeleteAgent,
        *FileSystemTools,
        ReviewCode,
        ImproveCode,
        WriteTests,
        ExecutePythonFile,
        EvaluateMath,
        AskUser,
        Shell,
    ]


def research_tools():
    return [
        GoogleSearch,
        Browser,
        Shell,
        *FileSystemTools,
    ]


def report_tools():
    return [
        GoogleSearch,
        Browser,
        Shell,
        *FileSystemTools,
    ]
