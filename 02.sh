#!/usr/bin/env bash

./setup.sh
export PATH=~/mc/bin:$PATH
conda-forge-tick --run 0
conda-forge-tick --run 1
doctr deploy --token --built-docs . --deploy-repo regro/cf-graph --deploy-branch-name master .
