#!/bin/bash

export KIWICLIENT_DIR=../kiwiclient
export CMDFSK_DIR=../decoders/cmdfsk

python3 schedule.py $1

