import os

DEFAULT_CONFIG = {
    "project_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
    "results_dir": os.getenv("TRADINGAGENTS_RESULTS_DIR", "./results"),
    #"data_dir": "/Users/yluo/Documents/Code/ScAI/FR1-data",
    "data_dir": "D:\\Project\\antigravity_workspace\\_data\\TradingAgents\\data",   
    "data_cache_dir": os.path.join(
        os.path.abspath(os.path.join(os.path.dirname(__file__), ".")),
        "dataflows/data_cache",
    ),
    # LLM settings
    # "llm_provider": "openai",
    # "deep_think_llm": "o4-mini",
    # "quick_think_llm": "gpt-4o-mini",
    # "backend_url": "https://api.openai.com/v1",

    "llm_provider": "google",
    "deep_think_llm": "gemini-2.5-flash",
    "quick_think_llm": "gemini-2.5-flash",
    "backend_url": "https://generativelanguage.googleapis.com/v1beta",
    
    # "llm_provider": "ollama",
    # "deep_think_llm": "huihui_ai/deepseek-r1-abliterated:14b",
    # "quick_think_llm": "qwen3:14b",
    # "backend_url": "http://localhost:11434/v1",

    # Debate and discussion settings
    "max_debate_rounds": 1,
    "max_risk_discuss_rounds": 1,
    "max_recur_limit": 100,
    # Data vendor configuration
    # Category-level configuration (default for all tools in category)
    "data_vendors": {
        "core_stock_apis": "yfinance",       # Options: yfinance, alpha_vantage, local
        "technical_indicators": "yfinance",  # Options: yfinance, alpha_vantage, local
        "fundamental_data": "alpha_vantage", # Options: openai, alpha_vantage, local
        "news_data": "alpha_vantage",        # Options: openai, alpha_vantage, google, local
    },
    # Tool-level configuration (takes precedence over category-level)
    "tool_vendors": {
        # Example: "get_stock_data": "alpha_vantage",  # Override category default
        # Example: "get_news": "openai",               # Override category default
    },
}
