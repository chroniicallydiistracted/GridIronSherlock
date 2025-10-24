#!/usr/bin/env bash
set -euo pipefail

if command -v corepack >/dev/null 2>&1; then
  corepack enable
fi

if command -v npm >/dev/null 2>&1; then
  npm -v >/dev/null 2>&1 || true
fi

if command -v python3 >/dev/null 2>&1; then
  python3 -m pip install --upgrade pip
fi

if command -v pip >/dev/null 2>&1; then
  pip install --upgrade poetry uv
fi

if command -v R >/dev/null 2>&1; then
  R -q -e "if(!'remotes'%in%installed.packages()[,1]) install.packages('remotes', repos='https://cloud.r-project.org')"
  R -q -e "pkgs<-c('nflreadr','nflfastR','nflseedr','arrow','duckdb'); to_install<-setdiff(pkgs, rownames(installed.packages())); if(length(to_install)>0) install.packages(to_install, repos='https://cloud.r-project.org')"
fi

if [ -f Makefile ]; then
  make setup || true
fi
