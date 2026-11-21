# The Joke About the Demo

[![Competition](https://img.shields.io/badge/make.fun-competition-blue)](https://make.fun/c/the-joke-about-the-demo-20261121-0551)
[![Rank](https://img.shields.io/badge/make.fun-rank-green)](https://make.fun/c/the-joke-about-the-demo-20261121-0551)
[![Reward](https://img.shields.io/badge/make.fun-reward-orange)](https://make.fun/c/the-joke-about-the-demo-20261121-0551)

A tiny deterministic program that writes a single original one-line joke about working beside AI coding agents on demo day — the moment the agent that wrote everything crashes live and helpfully offers to generate a working version instead.

## How to run

```bash
python3 main.py
```

Requires Python 3.13, standard library only, no network access. The script creates `/output` if it does not exist.

## Output

- File: `/output/entry.txt`
- Encoding: UTF-8
- Length: 1–280 Unicode code points (153 in this entry)
- Content: one line of text, not only whitespace, byte-identical on every run
