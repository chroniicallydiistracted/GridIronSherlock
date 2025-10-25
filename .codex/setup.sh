#!/usr/bin/env bash
set -euo pipefail

export PIP_REQUIRE_VIRTUALENV=1

if command -v corepack >/dev/null 2>&1; then corepack enable; fi
if command -v npm >/dev/null 2>&1 && ! command -v pnpm >/dev/null 2>&1; then npm i -g pnpm@9 >/dev/null 2>&1 || true; fi

python3 -m venv .venv || true
. .venv/bin/activate
python -m pip install -U pip wheel
if [ -f requirements.txt ]; then python -m pip install -r requirements.txt; fi
python -m pip install -U ortools duckdb pandas fastapi "uvicorn[standard]" pydantic

if command -v R >/dev/null 2>&1; then
  R -q -e "if(!'remotes'%in%installed.packages()[,1]) install.packages('remotes', repos='https://cloud.r-project.org')"
  R -q -e "pkgs<-c('nflreadr','nflfastR','nflseedr','arrow','duckdb'); ti<-setdiff(pkgs, rownames(installed.packages())); if(length(ti)>0) install.packages(ti, repos='https://cloud.r-project.org')"
fi

if [ -f Makefile ]; then make setup || true; fi

