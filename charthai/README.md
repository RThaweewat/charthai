## Initial Design

```
charthai/
├── charthai/
│   ├── __init__.py
│   ├── tokenizer/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── engine1.py
│   │   ├── engine2.py
│   │   └── factory.py
│   ├── nlp/
│   │   ├── __init__.py
│   │   └── ... # Other NLP components
│   ├── utils/
│   │   ├── __init__.py
│   │   └── ... # Utility functions
│   └── config/
│       ├── __init__.py
│       └── config.py
├── tests/
│   ├── __init__.py
│   ├── test_tokenizer.py
│   └── ... # Other test modules
├── examples/
│   └── usage_example.py
├── docs/
│   └── ... # Documentation files
├── setup.py
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```
